##Time Degrees

Note : Please use python 3.4.3 , there is round off issue that is being resolved with python 2.7 , THANKS !

Time , time , time . Your task is to write a function that will return the degrees on a analog clock from a digital time that is passed in as parameter . The digital time is type string and will be in the format 00:00 . You also need to return the degrees on the analog clock in type string and format 360:360 . Remember to round of the degrees . Remeber the basic time rules and format like 24:00 = 00:00 and 12:60 = 13:00 . Create your own validation that should return "Check your time !" in any case the time is incorrect or the format is wrong , remember this includes passing in negatives times like "-01:-10".

A few examples :
```python
clock_degree("00:00") will return : "360:360"
clock_degree("01:01") will return : "30:6"
clock_degree("00:01") will return : "360:6"
clock_degree("01:00") will return : "30:360"
clock_degree("01:30") will return : "30:180"
clock_degree("24:00") will return : "Check your time !"
clock_degree("13:60") will return : "Check your time !"
clock_degree("20:34") will return : "240:204"
```
Remember that discrete hour hand movement is required - snapping to each hour position and also coterminal angles are not allowed. Goodluck and Enjoy !
