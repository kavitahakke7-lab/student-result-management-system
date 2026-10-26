import sqlite3


def create_db():

    con = sqlite3.connect("rms.db")
    cur = con.cursor()

    # ===== Course Table =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)

    # ===== Student Table =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            course TEXT,
            admission_date TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )
    """)

    # ===== Result Table =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_obtained TEXT,
            full_marks TEXT
        )
    """)

    # ===== User / Login Table =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    con.commit()
    con.close()


create_db()