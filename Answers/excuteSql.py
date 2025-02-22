import sqlite3

# Connect to a database (it will create a new one if it doesn't exist)
conn = sqlite3.connect(':memory:')  # Use ':memory:' to create a temporary in-memory database
cursor = conn.cursor()

# Create a table (equivalent to SQL CREATE TABLE)
cursor.execute('''
    CREATE TABLE employees (
        code_id INTEGER  ,
        test_id INTEGER,
        date_tested Date,
        status TEXT
    )
''')

# Insert data (equivalent to SQL INSERT INTO)
cursor.execute('''
    INSERT INTO employees (code_id, test_id, date_tested, status)
    VALUES (3, 1, '20191120', 'Failed' ),
            (3, 1, '20200613', 'Passed' ),
            (1, 2, '20201102', 'Passed' ),
            (1, 1, '20200507', 'Passed' ),
            (3, 1, '20191120', 'Failed' ),
            (1, 3, '20200417', 'Failed' ),
            (3, 1, '20200105', 'Failed' ),
            (1, 3, '20200425', 'Passed' ),
            (1, 1, '20200922', 'Failed' ),
            (1, 2, '20200922', 'Failed' ),
            (1, 1, '20200916', 'Passed' )
''')

# Commit the changes
conn.commit()

# Query the database (equivalent to SQL SELECT)
cursor.execute('SELECT * FROM employees where (test_id = 1 and \
               status="Passed") or (test_id = 2 and status="Failed")')
rows = cursor.fetchall()

# Display the results (equivalent to SQL SELECT * FROM employees)
print("All employees:")
for row in rows:
    print(row)

# Filter query (equivalent to SQL SELECT * FROM employees WHERE department='Engineering')
cursor.execute('SELECT *, count(*) as count_failed  \
               from employees \
               where status="Failed" \
               group by code_id, test_id, date_tested \
                ')
engineering_employees = cursor.fetchall()

print("\nEngineering employees:")
for employee in engineering_employees:
    print(employee)



# Clean up and close the connection
conn.close()
