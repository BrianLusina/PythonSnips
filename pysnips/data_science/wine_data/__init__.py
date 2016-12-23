from data_science.data_download import DataDownload
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv
from pprint import pprint


class RedWineData(object):
    """

    """

    def __init__(self):
        self.wine_url = None

    def download_red_wine(self):
        """
        Downloads red wine data from a given url and saves it to a file
        :return:
        """
        # store the url in a variable for retrieval
        self.wine_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

        red_wine = DataDownload(self.wine_url, "red_wine.csv")
        return red_wine.download()

    def extract_data(self):
        """
        Extracts the red wine data and stores the data in a numpy array
        :return: A Numpy 2d array
        :rtype: list
        """
        file_name = self.download_red_wine()[0]
        with open(file_name, "r") as f:
            wines = list(csv.reader(f, delimiter=";"))
        wines = np.array(wines[1:], dtype=np.float)
        return wines

    def get_shape(self):
        """
        Gets the shape of the Numpy 2D array
        This is the number of rows and columns in the
        :return: Dictionary with the number cols and rows
        :rtype: dict
        """
        wine_data = self.extract_data()
        return dict(rows=wine_data.shape[0], cols=wine_data.shape[1])
