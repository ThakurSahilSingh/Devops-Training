class Hospital:
    def __init__(self):
        self.patients = {}

    def add_patient(self, id, name, age, disease):
        self.patients[id] = {"Name": name, "Age": age, "Disease": disease}
        print(f"Patient {name} added!")

    def view_patients(self):
        if not self.patients:
            print("No patients registered!")
        else:
            print("\nPatient Records:")
            for id, details in self.patients.items():
                print(f"ID: {id} - {details}")

    def remove_patient(self, id):
        if id in self.patients:
            del self.patients[id]
            print("Patient removed!")
        else:
            print("Patient not found!")

def main():
    hospital = Hospital()
    while True:
        print("\n1. Add Patient\n2. View Patients\n3. Remove Patient\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            id = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            hospital.add_patient(id, name, age, disease)
        elif choice == "2":
            hospital.view_patients()
        elif choice == "3":
            id = input("Enter Patient ID to remove: ")
            hospital.remove_patient(id)
        elif choice == "4":
            print("Exiting Hospital System.")
            break
        else:
            print("Invalid choice!")

main()
