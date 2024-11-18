def is_leap_year(year: int) -> bool:
    """
    Given a year, this function returns a boolean indicating whether or not it is a leap year.

    :param year: an integer indicating a year.
    :return: A boolean indicating whether or not the year parameter is a leap year.
    """

    # A leap year is a calendar year that has an extra day added to it, making it 366 days long instead of 365.


    #  test_cases = [
    #         (1800, False),  # divisible by 4 and 100 but not by 400
    #         (1818, False),  # not divisible by 4
    #         (2000, True),   # divisible by 4 and 100 and 400
    #         (2020, True),   # divisible by 4 but not 100

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
