import sqlite3

create = """CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT,
    Rating REAL  -- Rating column will be added later
);
"""

insert = """INSERT OR IGNORE INTO Books (Title, Author, Year_Published, Genre)
    VALUES
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');
"""


sql = "UPDATE Books SET Year_Published = 1950 WHERE Year_Published = 1949"

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()

    cursor.execute(create)
    cursor.execute(insert)
    cursor.execute(sql)
    connection.commit()

    
    query = "SELECT Title, Author FROM Books WHERE Genre = ?"
    cursor.execute(query, ('Dystopian',))
    
    results = cursor.fetchall()
    print("Books in the Dystopian Genre:")
    for row in results:
        print(f"Title: {row[0]}, Author: {row[1]}")

    
    delete_query = "DELETE FROM Books WHERE Year_Published < ?"
    cursor.execute(delete_query, (1950,))
    connection.commit()

    
    cursor.execute("PRAGMA table_info(Books)")  
    columns = [column[1] for column in cursor.fetchall()]
    if 'Rating' not in columns:
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    
    
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.8, 'To Kill a Mockingbird'))
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.7, '1984'))
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.5, 'The Great Gatsby'))
    connection.commit()

    
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    results = cursor.fetchall()
    
    print("\nBooks Sorted by Year Published (Ascending Order):")
    for row in results:
        print(row)
