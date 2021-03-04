# For easy setup, name your table ratingstbl and add two columns named rating and ratingdate

import sqlite3

conn = sqlite3.connect("DATABASE FILE")
cur = conn.cursor()

def allCommands():
    print("Commands: help, allratings ([<|>] [mm/dd/yyyy]), order [asc|des], count ([<|>] [#]), average, deleteall")

def allRatings(): # Shows all ratings, before or after a date, if specified
    if ">" in sqlcommand:
        datesplit = sqlcommand.split()
        datetuple = (datesplit[2])
        cur.execute("SELECT * FROM ratingstbl WHERE ratingdate >= (?)", (datetuple,))
        ratingresults = cur.fetchall()
        for x in ratingresults:
            print(x[0])
    elif "<" in sqlcommand:
        datesplit = sqlcommand.split()
        datetuple = (datesplit[2])
        cur.execute("SELECT * FROM ratingstbl WHERE ratingdate <= (?)", (datetuple,))
        ratingresults = cur.fetchall()
        for x in ratingresults:
            print(x[0])
    else:
        cur.execute("SELECT * FROM ratingstbl")
        ratingresults = cur.fetchall()
        for x in ratingresults:
            print(x[0])
    conn.close()

def orderRatingsAsc(): # Shows all ratings in an ascending order
    cur.execute("SELECT * FROM ratingstbl ORDER BY ratings")
    ratingresults = cur.fetchall()
    for x in ratingresults:
        print(x[0])
    conn.close()

def orderRatingsDes(): # Shows all ratings in a descending order
    cur.execute("SELECT * FROM ratingstbl ORDER BY ratings DESC")
    ratingresults = cur.fetchall()
    for x in ratingresults:
        print(x[0])
    conn.close()

def countRatings(): # Counts the total number of votes submitted, condition may apply if it's above/below a rating
    if ">" in sqlcommand:
        condsplit = sqlcommand.split()
        condtuple = (condsplit[2])
        cur.execute("SELECT COUNT(ratings) FROM ratingstbl WHERE ratings > (?)", (condtuple,))
        ratingresults = cur.fetchall()
        for x in ratingresults:
            print(x[0])
    elif "<" in sqlcommand:
        condsplit = sqlcommand.split()
        condtuple = (condsplit[2])
        cur.execute("SELECT COUNT(ratings) FROM ratingstbl WHERE ratings < (?)", (condtuple,))
        ratingresults = cur.fetchall()
        for x in ratingresults:
            print(x[0])
    else:
        cur.execute("SELECT COUNT(ratings) FROM ratingstbl")
        ratingresults = cur.fetchall()
        for x in ratingresults:
            print(x[0])
    conn.close()

def averageRatings(): # Calculates the average rating
    cur.execute("SELECT AVG(ratings) FROM ratingstbl")
    ratingresults = cur.fetchall()
    for x in ratingresults:
        print(x[0])
    conn.close()

def deleteAll(): # Deletes all ratings
    cur.execute("DELETE FROM ratingstbl")
    conn.commit()
    conn.close()

print("Type \'help\' to see a list of commands.")
sqlcommand = input("Enter command: ").lower()

if sqlcommand == "help":
    allCommands()
elif "allratings" in sqlcommand:
    allRatings()
elif sqlcommand == "order asc":
    orderRatingsAsc()
elif sqlcommand == "order des":
    orderRatingsDes()
elif "count" in sqlcommand:
    countRatings()
elif sqlcommand == "average":
    averageRatings()
elif sqlcommand == "deleteall":
    print("The records you're about to delete cannot be recovered.")
    delAllPrompt = input("Are you sure you want to delete all the records? ").lower()
    if delAllPrompt == "yes":
        deleteAll()
        print("All records have now been deleted.")
else:
    print("Command not found.")
