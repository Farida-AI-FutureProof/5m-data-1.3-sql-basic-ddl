import duckdb

# Step 1: Connect to database
con = duckdb.connect('ddl_demo_1_3.db')
print("✅ Connected to DuckDB successfully.")

# Step 2: Create tables
con.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR UNIQUE NOT NULL
);
""")

con.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR NOT NULL,
    dept_id INTEGER,
    salary DECIMAL(10,2) CHECK (salary > 0),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
""")
print("✅ Tables created: departments, employees")

# Step 3: Alter table (add a new column)
con.execute("ALTER TABLE employees ADD COLUMN hire_date DATE;")
print("✅ Added 'hire_date' column to employees")

# Step 4: Create a view
con.execute("""
CREATE OR REPLACE VIEW v_employee_summary AS
SELECT e.emp_name, d.dept_name, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
""")
print("✅ View 'v_employee_summary' created")

# Step 5: Show schema
print("\n📄 Current tables:")
print(con.execute("PRAGMA show_tables;").fetchall())

print("\n📄 Current views:")
print(con.execute("PRAGMA show_views;").fetchall())

# Step 6: Close connection
con.close()
print("✅ Connection closed.")
