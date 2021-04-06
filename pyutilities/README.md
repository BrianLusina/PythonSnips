# Files

These are a series of Python file access methods

## User file

### Objective:

+ First get user input,
+ check if input is in a seperate file,
+ if not in file, write input to that file, return success message
+ if in file, return error message

## JSON files

A JSON file looks like so:

```json
[
{"id":1,"first_name":"Karen","last_name":"Wheeler","email":"kwheeler0@ameblo.jp","gender":"Female"},
{"id":2,"first_name":"Larry","last_name":"Morales","email":"lmorales1@phpbb.com","gender":"Male"},
{"id":3,"first_name":"Rose","last_name":"Lane","email":"rlane2@census.gov","gender":"Female"},
{"id":4,"first_name":"Cheryl","last_name":"Frazier","email":"cfrazier3@lulu.com","gender":"Female"},
...
]
```

json_files is a Python file demonstrating the use and creation of JSON files in Python. Objective is to obtain

## JSON Stats

Class to check stats of the JSON file, check the count for genders Returns the count for male, female in a list, with
each list containing data for each gender, e.g

```python
[[Males: 46],[Females:54]]
```

## Word Reader

TASK : File based database Search... - User should be able to search for words in a paragraph/text - Search results
should be displayed in the terminal - Add the results and display the total number in terminal

## Domestic Trade

You have been hired by a trade company to write a program. They have given you a CSV (comma separated value, used in
spreadsheets) file containing sales data by transaction for 10,000 sales transactions. write a function that calculates
the grand total of sales for a given item across all stores.

Your output should be in a form of a dictionary, with total_KSH as a key and the total as a value.

Additionally, the company wants to know which store location made the largest sales for that item. Add that as another
hash key-value pair.

Example: Given a `TRANS.csv` of:

store,sku,amount Nairobi,DM1210,7000 KSH Nairobi,DM1182,1968 KSH Naivasha,DM1182,5858 KSH Mombasa,DM1210,6876 KSH
Nakuru,DM1182,5464 KSH

If we enter 'DM1182', you program should return:
{:total_KSH=> 13290, :largest=> 'Naivasha'}.