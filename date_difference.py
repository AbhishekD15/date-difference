"""
Date Difference calculator

This script allows the user to input two dates and it will calculate the
number of days between them.

It accepts two dates as argumentsin the format DD MM YYYY.
"""
import argparse
import datetime

def validate_date(date):
    """ Validate date format """
    try:
        datetime.datetime.strptime(date, "%d %m %Y")
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be DD MM YYYY")


def is_leap_year(year):
    """ Check if year is leap year """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


def check_same_date(date1, date2):
    """ Check if both dates are same """
    if date1 == date2:
        return True
    else:
        return False


def days_in_month(month, year):
    """ Return number of days in a month """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28


def calculate_days(date):
    """ Calculate number of days from 01 01 1900 """
    day, month, year = date.split()
    day, month, year = int(day), int(month), int(year)
    total_days = 0
    if year >= 1900 and year <= 2010: # check if year is in range
        for each_year in range(1900, year): # calculate days for each year
            days_in_year = 366 if is_leap_year(each_year) else 365
            total_days += days_in_year
        for each_month in range(1, month): # calculate days for each month
            total_days += days_in_month(each_month, year)
        total_days += day
        return total_days
    else:
        raise ValueError("Year should be between 1900 and 2010")


def date_difference(date1, date2):
    """"Calculate difference between two dates

    Parameters
    ----------
    date1 : date in format DD MM YYYY
    date2 : date in format DD MM YYYY

    Returns
    -------
    tuple 
        Tuple of dates in ascending order and difference between them
    """
    num_of_days = 0
    if validate_date(date1) and validate_date(date2):
        if not check_same_date(date1, date2):
            days1 = calculate_days(date1)
            days2 = calculate_days(date2)
            num_of_days = abs(days1 - days2)
        else:
            raise ValueError("Dates are same")
    if days1 < days2: # check if date1 is before date2
        return date1, date2, num_of_days
    else:
        return date2, date1, num_of_days

if __name__ == "__main__":
    """This is executed when run from the command line"""
    parser = argparse.ArgumentParser(description="Calculate difference between two dates")
    parser.add_argument("date1", help="Enter first date in DD MM YYYY format")
    parser.add_argument("date2", help="Enter second date in DD MM YYYY format")
    args = parser.parse_args()
    date1 = args.date1
    date2 = args.date2
    date1, date2, num_of_days = date_difference(date1, date2)
    #date1, date2, num_of_days = date_difference("24 12 2005", "08 01 1995")

    print(f"{date1} {date2} {num_of_days}")
