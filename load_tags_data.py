# the above just indicates to use python to intepret this file


import sys  # a python module with system functions for this OS
import pymongo  # python MongoDB module

# connect with mongo DB here
from pymongo import MongoClient

client = MongoClient()

# set the database
db = client['moviesdb']

# drop and recreate the collection
#db.drop_collection('ratings')
db.create_collection('tags')

# specify the collection to use
tagsCollection = db.tags

# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system
#    standard input file
# ------------------------------------------------------------
file2 = open('tags.dat')

for line in file2:
    word = line.split('::')
    userid = word[0]
    movieid = word[1]
    tags = word[2]
    timestamps = word[3]
    tagsCollection.insert_one(
                                 {
                                 "UserID": userid,
                                 "MovieID": movieid,
                                 "Tag": tags,
                                 "Timestamp": timestamps,
                                 }
                        )
# -----------------------------------
# sys.stdin call 'sys' to read a line from standard input,
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
# movie file format -->MovieID::Title::Genres
# 1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy
# process incoming lines of file

# insert data into mongo

print("process finished")
