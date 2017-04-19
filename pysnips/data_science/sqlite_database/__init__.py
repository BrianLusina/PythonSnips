import sqlite3


class AccessSimiti(object):
    def __init__(self, db_name):
        """
        Creates an object of this class
        :param db_name: the name of the database to access
        """
        # connect to the database
        self.simiti = sqlite3.connect(db_name)

        # get a cursor object
        self.cursor = self.simiti.cursor()

    def query_table(self, table_name):
        """
        Queries a particular table from the database
        :return: a cursor
        """

    def select_cols_from_table(self, cols="*"):
        """
        Query columns from table

        cursor.execute("SELECT * FROM mzigos WHERE id='1a2015828ee354885afd0c8083170876';")
        print(cursor.fetchone())

        :param cols the columns to query, default is all of them
        :return: all the rows from the table
        """
        if cols != "*":
            self.cursor.execute("SELECT ")
        results = self.cursor.fetchall()
        self.cursor.close()

        return results

    def insert_values(self, table_name, values):
        """
        inserts values into the database
        :param table_name the name of the table
        :param values the values to insert into the table as a tuple with the entries matching the columns
        :return:
        """

        for value in values:
            v = (str(value))
            self.cursor.execute("INSERT INTO " + table_name + " VALUES " + v)
            self.simiti.commit()
        self.simiti.close()


value_list = [('784bc244b6053553cb5b3a4f9250ba79', '56b4f14f4ac4272e63ca1a45', 'FlashCards',
               'It is a set of cards bearing information, as words or numbers, on either or both sides, used in classroom drills or in private study.',
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('b2d90b9ac7661631a8608e7eb89bff06', '56b4f14f4ac4272e63ca1a45', 'Grammar Workbooks',
               'The set of structural rules governing the composition of clauses, phrases, and words in any given natural language. This is categories, we looks at the tenses , reading practices,Modal Verbs,Direct speech,short stories,various topics,English grammar tenses,mixed and progressive tense',
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('0fd0d7070e17b8eb25cac9207c788bcf', '56b4f14f4ac4272e63ca1a45', 'Grammar Worksheets',
               'The set of structural rules governing the composition of clauses, phrases, and words in any given natural language. This is categories, we looks at the tenses , reading practices,Modal Verbs,Direct speech,short stories,various topics,English grammar tenses,mixed and progressive tense',
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('58110c37b29af91a4fd7a48bb9db1f58', '56b4f177b57c58846304a8a0', 'English Jokes',
               'A display of humour in which words and images are used within a specific and well defined narrative to make people laugh.',
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('68ecb331acf689a1a2d531d3926f8b58', '56b4f177b57c58846304a8a0', 'Role Play',
               "This is changing of one's behaviour to assume a role,either unconsciously to fill a sociol role, or consciously to act out an adopted role.Mostly adpoted within theatres or educational settings.",
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('403a06e3848b1fdc7134601fd46a7265', '56b4f177b57c58846304a8a0', 'Songs',
               'Traditional poems or rhymes for childern that are educational and fun', 'package',
               'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('e6c3993ab9b9e52e4e65fa58e1b5ce43', '56b4f177b57c58846304a8a0', 'Tongue Twisters',
               'Phrases that are designed to be difficult to articulate properly, and can be used as a type of spoken (or sung) word game.',
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('66052456c2b3535bf48812d3267b4360', '56b4f177b57c58846304a8a0', 'Wally',
               "This is a series of hidden picture puzzle games that are engineered to stimulate the children's mind and thinking capacity.",
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', ''),

              ('1a2015828ee354885afd0c8083170876', '56b4f14f4ac4272e63ca1a45', "Learner's Library",
               'A journey through different stories that provide resourceful information, facts and roles that can be reffered to thereafter in test, exams or even in everyday life circumstances.',
               'package', 'd41d8cd98f00b204e9800998ecf8427e', '1460618542327.0', 1463149315952, 0, '', '')]
