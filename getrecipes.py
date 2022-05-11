# GET RECIPIES
# Author: Morgan Luttman
# Date: 5/26/2021
# Description: Microservice delivers to text file recipe URL data in JSON format
#              upon receipt of a run command from a signal file.


import json
import csv
import time

class Recipes:
    """Loads and save Recipe Website Data"""

    def __init__(self):
        self._websites = []
        self._results = {"Websites": self._websites}

    def read_csv(self, filename):
        """Reads and replaces all recipes in memory from CSV File"""
        with open(filename) as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                self._websites.append(rows)

    def write_json(self, filename):
        """Writes and replaces all recipes in JSON File from memory"""
        with open(filename, 'w') as jsonf:
            jsonf.write(json.dumps(self._results, indent=4))

if __name__ == "__main__":

    dataFilePath = 'data.csv'
    resultFilePath = 'recipes.json'

    while True:
        time.sleep(1)

        with open('signal.txt') as file:
            line = file.readline()

        if line == 'run\n':
            print("Serving Recipe URLs")
            serve = Recipes()
            serve.read_csv(dataFilePath)
            serve.write_json(resultFilePath)

            with open('signal.txt', 'w') as file:
                file.writelines('complete\n')

