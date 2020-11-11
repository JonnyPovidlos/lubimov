import sqlite3

def create_db(db_name):
    with sqlite3.connect(db_name) as connection:
        connection.executescript("""
            CREATE TABLE book_of_registration (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            second_name TEXT NOT NULL,
            series TEXT NOT NULL,
            number TEXT NOT NULL,
            date_of_issue TEXT NOT NULL,
            obtaining INTEGER NOT NULL,
            issuing INTEGER NOT NULL,
            consent INTEGER NOT NULL
            )
        """)

def db_is_empty(db_name):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.execute("""
            SELECT *
            FROM book_of_registration
        """)
        row = cursor.fetchone()
        if row is None:
            return False
        return True

def insert_into_db(db_name, info):
    with sqlite3.connect(db_name) as connection:
        connection.execute(
            'INSERT INTO book_of_registration (last_name, first_name, second_name, series, number, date_of_issue, obtaining, issuing, consent)'
            f'VALUES ("{info["last_name"]}", "{info["first_name"]}", "{info["second_name"]}", "{info["series"]}", "{info["number"]}", "{info["date_of_issue"]}", "{info["obtaining"]}", "{info["issuing"]}", "{info["consent"]}")'
        )

def get_line(db_name, last_name):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.execute(
            'SELECT *'
            'FROM book_of_registration '
            f'WHERE last_name = "{last_name}" '
        )
        rows = cursor.fetchall()
        result = []
        for row in rows:
            obtaining = row[6]
            issuing = row[7]
            consent = row[8]
            if obtaining and issuing and consent:
                print(row[1:6])
                result.append(row[1:7])
        return result