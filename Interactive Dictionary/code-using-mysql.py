import mysql.connector
import difflib
from difflib import get_close_matches

connection = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor =  connection.cursor()

word = input("Enter the word : ").lower()

query = cursor.execute("SELECT * FROM  Dictionary WHERE Expression = '%s' " %word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    qry = cursor.execute("SELECT * FROM  Dictionary")
    all_results = cursor.fetchall()
    data = dict(all_results)
    guesses = get_close_matches(word, data.keys(), cutoff = 0.5)
    confirmation = input("Did you mean %s instead? Please Enter Y if Yes or N if No : " %guesses[0]).upper()
    if confirmation == "Y":
        print(data[guesses[0]])
    elif confirmation == 'N':
        print("Enter word again!")