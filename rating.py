import sqlite3, datetime

def submitRating():
    getToday = datetime.datetime.now()
    today = getToday.strftime("%x")
    conn = sqlite3.connect("DATABASE FILE")
    cur = conn.cursor()
    cur.execute("INSERT INTO ratingstbl (ratings, ratingdate) VALUES (?, ?)", (ratingInput, today))
    conn.commit()
    conn.close()

print("A rating is required between 1 - 10.")
ratingInput = input("Enter Rating: ")
try:
    rating = int(ratingInput)
    if rating > 10 or rating < 0:
        print("Your rating was invalid.")
    elif rating >= 8:
        print("Your rating was excellent!")
    elif rating >= 6 and rating < 8:
        print("Your rating was good!")
    elif rating >= 4 and rating < 6:
        print("Your rating was average!")
    elif rating >= 2 and rating < 4:
        print("Your rating was poor!")
    elif rating >= 0 and rating < 2:
        print("Your rating was bad!")
except:
    print("Invalid character entered.")
submitRating()
