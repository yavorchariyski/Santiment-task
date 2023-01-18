import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('metrics.db')

# Query the data in the metrics table
query = "SELECT * FROM metrics"
data = pd.read_sql_query(query, conn)

# Print the data
print(data)

# Close the connection
conn.close()

# # Clear the data in the metrics table
# conn.execute("DELETE FROM metrics")
# conn.commit()

# DROP TABLE
# conn.execute("DROP TABLE metrics")
