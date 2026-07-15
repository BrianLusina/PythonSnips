import unittest
from typing import List
from parameterized import parameterized
from algorithms.hash_table.duplicate_file_in_system import find_duplicate

FIND_DUPLICATE_FILE_IN_SYSTEM_TEST_CASES = [
    (
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)",
        ],
        [
            ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
            ["root/a/1.txt", "root/c/3.txt"],
        ],
    ),
    (
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
        ],
        [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]],
    ),
    (
        [
            "data/files 1.csv(data1)",
            "data/files/processed 2.csv(data2)",
            "data/files/backup 3.csv(data1)",
            "data/archives 4.csv(data3)",
            "data/archives/old 5.csv(data2)",
        ],
        [
            ["data/files/1.csv", "data/files/backup/3.csv"],
            ["data/files/processed/2.csv", "data/archives/old/5.csv"],
        ],
    ),
    (
        [
            "usr/local/bin 1.sh(scriptX) 2.sh(scriptY)",
            "usr/local/lib 3.sh(scriptZ)",
            "usr/local/share 4.sh(scriptX)",
            "usr/local/share/tools 5.sh(scriptY)",
        ],
        [
            ["usr/local/bin/1.sh", "usr/local/share/4.sh"],
            ["usr/local/bin/2.sh", "usr/local/share/tools/5.sh"],
        ],
    ),
    (
        [
            "documents/reports 1.pdf(report1) 2.pdf(report2)",
            "documents/presentations 3.pdf(presentation1)",
            "documents/reports/old 4.pdf(report1)",
            "documents/archive 5.pdf(archive1)",
        ],
        [["documents/reports/1.pdf", "documents/reports/old/4.pdf"]],
    ),
    (
        [
            "root/notes 1.md(note1) 2.md(note2)",
            "root/notes/meetings 3.md(note3)",
            "root/notes/summaries 4.md(note1)",
            "root/summaries 5.md(note4)",
            "root/summaries/meetings 6.md(note2)",
        ],
        [
            ["root/notes/1.md", "root/notes/summaries/4.md"],
            ["root/notes/2.md", "root/summaries/meetings/6.md"],
        ],
    ),
]


class FindDuplicateFileInSystemTestCase(unittest.TestCase):
    @parameterized.expand(FIND_DUPLICATE_FILE_IN_SYSTEM_TEST_CASES)
    def test_find_duplicate(self, paths: List[str], expected: List[List[str]]):
        actual = find_duplicate(paths)
        actual.sort()
        self.assertListEqual(sorted(expected), actual)


if __name__ == "__main__":
    unittest.main()
