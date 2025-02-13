class GradeSystem:
    def __init__(self):
        self.grades = {}

    def add_grade(self, name, grade):
        self.grades[name] = grade
        print(f"Added: {name} - {grade}")

    def view_grades(self):
        if not self.grades:
            print("No grades available!")
        else:
            print("\nStudent Grades:")
            for name, grade in self.grades.items():
                print(f"{name}: {grade}")

    def calculate_average(self):
        if not self.grades:
            print("No grades available!")
        else:
            avg = sum(self.grades.values()) / len(self.grades)
            print(f"Class Average: {avg:.2f}")

def main():
    system = GradeSystem()

    while True:
        print("\n1. Add Grade\n2. View Grades\n3. Calculate Average\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            system.add_grade(name, grade)
        elif choice == "2":
            system.view_grades()
        elif choice == "3":
            system.calculate_average()
        elif choice == "4":
            print("Exiting Grade System.")
            break
        else:
            print("Invalid choice!")

main()
