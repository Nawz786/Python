import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nawaz@1509"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS db")
cursor.execute("USE db")
cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
cursor.close()
db.close()

---------

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nawaz@1509",
    database="CareerHub"  # ← replace if the DB name is different
)

cursor = db.cursor()
cursor.execute("SELECT * FROM Jobs LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()

---------

#%%
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nawaz@1509"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS db")
cursor.execute("USE db")
cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
cursor.close()
db.close()

#%%
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nawaz@1509",
    database="CareerHub"  # ← replace if the DB name is different
)

cursor = db.cursor()
cursor.execute("SELECT * FROM Jobs LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
#%%
import mysql.connector

# Step 1: Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nawaz@1509",
    database="CareerHub"  # make sure this DB exists
)

cursor = db.cursor()

# Step 2: Insert a row into the Jobs table
insert_query = """
INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
insert_values = (2, 'Python Developer', 'Develop backend APIs', 'Remote', 85000, 'Full-time', '2025-06-24')
cursor.execute(insert_query, insert_values)
print("✅ Inserted a new job")

# Step 3: Update the inserted row
update_query = """
UPDATE Jobs
SET Salary = 90000
WHERE JobTitle = 'Python Developer'
"""
cursor.execute(update_query)
print("✅ Updated job salary")

# Step 4: Alter the table to add a new column (if it doesn't already exist)
try:
    alter_query = "ALTER TABLE Jobs ADD COLUMN ExperienceRequired INT DEFAULT 0"
    cursor.execute(alter_query)
    print("✅ Altered table to add 'ExperienceRequired' column")
except mysql.connector.errors.ProgrammingError as e:
    if "Duplicate column name" in str(e):
        print("⚠️ Column 'ExperienceRequired' already exists.")
    else:
        raise

# Step 5: Display all rows in Jobs table
cursor.execute("SELECT * FROM Jobs")
rows = cursor.fetchall()
print("\n📋 All rows in Jobs table:")
for row in rows:
    print(row)

# Cleanup
cursor.close()
db.close()

#%%



