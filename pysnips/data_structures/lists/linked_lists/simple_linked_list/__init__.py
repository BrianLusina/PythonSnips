class LinkedList(object):
    def __init__(self, data=None):
        self.data = data
    
    def head(self):
        if self.data is None or len(data) == 0:
            raise EmptyListException("Can not get head of empty List")
    
    def push(self, value):
        pass

    def pop(self):
        pass
    

    def reversed(self):
        pass
    
    def __len__(self):
        return len(self.data) if self.data else 0
    

    

class EmptyListException(Exception):
    def __init__(self):
        pass



    