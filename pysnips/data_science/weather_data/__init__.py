# -*- coding: utf-8 -*-


class WeatherData(object):
    def __init__(self):
        # open and read the file
        weather_file = open("weather.dat")
        with weather_file as data:
            rows = []
            # get all the rows and store them in a list
            for line in data.readlines():
                elem = line.split()
                rows.append(elem)
        self.rows = rows
        # record to keep track of the spreads
        self.spread_data = {}

    def calculate_spread(self):
        """
        Calculates the spread for each day in the weather data
        Will populate spread data,a dictionary with each day's spread already calculated,
        the spread is the value, the day is the key
        """
        # mark the header columns they will be used as indices
        headers = self.rows[0]

        # acquire the index of Dy, MxT and Mnt
        dy_indx = headers.index("Dy")
        mxt_indx = headers.index("MxT")
        mnt_indx = headers.index("MnT")

        # loop through the data, getting the spread
        # skip the header
        for x in range(2, len(self.rows[1:])):
            # current row
            row = self.rows[x]

            # current day
            row_day = row[dy_indx]

            # clean data and return the clean values for max temp and min temp
            mx, mn = self.clean_data(row[mxt_indx], row[mnt_indx])

            # get the spread
            spread = mx - mn

            self.spread_data[row_day] = spread

    def get_spread(self):
        """
        Evaluates which is the highest spread and from which day that is
        :return: day and spread as a tuple
        :rtype: tuple
        """
        spreads = self.spread_data.values()

        # get the maximum spread
        mx_spread = max(spreads)

        for k, v in self.spread_data.items():
            if v == mx_spread:
                return k, v

    @staticmethod
    def clean_data(mx, mn):
        """
        Cleans the data removing unwanted characters such as +="£$%^&*()_/*-+. from the numbers
        Gets the character that is a digit from the string and adds it to the final clean result
        :param mx: maximum temperature as a string
        :param mn: minimum temperature as a string
        :return: A tuple with the 1st index as max temp, 2nd as min temp
        :rtype: tuple
        """
        # list comprehension to return only digits
        clean_min = "".join(char for char in mn if char.isdigit())
        clean_max = "".join(char for char in mx if char.isdigit())

        return int(clean_max), int(clean_min)


def main():
    weather_data = WeatherData()
    # calculate the spread
    weather_data.calculate_spread()
    # print to stdout
    print(weather_data.get_spread())


if __name__ == "__main__":
    main()
