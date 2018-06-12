import unittest

from beginning.operator import slices, cut


class OperatorTestCase(unittest.TestCase):
    def test_slices(self):
        now = '2018-06-12 11:22:33'
        expected = now[0:4], now[5:7], now[8:10], now[11:13], now[14:16], now[17:19]
        result = slices[0:4, 5:7, 8:10, 11:13, 14:16, 17:19](now)
        self.assertTupleEqual(result, expected)

    def test_cut(self):
        now = '20180612112233'
        expected = now[:4], now[4:6], now[6:8], now[8:10], now[10:12], now[12:]
        result = cut(4, 6, 8, 10, 12)(now)
        self.assertTupleEqual(result, expected)
