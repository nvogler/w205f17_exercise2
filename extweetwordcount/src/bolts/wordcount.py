from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
	
	# Connect to database
	self.conn = psycopg2.connect(database="postgres", user="postgres")
	
	# Create database
	try:	
		self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE DATABASE tcount")
		self.cur.close()
		self.conn.commit()
		self.conn.close()
	except:
		print ("Count not create tcount")
 
	# Connect to tcount
	self.conn = psycopg2.connect(database="tcount", user="postgres")
	
	# Create table
	self.cur = self.conn.cursor()
	self.cur.execute('''DROP TABLE tweetwordcount''')
	self.cur.execute('''CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY	NOT NULL, \
		count INT	NOT NULL);''')
	self.conn.commit()	
	
    def process(self, tup):
        word = tup.values[0]
	
	# Connect to tcount
	self.conn = psycopg2.connect(database="tcount", user="postgres")
 	self.cur = self.conn.cursor()
	
	# Update Count
	## Check prior word appearance
	if word in self.counts.keys():
		# Update local
		self.counts[word] = self.counts[word] + 1
		# Update database
		self.cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", \
			(self.counts[word], word))	       
	else:
		# Update local
		self.counts[word] = 1
		# Update database
		self.cur.execute("INSERT INTO tweetwordcount (word, count) \
			VALUES (%s, %s)", (word, "1"))

	# Emit and log
	self.emit([word], self.counts[word])
        self.log("%s, %d", (word, count))
