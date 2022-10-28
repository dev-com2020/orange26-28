import csv

fields = ["name", "branch", "year", 'cgpa']
rows = [
    ['Sanchit', 'COE', '2', '9.1'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Nikhil', 'COE', '2', '9.0'],
]
mydict =[{'branch': 'COE', 'cgpa': '9.0',
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1',
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3',
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5',
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8',
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1',
         'name': 'Sahil', 'year': '2'}]

file = "records2.csv"
with open(file, 'w') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(mydict)
