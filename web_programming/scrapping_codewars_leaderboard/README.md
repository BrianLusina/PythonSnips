You should get and parse the html of the codewars leaderboard page. You can use the 'nokogiri' gem(Ruby) or '
BeautifulSoup'(Python) or 'jsdom'(Javascript). For Javascript: Return a Promise resolved with your 'Leaderboard' Object!

You must meet the following criteria:

Return a 'Leaderboard' object with a position property. Leaderboard#position should contain 500 'User' objects.
Leaderboard#position[i] should return the ith ranked User(1 based index). Each User should have the following
properties:

``` python
User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer
```

Ex:

``` python
an_alien = leaderboard.position[3]   # => #<User:0x3124da0 @name="myjinxin2015", @clan="China Changyuan", @honor=21446>
an_alien.name                        # => "myjinxin2015"
an_alien.clan                        # => "China Changyuan"
an_alien.honor                       # => 21446
```