# Dictionary contains employee positions, names and age (from exercise 3)
employeeDictionary = {
    "date": "10.12.2024.",
    "employees": [
        {
            "position": "sales manager",
            "name": "Igors",
            "age": 36
        },
        {
            "position": "hotel manager",
            "name": "Dace",
            "age": 38
        },
        {
            "position": "cook",
            "name": "Ralfs",
            "age": 39
        },
        {
            "position": "administrator",
            "name": "Juris",
            "age": 22
        }
    ]
}

# For Loop
# pārbaudīt, kurš darbinieks ir vecākais
oldestEmployeeAge = 0
employeeName = ""
for employee in employeeDictionary['employees']:
    employeeAge = employee.get("age")
    if employeeAge > oldestEmployeeAge:
        oldestEmployeeAge = employeeAge
        employeeName = employee.get("name")
print("The oldest employee is", employeeName + ".")

# Range Loop
# saskaita, cik darbiniekiem ir vismaz 38 gadu vai mazāk par 25
countOfEmployees = 0
for x in range(len(employeeDictionary['employees'])):
    if employeeDictionary['employees'][(x-1)].get("age")>=38:
        countOfEmployees += 1
    elif employeeDictionary['employees'][(x-1)].get("age")<25:
        countOfEmployees += 1
print("There are", countOfEmployees, "such employees in this hotel.")

# While
# izvadīt katra darbinieka amatu
boo = True
sk = 0
while boo:
    firstLetter = employeeDictionary['employees'][sk].get("position")
    if (firstLetter[0] == 'a' or firstLetter[0] == 'e' or firstLetter[0] == 'i' or firstLetter[0] == 'o' or firstLetter[0] == 'u' or firstLetter[0] == 'y'):
        print(employeeDictionary['employees'][sk].get("name"), "is an", employeeDictionary['employees'][sk].get("position") + ".")
        sk = sk + 1
    else:
        print(employeeDictionary['employees'][sk].get("name"), "is a", employeeDictionary['employees'][sk].get("position") + ".")
        sk = sk + 1
    if sk == len(employeeDictionary['employees']):
        boo = False