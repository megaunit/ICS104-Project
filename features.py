# This file aims to separate contain the main features our program offers

from our_tools import rewrite, AskID, DisplayTable



def AddPatient(patients):
    ID = input("Enter the patient's ID: ")
    if ID not in ID.isdigit():
        print("ID numbers can only consist of digits") # To ensure the user can't enter letters, this is helpful for sorting later
        return
    elif ID in patients:
        print("ID Already exist")
        return
    
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

def UpdateInfo(patients):
    ID = AskID()
    if ID == None:
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

def AddMedicalHistory(patients):
    ID = AskID()
    if ID == None:
        return

    patient_data = patients.get(ID) # .get() will return None if ID doesn't exist
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

def DisplayData(patients):
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