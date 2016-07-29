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

Class to check stats of the JSON file, check the count for genders
Returns the count for male, female in a list, with each list containing data for each gender, e.g
```python
[[Males: 46],[Females:54]]
```

## Word Reader

TASK : File based database
      Search...
     - User should be able to search for words in a paragraph/text
     - Search results should be displayed in the terminal 
     - Add the results and display the total number in terminal