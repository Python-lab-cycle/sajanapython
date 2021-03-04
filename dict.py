import csv
csv_col =['ID','Name','place']
dict_data=[{'ID':1,'Name':'dhiana','place':'mvpzha'},
           {'ID':2,'Name':'ansala','place':'mvtpzha'},
           {'ID':3,'Name':'Najmal','place':'Malappuram'},
           {'ID':4,'Name':'Ameen','place':'kannur'},
	   {'ID':5,'Name':'Ajmal','place':'idukki'},
	   {'ID':6,'Name':'Jeny','place':'Alappuzha'},
	   {'ID':7,'Name':'Anu','place':'Muvattupuzha'},
	   {'ID':8,'Name':'Afla','place':'Hightech'},
	   {'ID':9,'Name':'sajana','place':'nellimattom'},
	   {'ID':10,'Name':'jerin','place':'Kothamangalam'}]

try:
    with open("names.csv",'w')as file1:
        writer1=csv.DictWriter(file1,fieldnames=csv_col)
        writer1.writeheader()
        for data in dict_data:
            writer1.writerow(data)
except IOError:
    print("i/o error")
    """abcdgdfg
    afss
    sdfgs"""
data=csv.DictReader(open("Names.csv"))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)
