import mysql.connector
from patient import Patient
from doctor import Doctor
from appointment import Appointment

def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rachana@2106",
        database="hospital"
    )

def main_menu():
    print("\nWelcome to the Health Management System")
    print("1. Manage Patients")
    print("2. Manage Doctors")
    print("3. Manage Appointments")
    print("4. Display Tables")
    print("5. Exit")

def patient_menu():
    print("\nPatient Management")
    print("1. Add Patient")
    print("2. Update Patient")
    print("3. Delete Patient")
    print("4. Back to Main Menu")

def doctor_menu():
    print("\nDoctor Management")
    print("1. Add Doctor")
    print("2. Update Doctor")
    print("3. Delete Doctor")
    print("4. Back to Main Menu")

def appointment_menu():
    print("\nAppointment Management")
    print("1. Schedule Appointment")
    print("2. Update Appointment")
    print("3. Cancel Appointment")
    print("4. Back to Main Menu")

def display_menu():
    print("\nDisplay Tables")
    print("1. Display Patients")
    print("2. Display Doctors")
    print("3. Display Appointments")
    print("4. Back to Main Menu")

def display_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    db_connection = create_db_connection()
    cursor = db_connection.cursor()
    patient_manager = Patient(db_connection)
    doctor_manager = Doctor(db_connection)
    appointment_manager = Appointment(db_connection)

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                patient_menu()
                patient_choice = input("Enter your choice: ")

                if patient_choice == "1":
                    patient_id = int(input("Enter patient ID: "))
                    name = input("Enter name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    gender = input("Enter gender: ")
                    contact_info = input("Enter contact info: ")
                    patient_manager.add_patient(patient_id, name, date_of_birth, gender, contact_info)
                    print("Patient added successfully!")

                elif patient_choice == "2":
                    patient_id = int(input("Enter patient ID: "))
                    name = input("Enter name (leave blank if no change): ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD, leave blank if no change): ")
                    gender = input("Enter gender (leave blank if no change): ")
                    contact_info = input("Enter contact info (leave blank if no change): ")
                    patient_manager.update_patient(patient_id, name or None, date_of_birth or None, gender or None, contact_info or None)
                    print("Patient updated successfully!")

                elif patient_choice == "3":
                    patient_id = int(input("Enter patient ID: "))
                    patient_manager.delete_patient(patient_id)
                    print("Patient deleted successfully!")

                elif patient_choice == "4":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                doctor_menu()
                doctor_choice = input("Enter your choice: ")

                if doctor_choice == "1":
                    doctor_id = int(input("Enter doctor ID: "))
                    name = input("Enter name: ")
                    specialty = input("Enter specialty: ")
                    contact_info = input("Enter contact info: ")
                    available_dates = input("Enter available dates (comma-separated): ")
                    doctor_manager.add_doctor(doctor_id, name, specialty, contact_info, available_dates)
                    print("Doctor added successfully!")

                elif doctor_choice == "2":
                    doctor_id = int(input("Enter doctor ID: "))
                    name = input("Enter name (leave blank if no change): ")
                    specialty = input("Enter specialty (leave blank if no change): ")
                    contact_info = input("Enter contact info (leave blank if no change): ")
                    available_dates = input("Enter available dates (comma-separated, leave blank if no change): ")
                    doctor_manager.update_doctor(doctor_id, name or None, specialty or None, contact_info or None, available_dates or None)
                    print("Doctor updated successfully!")

                elif doctor_choice == "3":
                    doctor_id = int(input("Enter doctor ID: "))
                    doctor_manager.delete_doctor(doctor_id)
                    print("Doctor deleted successfully!")

                elif doctor_choice == "4":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                appointment_menu()
                appointment_choice = input("Enter your choice: ")

                if appointment_choice == "1":
                    appointment_id = int(input("Enter appointment ID: "))
                    patient_id = int(input("Enter patient ID: "))
                    doctor_id = int(input("Enter doctor ID: "))
                    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                    reason = input("Enter reason: ")
                    appointment_manager.schedule_appointment(appointment_id, patient_id, doctor_id, appointment_date, reason)
                    print("Appointment scheduled successfully!")

                elif appointment_choice == "2":
                    appointment_id = int(input("Enter appointment ID: "))
                    patient_id = input("Enter patient ID (leave blank if no change): ")
                    doctor_id = input("Enter doctor ID (leave blank if no change): ")
                    appointment_date = input("Enter appointment date (YYYY-MM-DD, leave blank if no change): ")
                    reason = input("Enter reason (leave blank if no change): ")
                    appointment_manager.update_appointment(appointment_id, int(patient_id) if patient_id else None, int(doctor_id) if doctor_id else None, appointment_date or None, reason or None)
                    print("Appointment updated successfully!")

                elif appointment_choice == "3":
                    appointment_id = int(input("Enter appointment ID: "))
                    appointment_manager.cancel_appointment(appointment_id)
                    print("Appointment canceled successfully!")

                elif appointment_choice == "4":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                display_menu()
                display_choice = input("Enter your choice: ")

                if display_choice == "1":
                    print("\nPatients Table:")
                    display_table(cursor, "Patients")

                elif display_choice == "2":
                    print("\nDoctors Table:")
                    display_table(cursor, "Doctors")

                elif display_choice == "3":
                    print("\nAppointments Table:")
                    display_table(cursor, "Appointments")

                elif display_choice == "4":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

    db_connection.close()

if __name__ == "__main__":
    main()
