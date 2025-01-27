import sqlite3
import json

def initialize_database():
    # Connect to the SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect("german_tutor.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level TEXT NOT NULL,
        theme TEXT NOT NULL,
        lesson_json TEXT NOT NULL
    )
    """)


    # Create the necessary tables if they don't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY,
        level TEXT,
        learned_material TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        content TEXT
    )
    """)

    # Optional: Initialize user data if not already present
    cursor.execute("SELECT COUNT(*) FROM user_info")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO user_info (id, level, learned_material)
        VALUES (1, 'A1', '')
        """)
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()


def get_user_info():
    conn = sqlite3.connect("german_tutor.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_info (id INTEGER PRIMARY KEY, level TEXT, progress TEXT)")
    cursor.execute("SELECT * FROM user_info WHERE id = 1")
    user = cursor.fetchone()
    conn.close()
    return user or {"level": "A1", "progress": ""}

def log_progress(category, content):
    conn = sqlite3.connect("german_tutor.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS progress (id INTEGER PRIMARY KEY, date TEXT, category TEXT, content TEXT)")
    cursor.execute("INSERT INTO progress (date, category, content) VALUES (datetime('now'), ?, ?)", (category, content))
    conn.commit()
    conn.close()

def save_lesson_to_db(lesson_content):
    conn = sqlite3.connect("german_tutor.db")
    cursor = conn.cursor()

    # Insert the lesson as a whole JSON object
    cursor.execute("""
        INSERT INTO lessons (level, theme, lesson_json)
        VALUES (?, ?, ?)
    """, (
        lesson_content["lesson"]["level"],
        lesson_content["lesson"]["theme"],
        json.dumps(lesson_content)
    ))

    conn.commit()
    conn.close()
