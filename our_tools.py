# This file aims to separate contain our made up functions that ease out our work

import json
import os

# Gets information from patients.txt and convert it to a dictionary
def GetData():
    with open("patients.json", 'r') as file: 
        patients = json.loads(file.read())
    return patients

# rewrite new changes current (patients) dictionary to patients.txt file
def rewrite(patients):
    with open("patients.json", 'w') as file:
        file.write(json.dumps(patients, indent=4)) 

# prompt the user to enter the needed ID with the needed checks
def AskID(patients):
    ID = input("Enter the patient's ID: ")
    if not ID.isdigit():
        print("ID numbers can only consist of digits\n") # To ensure the user can't enter letters, this is helpful for sorting later
        return # To return none (useful later in the code)
    elif ID not in patients:
        print("ID does not exist")
        return # To return none (useful later in the code)
    return ID # If code reaches this point, it is certain that ID is valid. Thus, no if statement needed
    
def DisplayTable(header, givenValues):
    # givenValues must be nested lists where each list is a row
    if type(givenValues[0]) != type([]):
        givenValues = [givenValues] # ease creating tables with only one row of data 
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

def ClearConsole():
    if os.name == 'nt': # If system is windows
        os.system("cls")
    else: # Linux and mac
        os.system("clear")

def Rerun():
    while True:
        choice = input("Do you want to preform another task? (y/n): ")
        
        if choice.lower() == "y":
            ClearConsole()
            return True
        elif choice.lower() == "n":
            ClearConsole()
            return False
        else:
            print("only choose y or n")