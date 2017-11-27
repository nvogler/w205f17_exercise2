from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

	# Connect to database
        conn = psycopg2.connect(database="postgres", user="postgres")
	# Create db
        try:
                conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cur = conn.cursor()
                cur.execute("CREATE DATABASE tcount")
                cur.close()
                conn.close()
        except:
                print ("Count not create tcount")

        # Connect to tcount
        conn = psycopg2.connect(database="tcount", user="postgres")

        # Create table
        cur = conn.cursor()
        cur.execute('''DROP TABLE IF EXISTS tweetwordcount;''')
	cur.execute('''CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY  NOT NULL, \
                count INT       NOT NULL);''')
        conn.commit()

    def process(self, tup):
        word = tup.values[0]

	# Connect to tcount
        conn = psycopg2.connect(database="tcount", user="postgres")
        cur = conn.cursor()
	
	## Check prior word appearance
        if self.counts[word] != 0:
                # Update database
                cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", \
                        (self.counts[word], word))
	else:
		# Update database
                cur.execute("INSERT INTO tweetwordcount (word, count) \
                        VALUES (%s, %s)", (word, "1"))

	# Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
