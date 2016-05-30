from datetime import datetime
#create a new file called myfile.txt
journalNote = open("myfile.txt", "w")
#write data to id
journalEntry = journalNote.write("Log:1, \n Date: " +str(datetime.now()) + "\n Author: Brian Lusina, \n Rank: Scout. \n\n So much to say,yet it will not"
                                                       "be enough to describe what my squad and I went through that night. We did our daily rounds"
                                                            "as per our duties.\n It was always cold, but today was exceptionally chilly. We joked an laughed that it was "
                                                                           "probably our captain who had entered our patrol region, we loved the guy, but he had a heart made of ice."
                                                                           "")

#close the file
journalNote.close()

"""Reading the file contents to the console"""
f = open("myfile.txt","r")
try:
    print(f.read())
except IOError:
    print("Something went wrong with reading the file")
