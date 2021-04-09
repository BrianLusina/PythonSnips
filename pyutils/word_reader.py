class WordData(object):
    """
    TASK : File based database
              Search...
             - User should be able to search for words in a paragraph/text
             - Search results should be displayed in the terminal
             - Add the results and display the total number in terminal
    """

    @staticmethod
    def words(w):
        count = 0
        file = open("datafile.txt")
        for x in file.readlines():
            print(x)
            if w in x:
                count += 1
        print(w + " has a count of " + str(count))


WordData.words("est")
