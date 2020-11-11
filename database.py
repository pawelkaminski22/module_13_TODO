import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn


def execute_sql(sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    conn = create_connection(r"C:\Kodilla\Module13_TODO\todo_database.db")
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def select_all():
    """
    Query all rows in the table
    :param conn: the Connection object
    :return:
    """
    lines = []
    conn = create_connection(r"C:\Kodilla\Module13_TODO\todo_database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM todo")
    rows = cur.fetchall()
    for row in rows:
        if row[3] == '1' or row[3] == 'True':
            completed = 'Yes'
        else:
            completed = "No"

        line = {'title': row[1], 'description': row[2], 'completed': completed}
        lines.append(line)
    return lines


def select_movie(id):
    """
    Query tasks from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    lines = []
    conn = create_connection(r"C:\Kodilla\Module13_TODO\todo_database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM todo WHERE id={id}")
    rows = cur.fetchall()
    for row in rows:
        if row[3] == '1':
            completed = 'true'
        else:
            completed = "false"
        line = {'title': row[1], 'description': row[2], 'completed': completed}
        #lines.append(line)
        print(line)
    return line


def add_movie(movie):
    conn = create_connection(r"C:\Kodilla\Module13_TODO\todo_database.db")
    """
    Create a new projekt into the projects table
    :param conn:
    :param projekt:
    :return: projekt id
    """
    sql = '''INSERT INTO todo(title, description, completed)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    val = (movie['title'], movie['description'], movie['completed'])
    cur.execute(sql, val)
    conn.commit()
    return cur.lastrowid


def update(id, data):
    conn = create_connection(r"C:\Kodilla\Module13_TODO\todo_database.db")
    """
    update status, begin_date, and end date of a task
    :param conn:
    :param table: table name
    :param id: row id
    :return:
    """
    title = data['title']
    description = data['description']
    completed = data['completed']
    values = f"title = '{title}', description = '{description}', completed = '{completed}'"
    print(values)
    sql = f''' UPDATE todo
             SET {values}
             WHERE id = {id}'''
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)


def delete_movie(id):
    conn = create_connection(r"C:\Kodilla\Module13_TODO\todo_database.db")
    """
    Delete from table where attributes from
    :param conn:  Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
    """

    sql = f'DELETE FROM todo WHERE id={id}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print("Deleted")

