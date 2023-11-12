import pytest
import datetime
from seasons import minutesConverter

def test_minuteConvert():
    minutesConverter(datetime.timedelta(1)) == "five hundred and twenty-five thousand, six hundred"


