
import sqlite3

create = """CREATE TABLE IF NOT EXISTS Roster(
    Name TEXT,
    Species TEXT,
    Age INTEGER,
    Rank TEXT
);"""


insert = """INSERT OR IGNORE INTO Roster (Name, Species, Age)
    VALUES ('Benjamin Sisko', 'Human', 40),
           ('Jadzia Dax', 'Trill', 300),
           ('Kira Nerys', 'Bajoran', 29);"""


sql = "UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'"

with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    
   
    cursor.execute(create)  
    
 
    cursor.execute(insert) 
    
  
    cursor.execute(sql)
    
   
    connection.commit()

 
    query = "SELECT Name, Age FROM Roster WHERE Species = ?"
    cursor.execute(query, ('Bajoran',))  
    
    results = cursor.fetchall()
    for row in results:
        print(f"Name: {row[0]}, Age: {row[1]}")

   
    query = "DELETE FROM Roster WHERE Age > ?"
    cursor.execute(query, (100,))
    connection.commit()

 
    cursor.execute("PRAGMA table_info(Roster)")  
    columns = [column[1] for column in cursor.fetchall()]
    if 'Rank' not in columns:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

 
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ('Captain', 'Benjamin Sisko'))
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ('Lieutenant', 'Ezri Dax'))
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ('Major', 'Kira Nerys'))
    connection.commit()

   
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    results = cursor.fetchall()
    for row in results:
        print(row)




