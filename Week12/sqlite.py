import sqlite3

con = sqlite3.connect("project.db")
cursor = con.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL
    )
""")

# Insert some data
cursor.execute("INSERT INTO cars (name, price) VALUES (?, ?)", ("Toyota Corolla", "PKR 5,200,000"))
cursor.execute("INSERT INTO cars (name, price) VALUES (?, ?)", ("Honda Civic", "PKR 6,800,000"))
cursor.execute("INSERT INTO cars (name, price) VALUES (?, ?)", ("Suzuki Alto", "PKR 2,100,000"))

# Read and print data
print("All cars in database:")
for row in cursor.execute("SELECT * FROM cars"):
    print(row)

con.commit()
con.close()

print("Done!")