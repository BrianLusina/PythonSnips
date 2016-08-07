class RemoveDuplicates(object):
    def __init__(self, duplicated_list):
        self.duplicated_list = duplicated_list

    def remove_duplicates(self):
        return list(set(self.duplicated_list))
