import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Verify cmd line args
if len(sys.argv) != 2:
        print ("Invalid arguments.\n Usage is: histogram.py k1,k2")
        exit(1)

# Connect to the database
conn = psycopg2.connect(database="tcount", user="postgres")
cur = conn.cursor()

# Pull k values
k1, k2 = sys.argv[1].split(',')

# Run query
query = "SELECT word, count FROM tweetwordcount WHERE count BETWEEN " + str(k1) + \
	" AND " + str(k2) + ";"
cur.execute(query)

# Display results
results = cur.fetchall()
for result in results:
	print (str(result[0]) + ": " + str(result[1]) + "\n")
