import json

# Brings the JSON file and convert it to a dictionary
with open("patients.txt", 'r') as file: 
    patients = json.loads(file.read())

#for more simplicity so we can recall it later any time
def rewrite():
    with open("patients.txt", 'w') as file:
            file.write(json.dumps(patients, indent=2)) 

def AddPatient():
    ID = input("Please enter the patient ID: ")
    if ID in patients:
        print("Patient ID already exist")
    else:
        name = input("Please enter the patient's name: ")
        gender = input("Please enter the patient's gender: ")
        year = input("Please enter the patient's year of birth: ") ## make limitation for the current year at max
        month = input("Please enter the patient's month of birth: ") ## limit it between 1 and 12
        day = input("Please enter the patient's day of birth: ") ## limit it in 1 and 30
        blood = input("Please enter the patient's blood type: ")
        city = input("Please enter the patient's city: ")
        number = input("Please enter the patient's number: ") ## consider not repeating the number
        email = input("Please enter the patient's email address: ") ## consider not repeating the email
        
        birthday = f"{day}/{month}/{year}"
        patients[ID] = {
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
        year = input("Please enter the new year of birth: ") ## mention the patient name instead of just saying "the new info"
        month = input("Please enter the new month of birth: ") 
        day = input("Please enter the new day of birth: ")
        new_info = f"{day}/{month}/{year}"
    else: ## more elifs (formatting email and phone number. Do that also above in the AddPatient)
        new_info = input(f"Please enter the new {info}: ")
    patients[ID][info.lower()] = new_info

    rewrite()
def add_medical_history():
    ID = input("Please enter the patient ID: ")
    patient_data = patients.get(ID)
    if ID not in patients:
        print("ID does not exist")
        return 

    patient_name = patient_data.get("name")
    if ID not in patients:
        print("Patient name is not registerd.")
        return 

    doctor = input(f"Please enter {patient_name}'s doctor: ")
    last_visit=input(f"Please enter {patient_name}'s last visit: ")
    diagnosis = input(f"Please enter {patient_name}'s diagnosis: ")
    medications = input(f"Please enter {patient_name}'s medications: ")
    advice = input(f"Please enter {patient_name}'s advice: ")

    medical_history_data = {
        "name": patient_name,
        "Correspondent Doctor": doctor,
        "Last Visit": last_visit,
        "diagnosis": diagnosis,
        "medications": medications,
        "advice": advice
    }
    directory="C:\\Users\\GAMER\\Desktop\\ICS\\test\\ICS104-Project\\Patient" #change the path to your patient folder 
    file_name=ID + ".txt"
    full_path=os.path.join(directory,file_name)
    with open(full_path, 'a') as file2:
        file2.write(json.dumps({ID: medical_history_data}) + '\n')

    return medical_history_data

add_medical_history()