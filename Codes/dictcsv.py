import pandas as pd
import numpy as np
import xlrd 
import csv

mydict={6: [7, 6, 8, 9, 10], 11: [12, 11, 14, 16, 17, 18, 15, 19, 20, 39, 40, 51], 21: [2, 3, 4, 1, 5, 22, 21, 23, 24, 25, 89, 26, 27, 85, 28, 34, 32, 33, 35, 36, 37, 38], 29: [30, 29, 31, 42, 41, 111, 44, 43, 45, 46, 47, 48, 49, 50, 60, 59], 54: [55, 54, 56, 57, 58, 52, 65, 69, 67, 66, 68, 70, 112, 74, 73, 71, 72, 76], 106: [63, 106, 109, 75, 53, 62], 94: [64, 94, 110, 78, 79, 77, 107, 108, 61, 114], 86: [80, 13, 81, 83, 84, 82, 86, 87, 88, 90, 91, 98, 100, 113, 104, 105, 103, 92, 93, 95, 97, 96, 99, 101, 102]}
with open('ZJ-Lev-2.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       for l in value:
          writer.writerow([l, key])
