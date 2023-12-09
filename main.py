from features import AddPatient, UpdateInfo, AddMedicalHistory, DisplayData, DisplayPatientInfo
from our_tools import Rerun, ClearConsole, GetData, newGetData

def main():
    ClearConsole()
    while True:
        task = input("\n1 - Add patient\n2 - Update patient info\n3 - Add medical history\n4 - Display all data\n5 - Display a specific patient's info\nChoose what do you want to do: ")
        task = task.lower()
        if task == "1":
            AddPatient(newGetData())
        elif task == "2":
            UpdateInfo(newGetData())
        elif task == "3":
            AddMedicalHistory(newGetData())
        elif task == "4":
            DisplayData(newGetData())
        elif task == "5":
            DisplayPatientInfo(newGetData())
        else:
            ClearConsole()
            print('Only choose from given choices')
            continue
        if not Rerun():
            break


main()