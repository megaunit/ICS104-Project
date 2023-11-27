# This file aims to separate contain our made up functions that ease out our work

import json

# Gets information from patients.txt and convert it to a dictionary
def GetInfo():
    with open("patients.txt", 'r') as file: 
        patients = json.loads(file.read())
    return patients

# rewrite new changes current (patients) dictionary to patients.txt file
def rewrite(patients):
    with open("patients.txt", 'w') as file:
            file.write(json.dumps(patients, indent=2)) 

# prompt the user to enter the needed ID with the needed checks
def AskID(patients):
    ID = input("Enter the patient's ID: ")
    if ID not in ID.isdigit():
        print("ID numbers can only consist of digits") # To ensure the user can't enter letters, this is helpful for sorting later
    elif ID not in patients:
        print("ID does not exist")
    if ID:
        return ID # This makes the functions return None if ID entered ID is invalid
    
def DisplayTable(header, givenValues):
    # givenValues must be nested lists where each list is a row
    structure = [header]
    structure.extend(givenValues)
    columns_width = []
    for row, row_values in enumerate(structure):
        for column, element in enumerate(row_values):
            if row == 0:
                columns_width.append(len(str(element)))
                continue
            if len(str(element)) > columns_width[column]:
                columns_width[column] = len(str(element))
    horizontalDividerLen = (len(columns_width)-1)*3 # Adds the sum of widths of all vertical dividers
    for i in columns_width:
        horizontalDividerLen+=i
    
    print("")
    for currentRow in structure:
        for cellNumber, cellValue in enumerate(currentRow):
            print(cellValue + " "*(columns_width[cellNumber]-len(cellValue)), end='')
            if (cellNumber+1) != len(currentRow):
                print(" | ", end='')
            else:
                print("") # to go to next line
        if (structure.index(currentRow)+1) != len(structure):
            print("-"*horizontalDividerLen)
    print("")

# A useful example of how this function works in case tests are needed
# createTable(list(choice(list(patients.values())).keys()), [["@"*randint(1,4) for i in range(7)] for _ in range (3)])
