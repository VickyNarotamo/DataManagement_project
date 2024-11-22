import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname="data_management_framework",  # Replace with your database name
        user="postgres",               # Replace with your PostgreSQL username
        password="caosthebest1",           # Replace with your PostgreSQL password
        host="localhost",                   # Replace with your host (e.g., localhost)
        port="5432"                         # Replace with your port (default is 5432)
    )
    print("Database connection successful!")
except Exception as e:
    print("Error connecting to the database:", e)
    exit()

# SQL query
query = """
SELECT 
    ds.name AS data_source_name,
    COUNT(rd.data_id) AS total_records,
    MAX(rd.ingestion_time) AS last_ingestion_time
FROM project_schema.data_sources ds
LEFT JOIN project_schema.raw_data rd ON ds.source_id = rd.source_id
GROUP BY ds.name;
"""

# Execute the query and load data into a Pandas DataFrame
try:
    df = pd.read_sql_query(query, conn)
    print("Query executed successfully!")
    print(df.head())  # Print first few rows for verification
except Exception as e:
    print("Error executing query:", e)
    conn.close()
    exit()

# Visualize data using seaborn
try:
    plt.figure(figsize=(10, 6))
    sns.barplot(x='data_source_name', y='total_records', data=df, palette='viridis')
    plt.title('Total Records by Data Source', fontsize=16)
    plt.xlabel('Data Source', fontsize=12)
    plt.ylabel('Total Records', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data_source_chart.png')  # Save chart as PNG in your project folder
    plt.show()
    print("Visualization saved as 'data_source_chart.png'")
except Exception as e:
    print("Error creating visualization:", e)

# Close the database connection
conn.close()
print("Database connection closed.")
