import unittest

from web.scrapping_codewars_leaderboard import solution


@unittest.skip
class CamperLeaderBoardTestCases(unittest.TestCase):
    def setUp(self):
        self.leaderboard = solution()

    def test_should_have_a_size_of_500(self):
        self.assertEquals(len(self.leaderboard.position), 500)

    def test_should_contain_the_correct_names(self):
        # since these are hard coded, you should substitute with the current top 5
        self.assertEquals(self.leaderboard.position[1].name, 'g964')
        self.assertEquals(self.leaderboard.position[2].name, 'GiacomoSorbi')
        self.assertEquals(self.leaderboard.position[3].name, 'myjinxin2015')
        self.assertEquals(self.leaderboard.position[4].name, 'ZozoFouchtra')
        self.assertEquals(self.leaderboard.position[5].name, 'SteffenVogel_79')

    def test_should_contain_correct_clan(self):
        # since these are hard coded, you should substitute with the current top 5
        self.assertEquals(self.leaderboard.position[1].clan, 'None')
        self.assertEquals(self.leaderboard.position[2].clan, '')
        self.assertEquals(self.leaderboard.position[3].clan, 'China Changyuan')
        self.assertEquals(self.leaderboard.position[4].clan, '')
        self.assertEquals(self.leaderboard.position[5].clan, 'CSV - SLayer')

    def test_should_contain_the_correct_honor(self):
        # since these are hard coded, you should substitute with the current top 5
        self.assertEquals(self.leaderboard.position[1].honor > 40000, True)
        self.assertEquals(self.leaderboard.position[2].honor > 20000, True)
        self.assertEquals(self.leaderboard.position[3].honor > 20000, True)
        self.assertEquals(self.leaderboard.position[4].honor > 15000, True)
        self.assertEquals(self.leaderboard.position[5].honor > 17000, True)


if __name__ == '__main__':
    unittest.main()
