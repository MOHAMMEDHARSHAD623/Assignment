class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def display_patient(self):
        print("\n---------- Patient Information ----------")
        print("Patient ID :", self.patient_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Contact    :", self.contact)


class Doctor:
    def __init__(self, doctor_id, name, specialization, contact):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact = contact

    def display_doctor(self):
        print("\n---------- Doctor Information ----------")
        print("Doctor ID      :", self.doctor_id)
        print("Name           :", self.name)
        print("Specialization :", self.specialization)
        print("Contact        :", self.contact)


class Appointment:
    def __init__(self, appointment_id, patient, doctor,
                 appointment_date, appointment_time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.status = status

    def display_appointment(self):
        print("\n==========================================")
        print("         APPOINTMENT DETAILS")
        print("==========================================")
        print("Appointment ID :", self.appointment_id)
        print("Date           :", self.appointment_date)
        print("Time           :", self.appointment_time)
        print("Status         :", self.status)

        print("\n----- Patient Details -----")
        self.patient.display_patient()

        print("\n----- Doctor Details -----")
        self.doctor.display_doctor()


patients = []
doctors = []
appointments = []


def add_patient():
    print("\n==========================================")
    print("              ADD PATIENT")
    print("==========================================")


    patient_id = 'P'+ str(len(patients)+1).zfill(3)
    print('Patient Id:',patient_id)

    # while True:
    #     patient_id = input("Enter Patient ID: ")

    #     duplicate_id = False

    #     for patient in patients:
    #         if patient.patient_id == patient_id:
    #             duplicate_id = True
    #             break

    #     if duplicate_id:
    #         print("Patient ID already exists. Please enter another ID.")
    #     else:
    #         break

    while True:
        name = input("Enter Patient Name: ").upper()

        duplicate_name = False

        for patient in patients:
            if patient.name == name:
                duplicate_name = True
                break

        if duplicate_name:
            print("Patient name already exists. Please enter another name.")
            continue

        break

    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    contact = input("Enter Contact Number: ")

    patient = Patient(
        patient_id,
        name,
        age,
        gender,
        contact
    )

    patients.append(patient)

    print("\nPatient added successfully!")


def view_patients():
    print("\n==========================================")
    print("           PATIENT RECORDS")
    print("==========================================")

    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient in patients:
        patient.display_patient()


def add_doctor():
    print("\n==========================================")
    print("              ADD DOCTOR")
    print("==========================================")

    doctor_id = 'D'+ str(len(doctors)+1).zfill(3)

    # while True:
    #     doctor_id = input("Enter Doctor ID: ")

    #     duplicate_id = False

    #     for doctor in doctors:
    #         if doctor.doctor_id == doctor_id:
    #             duplicate_id = True
    #             break

    #     if duplicate_id:
    #         print("Doctor ID already exists. Please enter another ID.")
    #     else:
    #         break

    while True:
        name = input("Enter Doctor Name: ").upper()


        duplicate_name = False

        for doctor in doctors:
            if doctor.name == name:
                duplicate_name = True
                break

        if duplicate_name:
            print("Doctor name already exists. Please enter another name.")
            continue

        break

    specialization = input("Enter Specialization: ")
    contact = input("Enter Contact Number: ")

    doctor = Doctor(
        doctor_id,
        name,
        specialization,
        contact
    )

    doctors.append(doctor)

    print("\nDoctor added successfully!")


def view_doctors():
    print("\n==========================================")
    print("            DOCTOR RECORDS")
    print("==========================================")

    if len(doctors) == 0:
        print("No doctor records found.")
        return

    for doctor in doctors:
        doctor.display_doctor()


def schedule_appointment():
    print("\n==========================================")
    print("         SCHEDULE APPOINTMENT")
    print("==========================================")

    if len(patients) == 0:
        print("No patients available.")
        print("Please add a patient first.")
        return

    if len(doctors) == 0:
        print("No doctors available.")
        print("Please add a doctor first.")
        return

    print("\nAvailable Patients:")

    for patient in patients:
        print(patient.patient_id, "-", patient.name)

    while True:
        patient_id = input("\nEnter Patient ID: ")

        selected_patient = None

        for patient in patients:
            if patient.patient_id == patient_id:
                selected_patient = patient
                break

        if selected_patient is not None:
            break

        print("Patient not found. Please enter a valid Patient ID.")

    print("\nAvailable Doctors:")

    for doctor in doctors:
        print(
            doctor.doctor_id,
            "-",
            doctor.name,
            "-",
            doctor.specialization
        )

    while True:
        doctor_id = input("\nEnter Doctor ID: ")

        selected_doctor = None

        for doctor in doctors:
            if doctor.doctor_id == doctor_id:
                selected_doctor = doctor
                break

        if selected_doctor is not None:
            break

        print("Doctor not found. Please enter a valid Doctor ID.")

    while True:
        appointment_id = 'MCC'+ str(len(appointments)+1).zfill(3)

        print('Appointment Id:',appointment_id)

        duplicate_id = False

        for appointment in appointments:
            if appointment.appointment_id == appointment_id:
                duplicate_id = True
                break

        if duplicate_id:
            print("Appointment ID already exists. Please enter another ID.")
        else:
            break

    appointment_date = input("Enter Appointment Date: ")
    appointment_time = input("Enter Appointment Time: ")

    status = "Scheduled"

    appointment = Appointment(
        appointment_id,
        selected_patient,
        selected_doctor,
        appointment_date,
        appointment_time,
        status
    )

    appointments.append(appointment)

    print("\nAppointment scheduled successfully!")


def view_appointment_details():
    print("\n==========================================")
    print("        APPOINTMENT DETAILS")
    print("==========================================")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    appointment_id = input("Enter Appointment ID: ")

    for appointment in appointments:
        if appointment.appointment_id == appointment_id:
            appointment.display_appointment()
            return

    print("Appointment not found.")


def appointment_summary():
    print("\n==========================================")
    print("         APPOINTMENT SUMMARY")
    print("==========================================")

    if len(appointments) == 0:
        print("No scheduled appointments.")
        return

    print("\nTotal Appointments :", len(appointments))

    print("\n------------------------------------------------------------")
    print("ID\tPatient\t\tDoctor\t\tDate\t\tTime\tStatus")
    print("------------------------------------------------------------")

    for appointment in appointments:
        print(
            appointment.appointment_id,
            "\t",
            appointment.patient.name,
            "\t\t",
            appointment.doctor.name,
            "\t\t",
            appointment.appointment_date,
            "\t",
            appointment.appointment_time,
            "\t",
            appointment.status
        )


while True:
    print("\n\n==========================================")
    print("       MEDICARE CONNECT")
    print("  HOSPITAL APPOINTMENT PLATFORM")
    print("==========================================")

    print("1. Add Patient")
    print("2. View Patient Records")
    print("3. Add Doctor")
    print("4. View Doctor Records")
    print("5. Schedule Appointment")
    print("6. View Appointment Details")
    print("7. Display Appointment Summary")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        add_doctor()

    elif choice == "4":
        view_doctors()

    elif choice == "5":
        schedule_appointment()

    elif choice == "6":
        view_appointment_details()

    elif choice == "7":
        appointment_summary()

    elif choice == "8":
        print("\nThank you for using MediCare Connect.")
        print("Program terminated.")
        break

    else:
        print("\nInvalid choice. Please try again.")