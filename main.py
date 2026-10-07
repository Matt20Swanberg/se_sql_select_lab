"""
SQL SELECT Lab

This project demonstrates how to execute SQL queries against a SQLite
database using Python and Pandas. The queries practice selecting columns,
creating aliases, using CASE statements, working with string functions,
performing aggregate calculations, and formatting dates.
"""

# STEP 1A
# Import SQLite for database access and Pandas for working with query results
import sqlite3
import pandas as pd

# STEP 1B
# Establish a connection to the SQLite database
conn = sqlite3.connect("data.sqlite")

# STEP 2
# Select employee numbers and last names from the employees table
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)
print(df_first_five)

# STEP 3
# Select the same employee information with the column order reversed
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)
print(df_five_reverse)

# STEP 4
# Use an alias to rename employeeNumber as ID in the query results
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS "ID"
    FROM employees
""", conn)
print(df_alias)

# STEP 5
# Use CASE to categorize employees based on their job title
df_executive = pd.read_sql("""
    SELECT firstName, lastName, jobTitle,
    CASE
        WHEN jobTitle = "Sales Manager (APAC)"
            OR jobTitle = "Sale Manager (EMEA)"
            OR jobTitle = "Sales Manager (NA)"
        THEN "Executive"
        ELSE "Not Executive"
    END AS role
    FROM employees
""", conn)
print(df_executive)

# STEP 6
# Calculate the number of characters in each employee's last name
df_name_length = pd.read_sql("""
    SELECT length(lastName) AS name_length
    FROM employees
""", conn)
print(df_name_length)

# STEP 7
# Extract the first two characters of each employee's job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)
print(df_short_title)

# STEP 8
# Calculate each order total by multiplying price by quantity,
# round each total, and sum all order totals together
sum_total_price = pd.read_sql("""
    SELECT SUM(round(priceEach * quantityOrdered)) AS order_total
    FROM orderDetails
""", conn)["order_total"]
print(sum_total_price)

# STEP 9
# Extract the day, month, and year from each original order date
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
        strftime("%d", orderDate) AS day,
        strftime("%m", orderDate) AS month,
        strftime("%Y", orderDate) AS year
    FROM orders
""", conn)
print(df_day_month_year)

conn.close()