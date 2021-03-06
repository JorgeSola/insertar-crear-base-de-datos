import sqlite3

#Primer ejemplo de como meter datos en una tabla sql

tablaSql = {'nombre':'Pedro', 'apellido':' ' , 'edad':56, 'ciudad':'Vitoria'}

row = []
for key in tablaSql:
    row.append(tablaSql[key])
print(row)

conn = sqlite3.connect('./data/datos.db')

c = conn.cursor()

# Insert a row of data

c.execute("INSERT INTO personas VALUES (NULL,?,?,?,?)", row)
conn.commit()


#///////////////////////////////////////////////////////////////////////////

#Segundo ejemplo de crear tabla e introducir datos de forma rápida.

sql_films = {
"Title":"Batman",
"Year":"1989",
"Rated":"PG-13",
"Released":"23 Jun 1989",
"Runtime":"126 min",
"Genre":"Action, Adventure",
"Director":"Tim Burton",
"Writer":"Bob KaneBatman characters",
"Actors":"Michael Keaton",
"Plot":"The Dark Knight of Gotham City begins his war on crime with his first major enemy being the clownishly homicidal Joker.",
"Language":"English, French, Spanish",
"Country":"USA, UK",
"Awards":"Won 1 Oscar. Another 8 wins & 26 nominations.",
"Poster":"https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_SX300.jpg",
"Ratings":"Internet Movie Database",
"Source":"Metacritic",
"Metascore":"69",
"imdbRating":"7.5",
"imdbVotes":"322,524",
"imdbID":"tt0096895",
"Type":"movie",
"DVD":"25 Mar 1997",
"BoxOffice":"N/A",
"Production":"Warner Bros. Pictures",
"Website":"N/A",
"Response":"True"}

#////////////////////////////////////////////////////////////////////////////////////

#Sirve para crear una tabla desde cero en una base de datos ya creada.

keys = []
for key in sql_films:
    keys.append(key)

c = conn.cursor()

# Insert a row of data
for key in keys:
    c.execute("ALTER TABLE peliculas ADD COLUMN {}".format(key))
conn.commit()

#/////////////////////////////////////////////////////////////////////////////////////

row = []
# Sirve para rellenar una tabla de datos sql
for key in sql_films:
    row.append(sql_films[key])
print(row)

c.execute("INSERT INTO peliculas VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
conn.commit()
conn.close()
