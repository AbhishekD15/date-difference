
import pytest
from date_difference import date_difference
from date_difference import validate_date
from date_difference import check_same_date
from date_difference import calculate_days
from date_difference import days_in_month
from date_difference import is_leap_year

def test_validate_date():
    assert validate_date("01 01 1900") == True
    assert validate_date("01 01 2010") == True
    with pytest.raises(ValueError):
        validate_date("01-01-1899")
   

def test_check_same_date():
    assert check_same_date("01 01 1900", "01 01 1900") == True
    assert check_same_date("01 01 1900", "01 01 1901") == False

def test_days_in_month():
    assert days_in_month(1, 1900) == 31
    assert days_in_month(2, 1900) == 28
    assert days_in_month(2, 2000) == 29

def test_is_leap_year():
    assert is_leap_year(1900) == False
    assert is_leap_year(2000) == True

def test_calculate_days():
    assert calculate_days("01 01 1900") == 1
    assert calculate_days("01 01 1901") == 366
    with pytest.raises(ValueError):
        calculate_days("01 01 1899")
    with pytest.raises(ValueError):
        calculate_days("01 01 2011")

def test_date_difference():
    assert date_difference("01 01 1900", "01 01 1901") == ("01 01 1900", "01 01 1901", 365)
    assert date_difference("08 01 1995", "24 12 2005") == ("08 01 1995", "24 12 2005", 4003)
    assert date_difference("15 04 1969", "12 09 1945") == ("12 09 1945", "15 04 1969", 8616)