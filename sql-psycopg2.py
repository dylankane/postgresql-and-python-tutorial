import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the artist table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" co;umn from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51  from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# Query 5 - select only the albums with "ArtistId" #51  from "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["51"])

# Query 6 - select all tracks where the "Composer" is "Queen" from the "Track"
# table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 select "Artist" by "Name" that doesnt exist in the "Atrist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', [test])

# fetch the results(mutiple)
results = cursor.fetchall()

# fetch the results (single)
# reults = fetchone()

# close the connection
connection.close

# print results
for result in results:
    print(result)
