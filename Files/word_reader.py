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
        d = {w:count}
        file = open("", "r")
        if w in file.readlines():
            c = d.get(w)
            c += 1
        print(d)