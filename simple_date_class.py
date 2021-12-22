
from __future__ import annotations

from datetime import datetime


WEEKDAYS = [
    'Poniedziałek',
    'Wtorek',
    'Środa',
    'Czwartek',
    'Piątek',
    'Sobota',
    'Niedziela'
]

DAYS_PER_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Data:
    
    def __init__(self, year: int, month: int, day: int) -> None:
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise TypeError("Year, month and day must be an int type!")

        if year < 1 or 1 <= month >= 12 or day < 1 or day > DAYS_PER_MONTHS[month]:
            raise ValueError("Wrong date!")

        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    def __eq__(self, data: Data):
        if not isinstance(data, Data):
            raise TypeError(f'Variable - {data}, is not a Data type !!!!')

        return self.__year, self.__month, self.__day == data.__year, data.__month, data.__day

    def __repr__(self):
        return f'Data(year={self.__year}, month={self.__month}, day={self.__day}'
    
    def __str__(self):
        return f'{self.__year:04}-{self.__month:02}-{self.__day:02}'
    
    def reprezentacja(self, s: str, since_year: bool = True) -> str:
        """
        returns a string in the format given by the arguments separator and since_year
        if since_year is True returns the date in the format YYY(separator)MM(separator)dd
        :param s: separator between year and month and between month and day
        :param since_year:
        :return:
        """
        if since_year:
            result = f'{self.__year:04}' \
                     f'{s}' \
                     f'{self.__month:02}' \
                     f'{s}' \
                     f'{self.__day:02}'
        else:
            result = f'{self.__day:02}{s}{self.__month:02}{s}{self.__year:04}'
        return result
        
    def day_of_year(self):
        """ returns number of day in year """
        return datetime(self.__year, self.__month, self.__day).timetuple().tm_yday
        
    def day_of_week(self):
        """

        :returns: name of weekday from date
        """
        return WEEKDAYS[datetime(self.__year, self.__month, self.__day).weekday()]

    def next_day(self):
        """

        :return: next day after the date
        """

        if self.__day + 1 > DAYS_PER_MONTHS[self.__month]:
            day = 1
            month = self.__month + 1
        else:
            day = self.__day + 1
            month = self.__month
        if month > 12:
            month = 1
            year = self.__year + 1
        else:
            year = self.__year

        return Data(year, month, day)
