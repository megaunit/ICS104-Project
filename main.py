import json
import os

# Brings the JSON file and convert it to a dictionary
with open("patients.txt", 'r') as file: 
    patients = json.loads(file.read())

#for more simplicity so we can recall it later any time
def rewrite():
    with open("patients.txt", 'w') as file:
            file.write(json.dumps(patients, indent=2)) 

def AddPatient():
    ID = input("Enter the patient ID: ")
    if ID not in ID.isdigit():
        print("ID numbers can only consist of digits") # To ensure the user can't enter letters, this is helpful for sorting later
    elif ID in patients:
        print("Patient ID already exist")
    else:
        name = input("Enter the patient's name: ")
        gender = input(f"Enter the {name}'s gender: ")
        year = input(f"Enter the {name}'s year of birth: ") ## make limitation for the current year at max
        month = input(f"Enter the {name}'s month of birth: ") ## limit it between 1 and 12
        day = input(f"Enter the {name}'s day of birth: ") ## limit it in 1 and 30
        blood = input(f"Enter the {name}'s blood type: ")
        city = input(f"Enter the {name}'s city: ")
        number = input(f"Enter the {name}'s number: ") ## consider not repeating the number
        email = input(f"Enter the {name}'s email address: ") ## consider not repeating the email
        
        birthday = f"{day}/{month}/{year}"
        patients[ID] = {
            "ID" : ID,
            "name": name,
            "gender": gender,
            "birthday": birthday,
            "blood": blood,
            "city": city,
            "number": number,
            "email": email
        }

        rewrite()

def UpdateInfo():
    ID = input("Which patient do you want to update (Patient ID)? ")
    if ID not in patients:
        print("ID does not exist")
        return
    while True:
        info = input("(choose from name, gender, birthday, blood, city, number, and email)\nWhat information do you want to update? ")
        if info in ['name', 'gender', 'birthday', 'blood', 'city', 'number', 'email']:
            break
        else:
            print("Choose only from the given choices")
    if info.lower() == "birthday":
        year = input("Enter the new year of birth: ") ## mention the patient name instead of just saying "the new info"
        month = input("Enter the new month of birth: ") 
        day = input("Enter the new day of birth: ")
        new_info = f"{day}/{month}/{year}"
    else: ## more elifs (formatting email and phone number. Do that also above in the AddPatient)
        new_info = input(f"Enter the new {info}: ")
    patients[ID][info.lower()] = new_info

    rewrite()

def AddMedicalHistory():
    ID = input("Enter the patient ID: ")
    patient_data = patients.get(ID) # .get() will return None if ID doesn't exist
    if patient_data == None:
        print("ID does not exist")
        return 
    patient_name = patient_data.get("name")
    
    doctor = input(f"Enter {patient_name}'s doctor: ")
    last_visit_year=input(f"Enter {patient_name}'s year of last visit: ")
    last_visit_month=input(f"Enter {patient_name}'s month of last visit: ")
    last_visit_day=input(f"Enter {patient_name}'s day of last visit: ")
    diagnosis = input(f"PEter {patient_name}'s diagnosis: ")
    medicine = input(f"Enter {patient_name}'s medicine: ")
    advice = input(f"Enter {patient_name}'s advice: ")
    last_visit = f"{last_visit_day}/{last_visit_month}/{last_visit_year}"

    medical_history_data = {
        "Correspondent Doctor": doctor,
        "Last Visit": last_visit,
        "diagnosis": diagnosis,
        "medications": medicine,
        "advice": advice
    }

    patients[ID]["medical_history"] = medical_history_data
    rewrite()

    return medical_history_data

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

def DisplayData():
    header = ['ID', 'Name', 'Gender', 'Birthday', 'Blood', 'City', 'Number', 'Email']
    data = [] # list which will contain all patients data as nested lists

    # adds patients data to the data list
    for patient in patients:
        data.append([patients[patient][info] for info in patients[patient] if info != 'medical_history'])

    # ask the user how he wants to sort the data
    while True:
        sorting = input("(ID, Name, City)\nChoose how do you want to sort the data in the table: ")
        sorting = sorting.lower()
        if sorting not in ['name', 'id', 'city']:
            print("You can only choose from the three given sorting methods")
        else:
            break
    
    # sorts data list according to the user's choice
    if sorting == "id":
        data.sort() # sorts by first element, which is ID in this  case
    elif sorting == "name":
        data.sort(key= lambda x:x[1]) # lambda function helps specifying index of element which will be key of sorting
    elif sorting == "city":
        data.sort(key= lambda x:x[5]) 

    DisplayTable(header, data)

DisplayData()