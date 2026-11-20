import csv
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"
SUMMARY_FILE = "attendance_summary.txt"


def initialize_file():
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "employee_id",
                "employee_name",
                "date",
                "status"
            ])


def validate_employee_id(employee_id):
    if employee_id.strip() == "":
        return False
    return True


def validate_employee_name(employee_name):
    employee_name = employee_name.strip()

    if employee_name == "":
        return False

    if len(employee_name) < 3:
        return False

    for char in employee_name:
        if not (char.isalpha() or char == "." or char == " " or char == "_" or char == "@"):
            return False

    return True

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_status(status):
    status = status.strip().capitalize()

    if status == "Present" or status == "Absent":
        return True

    return False


def record_attendance():
    print("\n========================================")
    print("       RECORD EMPLOYEE ATTENDANCE")
    print("========================================")

    employee_id = input("Enter Employee ID: ").strip().capitalize()

    if not validate_employee_id(employee_id):
        print("Error: Employee ID cannot be empty ")
        return 

    employee_name = input("Enter Employee Name: ").strip()

    if not validate_employee_name(employee_name):
        print("Error: Employee Name cannot be empty \nOR \ncheck the name it should me 3 letters and above also avoid '. , + - @ #'")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    if not validate_date(date):
        print("Error: Invalid date format.")
        print("Please use YYYY-MM-DD.")
        return

    status = input("Enter Status (Present/Absent): ").strip().capitalize()

    if not validate_status(status):
        print("Error: Status must be Present or Absent.")
        return

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            employee_id,
            employee_name,
            date,
            status
        ])

    print("\nAttendance recorded successfully!")


def view_all_records():
    print("\n========================================")
    print("         ATTENDANCE RECORDS")
    print("========================================")

    if not os.path.exists(ATTENDANCE_FILE):
        print("Attendance file not found.")
        return

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No attendance records found.")
        return

    print("-" * 75) 

    print(
        f"{'Employee ID':<15}"
        f"{'Employee Name':<20}"
        f"{'Date':<15}"
        f"{'Status':<15}"
    )

    print("-" * 75)

    for row in rows[1:]:

        if len(row) >= 4:
            print(
                f"{row[0].strip():<15}"
                f"{row[1].strip():<20}"
                f"{row[2].strip():<15}"
                f"{row[3].strip():<15}"
            )

    print("-" * 75)


def search_by_employee_id():
    print("\n========================================")
    print("       SEARCH EMPLOYEE ATTENDANCE")
    print("========================================")

    employee_id = input("Enter Employee ID: ").strip().capitalize()

    if not validate_employee_id(employee_id):
        print("Error: Employee ID cannot be empty.")
        return

    if not os.path.exists(ATTENDANCE_FILE):
        print("Attendance file not found.")
        return

    found = False

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:

        if len(row) >= 4:

            if row[0].strip().lower() == employee_id.lower():

                if not found:

                    print("-" * 75)

                    print(
                        f"{'Employee ID':<15}"
                        f"{'Employee Name':<20}"
                        f"{'Date':<15}"
                        f"{'Status':<15}"
                    )

                    print("-" * 75)

                print(
                    f"{row[0].strip():<15}"
                    f"{row[1].strip():<20}"
                    f"{row[2].strip():<15}"
                    f"{row[3].strip():<15}"
                )

                found = True

    if not found:
        print("No attendance record found for this employee.")

    print("-" * 75)


def generate_summary():
    print("\n========================================")
    print("       GENERATE ATTENDANCE SUMMARY")
    print("========================================")

    if not os.path.exists(ATTENDANCE_FILE):
        print("Attendance file not found.")
        return

    employees = {}

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:

        if len(row) < 4:
            continue

        employee_id = row[0].strip()
        employee_name = row[1].strip()
        status = row[3].strip()

        if employee_id == "":
            continue

        if employee_id not in employees:
            employees[employee_id] = {
                "name": employee_name,
                "present": 0,
                "absent": 0
            }

        if status.lower() == "present":
            employees[employee_id]["present"] += 1

        elif status.lower() == "absent":
            employees[employee_id]["absent"] += 1

    if len(employees) == 0:
        print("No attendance records found.")
        return

    with open(SUMMARY_FILE, "w") as file:

        file.write("========================================\n")
        file.write("       EMPLOYEE ATTENDANCE SUMMARY\n")
        file.write("========================================\n\n")

        for employee_id, data in employees.items():

            total = data["present"] + data["absent"]

            if total > 0:
                percentage = (data["present"] / total) * 100
            else:
                percentage = 0

            file.write(f"Employee ID   : {employee_id}\n")
            file.write(f"Employee Name : {data['name']}\n")
            file.write(f"Present       : {data['present']}\n")
            file.write(f"Absent        : {data['absent']}\n")
            file.write(f"Attendance    : {percentage:.2f}%\n")

            if percentage < 75:
                file.write("Warning       : Attendance below 75%\n")

            file.write("----------------------------------------\n")

    print("\nAttendance summary generated successfully!")
    print(f"Summary saved in {SUMMARY_FILE}")


def view_attendance_history():
    print("\n========================================")
    print("       ATTENDANCE HISTORY")
    print("========================================")

    if not os.path.exists(ATTENDANCE_FILE):
        print("Attendance file not found.")
        return

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No attendance history found.")
        return

    count = 1

    for row in rows[1:]:

        if len(row) >= 4:

            print(f"\nRecord {count}")
            print(f"Employee ID   : {row[0].strip()}")
            print(f"Employee Name : {row[1].strip()}")
            print(f"Date          : {row[2].strip()}")
            print(f"Status        : {row[3].strip()}")

            count += 1

    print("\n========================================")


def view_summary():
    print("\n========================================")
    print("       ATTENDANCE SUMMARY")
    print("========================================")

    if not os.path.exists(SUMMARY_FILE):
        print("Summary file not found.")
        print("Please generate the summary first.")
        return

    with open(SUMMARY_FILE, "r") as file:
        content = file.read()

    print(content)


def main():
    initialize_file()

    while True:

        print("\n========================================")
        print("       EMPLOYEE ATTENDANCE SYSTEM")
        print("========================================")
        print("1. Record Attendance")
        print("2. View All Attendance Records")
        print("3. Search by Employee ID")
        print("4. Generate Attendance Summary")
        print("5. View Attendance History")
        print("6. View Summary")
        print("7. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            record_attendance()

        elif choice == "2":
            view_all_records()

        elif choice == "3":
            search_by_employee_id()

        elif choice == "4":
            generate_summary()

        elif choice == "5":
            view_attendance_history()

        elif choice == "6":
            view_summary()

        elif choice == "7":
            print("\nThank you for using Employee Attendance System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")

main()
