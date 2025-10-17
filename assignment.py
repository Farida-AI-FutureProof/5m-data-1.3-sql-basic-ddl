import duckdb
import os

# ensure db folder exists
os.makedirs("db", exist_ok=True)

# connect (creates file if missing)
con = duckdb.connect("db/ddl_demo.db")
print("✅ Connected to DuckDB successfully!")

# create table
con.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);
""")
print("✅ Table 'employees' created.")

# alter table
con.execute("ALTER TABLE employees ADD COLUMN IF NOT EXISTS hire_date DATE;")
print("✅ Column 'hire_date' added (or already existed).")

# drop an old table if it exists
con.execute("DROP TABLE IF EXISTS old_employees;")
print("✅ Dropped table 'old_employees' if it existed.")

# show schema (list tables)
print("\n📄 Current tables:")
print(con.execute("PRAGMA show_tables;").fetchall())

con.close()
print("✅ Database connection closed.")
