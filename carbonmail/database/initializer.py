from carbonmail.database.connector import close_connection, connect
from carbonmail.database.operations import create
def initialize():
    connection = connect()
    sql_create_table_lists = """CREATE TABLE IF NOT EXISTS list (
			                    id integer PRIMARY KEY AUTOINCREMENT,
			                    name text NOT NULL
			                );"""

    sql_create_table_contact = """  CREATE TABLE IF NOT EXISTS contacts(
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL,
                                    email text NOT NULL,
                                    list_id integer NOT NULL,
                                    FOREIGN KEY (list_id) REFERENCES list(id)
                                    ON DELETE CASCADE
                            );"""
    
    create(connection,sql_create_table_lists)
    create(connection,sql_create_table_contact)
    
    close_connection(connection)