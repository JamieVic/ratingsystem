# Rating System
## About the Project
This rating project allows a user to enter a rating from 1 to 10 and their input is stored in a database file. The database can be accessed using the checkrating.py file where ratings can be checked, counted, ordered, provide an average and even delete all data in the file. This project also demonstrates the use of finding data before/after a date and above/below a number.
## How to Use
This program works using any Python interpreter. You can view the database data by using programs such as SQL Browser. The user is prompted to enter a rating from 1 to 10 which is then stored in a database file, along with the date the input was entered. The checkrating Python file will be typically used by the database admin to check the following data:
- Display all ratings
- Count how many ratings in the database
- Work out the average number of ratings
- Display all ratings in ascending/descending order
- Delete all ratings
To see the commands, you can type "help" in the checkrating Python file.
## How it Works
In the rating Python file, the user will enter their rating which is stored in the ratingInput variable. After pressing Enter, a function will be called that gets the date the rating is entered, converts it to mm/dd/yyyy format for readability, and stores it in the today variable. The try/except statement ensures a valid entry is made in the input function and the if/else statement checks the number to see which range it falls in and provides the user with feedback based on their rating. If the data is valid, both the date and input are stored in the database.

In the checkrating Python file, the user can connect to the database and check the data stored using various commands. A command can be used and stored in the sqlcommand input variable. An if/else statement checks to see if the user entered a valid command. If the database admin forgets a command, they can type "help" to get a list of available commands.

The allRatings function first checks to see if the user entered > or < to check ratings before/after the entered date. If no date is entered, all ratings in the database will be printed. There are two functions for ordering all the ratings in ascending and descending order which are named orderRatingsAsc and orderRatingsDes respectively. The countRatings function can count ratings above or below a number. If no above/below check is advised, all ratings in the database will be counted. The averageRatings function counts all the ratings in the database and prints the average rating. If for any reason all ratings in the database need to be deleted, that can be done using the deleteAll function.
