"""Script to seed mockingbird database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

#Automatically drops database and creates it
os.system('dropdb mockingbird')
os.system('createdb mockingbird')

model.connect_to_db(server.app)
model.db.create_all()

# with open('data/_____blank_____.json') as f:
#     data = json.loads(f.read())

# Create instances of class XYZ + store them in list so we can use it to create fake ratings
# ____XYZ_____in_db = []
# for x in data:
#     title, overview, poster_path = (x['title'],
#                                     x['overview'],
#                                     x['poster_path'])
#     release_date = datetime.strptime(x['release_date'], '%Y-%m-%d')

#     db_XYZ = crud.create_movie(title,
#                                  overview,
#                                  release_date,
#                                  poster_path)
#     ____XYZ_____in_db.append(db_XYZ)

# Create 10 fake users for testing
# def create_10fake_users()
firstname_list = ['James','John','Sarah','Karen','Nancy','Robert','Michael','William','David',
'Richard','Mary','Patricia','Jennifer','Linda','Elizabeth','Barbara','Susan','Jessica','Joseph',
'Thomas','Charles','Christopher','Daniel','Matthew','Anthony','Donald','Lisa','Margaret','Betty','Sandra']

lastname_list = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez',
'Martinez','Hernandez','Lopez','Gonzalez','Wilson','Anderson','Thomas','Taylor','Moore','Jackson',
'Martin','Lee','Perez','Thompson','White','Harris','Sanchez','Clark','Ramirez','Lewis','Robinson']

for n in range(10):
    # Voila! Unique fake user details!
    rand_num = randint(1,10)
    email = f'user{n}{rand_num}mail@test.com'
    password = 'pass{n}{n}word'
    fname = choice(firstname_list)
    lname = choice (lastname_list)
    name = '{fname} {lname}'

    user = crud.create_user(email, password, name)
    # print (user)
    db.session.add(user)
db.session.commit()

# def load_sample_text():
#     """Load sample text into database to be made available as a dropdown selection menu"""

#     #data file format: source | author | imgurl | overview | text 

#     with open("static/sourcetext.txt") as text:
#         for row in text:
#             row = row.rstrip()
            # source, author, imgurl, overview, text = row.split("|")

#     

#             sample_txt = Sample_Text(restaurant_id=restaurant_id,
#                                     source=source, 
#                                     author=author, 
#                                     imgurl=imgurl, 
#                                     overview=overview,
#                                     text=text)

#             # Add to the session or it won't be stored
#             db.session.add(sample_txt)

#     db.session.commit()
