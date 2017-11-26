import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Verify cmd line args
if len(sys.argv) > 2:
	print ("Too many arguments provided")
	exit(1)

# Connect to the database
conn = psycopg2.connect(database="tcount", user="postgres")
cur = conn.cursor()

# Determine appropiate action
## Pull all entries
if len(sys.argv) == 1:
	cur.execute("SELECT word, count FROM tweetwordcount")
	results = cur.fetchall()
	for result in results:
		print ("(" + str(result[0]) + ", " + str(result[1]) + "), ")
## Pull single entry	
else:
	word = sys.argv[1]
	cur.execute("SELECT word, count FROM tweetwordcount WHERE word=%s", (word,))
	count = cur.fetchone()
	if count:
		print ("Total number of occurrences of \"" + word + "\": " + str(count[1]))
	else:
		print (word + " not found.") 
