import os
import csv
pybankpath = os.path.join("..", "Pybank", "budget_data.csv")
with open (pybankpath, newline="") as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=",")
print (csv_reader)

