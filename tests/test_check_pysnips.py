#!/usr/bin/env python
import os
import ast
import importlib
import glob
import shutil
import subprocess
import sys
import tempfile

cov = None
if os.environ.get("FLASK_COVERAGE"):
    from coverage import coverage

    cov = coverage(branch=True, include='app/')
    cov.start()


def test(coverage_var=False):
    """
    Run unit tests and print out coverage report
    :param coverage_var:
    :return:
    """
    if coverage_var and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if cov:
        cov.stop()
        cov.save()
        print('Coverage Summary:')
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'coverage')
        cov.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        cov.erase()


def main():
    test()


if __name__ == '__main__':
    main()
