import pandas
import datetime
from dateutil.relativedelta import relativedelta


def utc_now():
    return utc_timestamp(datetime.datetime.now())


def utc_now_str():
    return utc_timestamp_str(datetime.datetime.now())


def utc_timestamp(timestamp, tz='UTC'):
    return pandas.Timestamp(timestamp, tz=tz)


def utc_now_value():
    return utc_now().value


def utc_timestamp_str(timestamp):
    return utc_timestamp(timestamp).strftime('%d-%b-%y %H:%M:%S')


def timestamp_minute(timestamp):
    return timestamp + relativedelta(second=0, microsecond=0)


def get_pnl_zero(timestamp):
    days = -1 if timestamp.time() < datetime.time(6, 5) else 0
    return timestamp + relativedelta(days=days, hour=6, minute=5, second=0, microsecond=0)


def get_pnl_zero_now():
    timestamp = utc_now()
    return get_pnl_zero(timestamp)


def coerce_time(candidate):
    """Coerce the candidate into a datetime.time if possible using the
    methods applied by pandas.Timestamp

    Parameters
    ----------
    candidate: str, datetime, pandas.Timestamp
        The candidate to coerce into a datetime.time

    Returns
    -------
    datetime.time
    """
    if candidate is None:
        time = None
    elif isinstance(candidate, datetime.time):
        time = candidate
    else:
        try:
            time = pandas.Timestamp(candidate).time()
        except ValueError:
            raise ValueError(
                'Could not coerce time from candidate %s' % candidate)
    return time