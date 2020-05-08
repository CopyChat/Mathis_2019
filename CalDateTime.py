#!/usr/bin/env python

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange

__version__ = "Time-stamp: <2019-08-28>"
__author__ = "Chao TANG chao.tang.1@gmail.com"

INPUT_FORMAT = '%Y-%m-%d %H:%M'


def date_diff_in_seconds(dt2: str, dt1: str):
    """
    calculate datetimedelta in Seconds
    :param dt2:
    :param dt1:
    :return:
    """
    datetime_obj_1 = datetime.strptime(dt1, INPUT_FORMAT)
    datetime_obj_2 = datetime.strptime(dt2, INPUT_FORMAT)

    timedelta = datetime_obj_2 - datetime_obj_1

    return timedelta.days * 24 * 3600 + timedelta.seconds


def date_diff_in_hours(dt2: str, dt1: str):
    """
    calculate datetimedelta in Seconds
    :param dt2:
    :param dt1:
    :return:
    """
    datetime_obj_1 = datetime.strptime(dt1, INPUT_FORMAT)
    datetime_obj_2 = datetime.strptime(dt2, INPUT_FORMAT)

    timedelta = datetime_obj_2 - datetime_obj_1

    return timedelta.days * 24 + round(timedelta.seconds/3600, 2)


datetime1 = input(f'Enter DateTime in {INPUT_FORMAT:s} ?\n')
datetime2 = input(f'Enter DateTime in {INPUT_FORMAT:s} ?\n')

print(f'{datetime2:s} - {datetime1:s} = \n'
      f'{date_diff_in_seconds(datetime2, datetime1):g} second')

print(f'{date_diff_in_hours(datetime2, datetime1):.2f} hours')

print(f'')
