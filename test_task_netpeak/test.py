import sqlite3
import os


def create_tables_and_insert_data():
    db_file = "bonus.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        salary REAL
    );
    """

    create_department_table = """
    CREATE TABLE IF NOT EXISTS department (
        department_id INTEGER PRIMARY KEY,
        bonus_rate REAL
    );
    """

    cursor.execute(create_users_table)
    cursor.execute(create_department_table)
    conn.commit()

    # Check if data exists before inserting
    cursor.execute("SELECT COUNT(*) FROM users")
    user_data_exists = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM department")
    department_data_exists = cursor.fetchone()[0]

    if not user_data_exists:
        insert_users_data = """
        INSERT INTO users (name, department_id, salary)
        VALUES
            ('John', 1, 1000),
            ('Regina', 2, 1200),
            ('Alice', 2, 1200),
            ('Bob', 1, 1500),
            ('Carol', 3, 900),
            ('David', 2, 800),
            ('Vic', 3, 500);
        """
        cursor.execute(insert_users_data)

    if not department_data_exists:
        insert_department_data = """
        INSERT OR REPLACE INTO department (department_id, bonus_rate)
        VALUES
            (1, 0.1),
            (2, 0.2),
            (3, 0.15);
        """
        cursor.execute(insert_department_data)

    conn.commit()
    conn.close()


def calculate_total_bonus():
    db_file = "bonus.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    query = """
    SELECT u.name AS name, (u.salary * d.bonus_rate) AS total_bonus
    FROM users AS u
    JOIN department AS d ON u.department_id = d.department_id
    ORDER BY total_bonus DESC;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]}: {row[1]}")

    conn.close()


if __name__ == "__main__":
    create_tables_and_insert_data()
    calculate_total_bonus()
