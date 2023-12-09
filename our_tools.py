# This file aims to separate contain our made up functions that ease out our work

import json
import os
import os.path as path

# Gets information from patients.txt and convert it to a dictionary
def GetData():
    with open("patients.json", 'r') as file: 
        patients = json.loads(file.read())
    return patients

def newGetData():
    patients = {}
    for patient in os.listdir("./patients"):
        patients[patient] = {}  
        with open(f"./patients/{patient}/data.txt", 'r') as file:
            content = file.readlines()
            for line in content:
                info = line.strip().split(":")
                patients[patient][info[0]] = info[1]
        if not os.listdir(f"./patients/{patient}/medical_history"):
            continue
        patients[patient]["medical_history"] = {} # to initiate a medical history
        for medicalFile in os.listdir(f"./patients/{patient}/medical_history"):
            with open(f"./patients/{patient}/medical_history/{medicalFile}", 'r') as file:
                content = file.readlines()
                patients[patient]["medical_history"][medicalFile.strip(".txt")] = {} 
                for line in content:
                    info = line.strip().split(":")
                    patients[patient]["medical_history"][medicalFile.strip(".txt")][info[0]] = info[1]
            # patients[patient]

    return patients

# rewrite new changes current (patients) dictionary to patients.txt file
def rewrite(patients):
    with open("patients.json", 'w') as file:
        file.write(json.dumps(patients, indent=4)) 

def newRewrite(patients):
    for patient in patients:

        # First, we deal with the patient's personal data
        data = patients.get(patient)
        if not path.exists(f"./patients/{patient}"): # to check if patient file exists or not
            os.mkdir(f"./patients/{patient}")
        with open(f"./patients/{patient}/data.txt", 'w') as file:
            for key in data:
                if key != "medical_history": # Because we will save medical histories in a different folder
                    file.write(f"{key}:{data[key]}\n")

        # Second, we deal with patient's medical histories
        if not path.exists(f"./patients/{patient}/medical_history"): # to check if medical history folder exist or not
            os.mkdir(f"./patients/{patient}/medical_history")
        if not "medical_history" in data: # in case the patient doesn't have a medical_history yet
            continue
        for visitNumber in data['medical_history']:
            with open(f"./patients/{patient}/medical_history/{visitNumber}.txt", 'w') as file:
                visitFile = data['medical_history'].get(visitNumber)
                for key in visitFile:
                    file.write(f"{key}:{visitFile[key]}\n") 

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

