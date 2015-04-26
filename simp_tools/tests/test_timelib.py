import unittest
import datetime
import pandas
from numpy import testing

from simp_tools import timelib


class TestCoerceDate(unittest.TestCase):

    def test_candidates(self):
        assert timelib.coerce_time(None) is None
        assert timelib.coerce_time(datetime.time(12)) == datetime.time(12)
        assert timelib.coerce_time('12:00') == datetime.time(12)
        assert timelib.coerce_time(pandas.Timestamp('12:00')) == datetime.time(12)
        testing.assert_raises(ValueError, timelib.coerce_time, 'str')