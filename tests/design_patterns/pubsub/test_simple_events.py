import unittest

from design_patterns.pubsub.simple_events import Event


class Stub:
    def __init__(self):
        self.calls = 0
        self.args = []

    def __call__(self, *args):
        self.calls += 1
        self.args += args


class SimpleEventsTestCase(unittest.TestCase):
    def test_simple_tests(self):
        e = Event()
        f1 = Stub()
        f2 = Stub()
        f3 = Stub()

        e.subscribe(f1)
        e.subscribe(f2)

        e.emit(1, 2, 3, 'first', None, False)

        self.assertEqual(f1.calls, 1, 'first handler calls')
        self.assertEqual(f2.calls, 1, 'second handler calls')
        self.assertEqual(f1.args, [1, 2, 3, 'first', None, False], 'first handler arguments')
        self.assertEqual(f2.args, [1, 2, 3, 'first', None, False], 'second handler arguments')

        e.subscribe(f3)
        e.unsubscribe(f2)

        e.emit(2, 'second', True)
        self.assertEqual(f1.calls, 2, 'previously subscribed handler calls')
        self.assertEqual(f2.calls, 1, 'unsubscribed handler calls')
        self.assertEqual(f3.calls, 1, 'newly subscribed handler calls')

        e.subscribe(f2)
        e.emit(3, 'third')

        self.assertEquals(f2.calls, 2, 'unsubscribed handler calls after re-subscription and emit')


if __name__ == '__main__':
    unittest.main()
