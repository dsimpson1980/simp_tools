import unittest

import datetime
import pandas
from numpy import testing

from simp_tools import datelib


class TestCoerceDate(unittest.TestCase):

    def test_candidates(self):
        assert datelib.coerce_date(None) is None
        assert datelib.coerce_date(
            datetime.date(2012, 4, 3)) == datetime.date(2012, 4, 3)
        assert datelib.coerce_date('3-Apr-2012') == datetime.date(2012, 4, 3)
        # Confirm European date formatting
        assert datelib.coerce_date('3-4-2012') == datetime.date(2012, 4, 3)
        assert datelib.coerce_date('3-4-12') == datetime.date(2012, 4, 3)
        assert datelib.coerce_date(
            pandas.Timestamp('3-Apr-12')) == datetime.date(2012, 4, 3)
        testing.assert_raises(ValueError, datelib.coerce_date, 'str')