import csv
with open('details.csv',newline='') as csvfile1:
          data=csv.DictReader(csvfile1)
          print("empno empname")
          print("--------------")
          for row in data:
              print(row['empno'],row['empname'])
