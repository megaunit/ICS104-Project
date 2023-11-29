from features import AddPatient, UpdateInfo, AddMedicalHistory, DisplayData, DisplayPatientInfo
from our_tools import Rerun, ClearConsole, GetData

def main():
    ClearConsole()
    while True:
        task = input("\n(Add-> AddPatient, Up -> UpdateInfo, AddMed -> AddMedicalHistory, Dis -> DisplayData, DisPa -> DisplayPatientInfo)\nChoose what do you want to do: ")
        task = task.lower()
        if task == "add":
            AddPatient(GetData())
        elif task == "up":
            UpdateInfo(GetData())
        elif task == "addmed":
            AddMedicalHistory(GetData())
        elif task == "dis":
            DisplayData(GetData())
        elif task == "dispa":
            DisplayPatientInfo(GetData())
        else:
            ClearConsole()
            print('Only choose from given choices')
            continue
        if not Rerun():
            break


main()