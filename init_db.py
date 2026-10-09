
import sqlite3

def initialize_database():
    # 1. Connect to SQLite (This automatically creates 'database.db' file in the folder)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    print("Creating database tables with full traceability fields...")

    # 2. Create Projects Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            idea TEXT NOT NULL
        )
    ''')

    # 3. Create Requirements Table (Links to Projects)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requirements (
            id TEXT PRIMARY KEY,
            project_id INTEGER,
            type TEXT,          -- functional or non-functional
            description TEXT,
            status TEXT DEFAULT 'draft',  -- draft / approved
            FOREIGN KEY (project_id) REFERENCES projects(project_id)
        )
    ''')

    # 4. Create User Stories Table (Links to Requirements via parent_id)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stories (
            id TEXT PRIMARY KEY,
            project_id INTEGER,
            parent_id TEXT,     -- Links to requirement id (REQ-01 / FR-01)
            story TEXT,
            acceptance_criteria TEXT, -- Stored as a simple text block
            status TEXT DEFAULT 'draft',
            FOREIGN KEY (project_id) REFERENCES projects(project_id),
            FOREIGN KEY (parent_id) REFERENCES requirements(id)
        )
    ''')

    # 5. Create Test Cases Table (Links to User Stories via parent_id)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tests (
            id TEXT PRIMARY KEY,
            project_id INTEGER,
            parent_id TEXT,     -- Links to user story id (US-01)
            scenario TEXT,
            expected_result TEXT,
            status TEXT DEFAULT 'draft',
            FOREIGN KEY (project_id) REFERENCES projects(project_id),
            FOREIGN KEY (parent_id) REFERENCES stories(id)
        )
    ''')

    # 6. Create Feedback Insights Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id TEXT PRIMARY KEY,
            project_id INTEGER,
            parent_id TEXT,     -- Links to the related feature/requirement ID
            feedback_text TEXT,
            theme TEXT,
            priority TEXT,      -- HIGH / MED / LOW
            FOREIGN KEY (project_id) REFERENCES projects(project_id)
        )
    ''')

    # Save changes and close the connection
    connection.commit()
    connection.close()
    print("Success! database.db has been created with all 5 tables.")

if __name__ == '__main__':
    initialize_database()
