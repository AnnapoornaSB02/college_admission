applications = {}

def apply_admission(app_id, name, department, marks):
    if app_id in applications:
        return "Application already exists"

    status = "Approved" if marks >= 60 else "Rejected"
    applications[app_id] = {
        "name": name,
        "department": department,
        "marks": marks,
        "status": status
    }
    return "Application submitted successfully"

def view_application(app_id):
    if app_id not in applications:
        return "Application not found"
    return applications[app_id]

def main():
    while True:
        print("\n1. Apply for Admission")
        print("2. View Application Status")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            app_id = input("Enter Application ID: ")
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            marks = float(input("Enter Marks: "))

            print(apply_admission(app_id, name, department, marks))

        elif choice == "2":
            app_id = input("Enter Application ID: ")
            result = view_application(app_id)
            print(result)

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
