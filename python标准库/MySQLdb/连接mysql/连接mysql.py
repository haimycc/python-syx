import MySQLdb

print "Connecting..."
dbh = MySQLdb.connect()
print "Connection successful."
dbh.close()
