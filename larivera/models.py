import sqlite3



def create_table(db_file, table_name, columns):
    """
        Paramters:
        - db_file: The database file to connect to.
        - table_name: The name of the table to be created.
        - columns:  List of column definitions, where each column definition is a tuple
                    containing (column_name, data_type)

        Example Usage:
        - create_table("countyfair.db", "prize_hog", [("id", "INTEGER PRIMARY KEY AUTOINCREMENT"), ("name", "TEXT"), ("age", "INTEGER")])
    """
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    createTableSQL = f"CREATE TABLE IF NOT EXISTS {table_name} ("

    for column in columns:
        column_name, data_type = column
        createTableSQL += f"{column_name} {data_type}, "

    createTableSQL = createTableSQL.rstrip(", ")
    createTableSQL += ");"

    try:
        cursor.execute(createTableSQL)
        print(f"\t*\tTable {table_name} created successfully.")
        connection.commit()

    except sqlite3.Error as e:
        print(f"Error creating table {table_name}: {e}")

    finally:
        connection.close()


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def search_category_by_name(db_file, category_name):
    """

    """
    pass


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def insert_menu_item(db_file, category_table, item_information):
    """
        Parameters:
        - db_file: the database file of course, if you need this explained, turn around.
        - category_table:   i thought going with a category table to separate the menu items 
                            from eachother was a good way to do product analysis.
                                ex: burritos, tacos, deserts, seafood, American dishes
        - item_information: dictionary representation of item information

        ex: {"name": "Burrito", "description": "stuff", "ingredients": [], "calories": 1500}

    """
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    category_id = search_category_by_name(category_table)

    try:
        cursor.execute(insertItemSql)
        print(f"\t*\t{item_information['name']} successfully inserted into {category_table} table.")
        connection.commit()
    
