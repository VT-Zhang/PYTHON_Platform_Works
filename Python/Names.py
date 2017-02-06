students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printName(a):
    i = 0
    for x in a:
        print a[i]['first_name'], a[i]['last_name']
        i = i + 1
printName(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printUsers(dict):
   for x in dict:
       print x
       # print data
       i = 1
       for value in dict[x]:
           # print value
           # index = data.index("value")
           # print index
           length = len(value["first_name"]) + len(value["last_name"])
           print i, "-", value["first_name"], value["last_name"], "-", length
           i += 1

printUsers(users)
