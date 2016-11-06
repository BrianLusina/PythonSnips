from DataStructures.Queues import Queue

microsoftQueue = Queue()

microsoftQueue.enqueue("{user: ILoveWindows@gmail.com}")
microsoftQueue.enqueue("{user: cortanaIsMyBestFriend@hotmail.com}")
microsoftQueue.enqueue("{user: InternetExplorer8Fan@outlook.com}")
microsoftQueue.enqueue("{user: IThrowApplesOutMyWindow@yahoo.com}")

print(microsoftQueue)

# size of queue at beginning
print(microsoftQueue.size())

# first person leaves
microsoftQueue.dequeue()

# size of queue after
print(microsoftQueue.size())
