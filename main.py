from features import AddPatient, UpdateInfo, AddMedicalHistory, DisplayData, DisplayPatientInfo
from our_tools import Rerun, ClearConsole, GetData

def main():
    ClearConsole()
    while True:
        task = input("\n1 - Add patient\n2 - Update patient info\n3 - Add medical history\n4 - Display all data\n5 - Display a specific patient's info\nChoose what do you want to do: ")
        task = task.lower()
        if task == "1":
            AddPatient(GetData())
        elif task == "2":
            UpdateInfo(GetData())
        elif task == "3":
            AddMedicalHistory(GetData())
        elif task == "4":
            DisplayData(GetData())
        elif task == "5":
            DisplayPatientInfo(GetData())
        else:
            ClearConsole()
            print('Only choose from given choices')
            continue
        if not Rerun():
            break


main()