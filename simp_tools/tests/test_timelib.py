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


class TestMinutesInFreq(unittest.TestCase):

    def test_minutes_in_freq(self):
        assert timelib.minutes_in_freq('D') == 1440
        assert timelib.minutes_in_freq('H') == 60
        assert timelib.minutes_in_freq('T') == 1
        assert timelib.minutes_in_freq('15T') == 15
        assert timelib.minutes_in_freq('6H') == 360
        day = pandas.tseries.frequencies.to_offset('D')
        assert timelib.minutes_in_freq(day) == 1440