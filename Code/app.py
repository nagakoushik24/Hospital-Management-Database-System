import streamlit as st
import pandas as pd
from models.patient import register_patient, get_patient_info
from models.doctor import register_doctor, get_doctor_info
from models.appointment import book_appointment, get_appointments
from models.billing import generate_bill, get_bills
from models.room import assign_room, get_rooms
from models.ambulance import request_ambulance, get_ambulance_requests
from models.medical_records import create_medical_record, get_medical_records
from models.manager import remove_doctor
from database.database import initialize_db, connect_db

# Initialize the database when the app starts
initialize_db()

# Sidebar for Navigation
st.sidebar.title('''
            Welcome 
            - Choose your role and action''')

# Streamlit Application Title
st.title("🏥 Hospital Management System")
st.write("----")
role = st.sidebar.selectbox("Select Role", ["Dashboard", "Applicant", "Manager"])

if role == "Dashboard":
    # Description of the Hospital Management System
    st.subheader("About This System")
    st.write("""
    This Hospital Management System (HMS) is designed to streamline hospital operations and enhance patient care. 
    The system allows for the efficient management of patients, doctors, appointments, billing, medical records, 
    room assignments, and ambulance requests. 
    Each entity plays a vital role in ensuring smooth healthcare delivery.
    """)

    # Entity Descriptions
    st.subheader("Entity Descriptions")
    st.write("- **Patient**: Individuals seeking medical care.")
    st.write("- **Doctor**: Medical professionals providing healthcare services.")
    st.write("- **Appointment**: Scheduled meetings between patients and doctors.")
    st.write("- **Billing**: Financial transactions for medical services provided.")
    st.write("- **Medical Records**: Documentation of patient diagnoses and treatments.")
    st.write("- **Room**: Physical spaces assigned to patients for care.")
    st.write("- **Ambulance**: Emergency transport service for patients.")
    st.write("- **Manager**: Authority to manage and oversee hospital staff and operations.")


# Applicant Actions
if role == "Applicant":
    action = st.sidebar.selectbox("Choose Section", 
        ["Register Patient", "Register Doctor", "Book Appointment", "Generate Bill", 
        "Add Medical Records", "Assign Room", "Request Ambulance", "View Database Records"])

    # Patient Registration Form
    if action == "Register Patient":
        st.subheader("👤 Register Patient")
        with st.form("patient_form"):
            name = st.text_input("Patient Name")
            age = st.number_input("Patient Age", min_value=0)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            contact = st.text_input("Contact Number")
            submitted = st.form_submit_button("Register Patient")
            if submitted:
                register_patient(name, age, gender, contact)
                st.success(f"Patient {name} registered successfully!")

    # Doctor Registration Form
    if action == "Register Doctor":
        st.subheader("👨‍⚕️ Register Doctor")
        with st.form("doctor_form"):
            doctor_name = st.text_input("Doctor Name")
            specialization = st.text_input("Specialization")
            available = st.checkbox("Available")
            doc_submitted = st.form_submit_button("Register Doctor")
            if doc_submitted:
                doc_id = register_doctor(doctor_name, specialization, available)
                st.success(f"Doctor {doctor_name} registered successfully with Doctor ID [{doc_id}]!")

    # Book Appointment
    if action == "Book Appointment":
        st.subheader("📅 Book Appointment")
        with st.form("appointment_form"):
            patient_id = st.number_input("Patient ID", min_value=1)
            doctor_id = st.number_input("Doctor ID", min_value=1)
            date = st.date_input("Appointment Date")
            time = st.time_input("Appointment Time")
            appointment_submitted = st.form_submit_button("Book Appointment")
            if appointment_submitted:
                book_appointment(patient_id, doctor_id, date, time)
                st.success(f"Appointment booked for Patient ID {patient_id} with Doctor ID {doctor_id}!")

    # Billing Section
    if action == "Generate Bill":
        st.subheader("💰 Generate Bill")
        with st.form("billing_form"):
            billing_patient_id = st.number_input("Patient ID for Billing", min_value=1)
            total_amount = st.number_input("Total Amount", min_value=0.0)
            paid_amount = st.number_input("Paid Amount", min_value=0.0)
            bill_submitted = st.form_submit_button("Generate Bill")
            if bill_submitted:
                generate_bill(billing_patient_id, total_amount)
                st.success(f"Bill generated for Patient ID {billing_patient_id}!")

    # Medical Records Section
    if action == "Add Medical Records":
        st.subheader("📋 Add Medical Record")
        with st.form("medical_record_form"):
            record_patient_id = st.number_input("Patient ID", min_value=1)
            diagnosis = st.text_input("Diagnosis")
            treatment = st.text_input("Treatment")
            record_date = st.date_input("Record Date")
            medical_record_submitted = st.form_submit_button("Add Medical Record")
            if medical_record_submitted:
                create_medical_record(record_patient_id, diagnosis, treatment, record_date)
                st.success(f"Medical record for Patient ID {record_patient_id} added successfully!")

    # Assign Room
    if action == "Assign Room":
        st.subheader("🏥 Assign Room to Patient")
        with st.form("room_form"):
            room_number = st.text_input("Room Number")
            patient_room_id = st.number_input("Patient ID for Room Assignment", min_value=1)
            room_status = st.selectbox("Room Status", ["Occupied", "Available"])
            room_submitted = st.form_submit_button("Assign Room")
            if room_submitted:
                assign_room(room_number, patient_room_id, room_status)
                st.success(f"Room {room_number} assigned to Patient ID {patient_room_id}.")

    # Request Ambulance
    if action == "Request Ambulance":
        st.subheader("🚑 Request Ambulance")
        with st.form("ambulance_form"):
            ambulance_patient_id = st.number_input("Patient ID for Ambulance", min_value=1)
            driver_name = st.text_input("Driver Name")
            contact_ambulance = st.text_input("Driver Contact")
            ambulance_submitted = st.form_submit_button("Request Ambulance")
            if ambulance_submitted:
                request_ambulance(ambulance_patient_id, driver_name, contact_ambulance)
                st.success(f"Ambulance requested for Patient ID {ambulance_patient_id}.")

    # View Database Records Section
    if action == "View Database Records":
        st.subheader("📊 View Database Records")

        # Display Patients Table
        if st.button("View all Patients"):
            patients = get_patient_info()
            if patients:
                patients_df = pd.DataFrame(patients, columns=["Patient ID", "Name", "Age", "Gender", "Contact"])
                st.dataframe(patients_df)
            else:
                st.write("No patients found.")

        # Display Doctors Table
        if st.button("View all Doctors"):
            doctors = get_doctor_info()
            if doctors:
                doctors_df = pd.DataFrame(doctors, columns=["Doctor ID", "Name", "Specialization", "Available"])
                st.dataframe(doctors_df)
            else:
                st.write("No doctors found.")

        # Display Appointments Table
        if st.button("View all Appointments"):
            appointments = get_appointments()
            if appointments:
                appointments_df = pd.DataFrame(appointments, columns=["Appointment ID", "Patient ID", "Doctor ID", "Date", "Time", "Status"])
                st.dataframe(appointments_df)
            else:
                st.write("No appointments found.")

        # Display Medical Records Table
        if st.button("View all Medical Records"):
            records = get_medical_records()
            if records:
                medical_records_df = pd.DataFrame(records, columns=["Record ID", "Patient ID", "Doctor ID", "Diagnosis", "Treatment", "Date"])
                st.dataframe(medical_records_df)
            else:
                st.write("No medical records found.")

        # Display Billing Table
        if st.button("View all Billing"):
            bills = get_bills()
            if bills:
                bills_df = pd.DataFrame(bills, columns=["Bill ID", "Patient ID", "Total Amount", "Paid Amount", "Date"])
                st.dataframe(bills_df)
            else:
                st.write("No bills found.")

        # Display Rooms Table
        if st.button("View all Rooms"):
            rooms = get_rooms()
            if rooms:
                rooms_df = pd.DataFrame(rooms, columns=["Room ID", "Room Number", "Patient ID", "Status"])
                st.dataframe(rooms_df)
            else:
                st.write("No rooms assigned.")

        # Display Ambulance Requests Table
        if st.button("View all Ambulance Requests"):
            ambulance_requests = get_ambulance_requests()
            if ambulance_requests:
                ambulance_df = pd.DataFrame(ambulance_requests, columns=["Request ID", "Patient ID", "Driver Name", "Contact"])
                st.dataframe(ambulance_df)
            else:
                st.write("No ambulance requests found.")

# Manager Actions
elif role == "Manager":
    action = st.sidebar.selectbox("Choose Manager Action", ["Remove Doctor", "View Records"])

    # Remove Doctor Action
    if action == "Remove Doctor":
        st.subheader("🩺 Remove Doctor")
        with st.form("remove_doctor_form"):
            doctor_id = st.number_input("Doctor ID", min_value=1)
            remove_submitted = st.form_submit_button("Remove Doctor")
            if remove_submitted:
                out = remove_doctor(doctor_id)
                if out:
                    st.success(f"Doctor with ID {doctor_id} has been removed successfully!")
                else:
                    st.error(f"Doctor with ID {doctor_id} not found!")
        if st.button("Current Doctors list"):
            doctors = get_doctor_info()
            if doctors:
                doctors_df = pd.DataFrame(doctors, columns=["Doctor ID", "Name", "Specialization", "Available"])
                st.dataframe(doctors_df)
            else:
                st.write("No doctors found.")

    # View Manager Records
    if action == "View Records":
        st.subheader("📊 View All Records")

        # Display Patients Table
        if st.button("View all Patients"):
            patients = get_patient_info()
            if patients:
                patients_df = pd.DataFrame(patients, columns=["Patient ID", "Name", "Age", "Gender", "Contact"])
                st.dataframe(patients_df)
            else:
                st.write("No patients found.")

        # Display Doctors Table
        if st.button("View all Doctors"):
            doctors = get_doctor_info()
            if doctors:
                doctors_df = pd.DataFrame(doctors, columns=["Doctor ID", "Name", "Specialization", "Available"])
                st.dataframe(doctors_df)
            else:
                st.write("No doctors found.")

        # Display Appointments Table
        if st.button("View all Appointments"):
            appointments = get_appointments()
            if appointments:
                appointments_df = pd.DataFrame(appointments, columns=["Appointment ID", "Patient ID", "Doctor ID", "Date", "Time", "Status"])
                st.dataframe(appointments_df)
            else:
                st.write("No appointments found.")

        # Display Medical Records Table
        if st.button("View all Medical Records"):
            records = get_medical_records()
            if records:
                medical_records_df = pd.DataFrame(records, columns=["Record ID", "Patient ID", "Doctor ID", "Diagnosis", "Treatment", "Date"])
                st.dataframe(medical_records_df)
            else:
                st.write("No medical records found.")

        # Display Billing Table
        if st.button("View all Billing"):
            bills = get_bills()
            if bills:
                bills_df = pd.DataFrame(bills, columns=["Bill ID", "Patient ID", "Total Amount", "Paid Amount", "Date"])
                st.dataframe(bills_df)
            else:
                st.write("No bills found.")

        # Display Rooms Table
        if st.button("View all Rooms"):
            rooms = get_rooms()
            if rooms:
                rooms_df = pd.DataFrame(rooms, columns=["Room ID", "Room Number", "Patient ID", "Status"])
                st.dataframe(rooms_df)
            else:
                st.write("No rooms assigned.")

        # Display Ambulance Requests Table
        if st.button("View all Ambulance Requests"):
            ambulance_requests = get_ambulance_requests()
            if ambulance_requests:
                ambulance_df = pd.DataFrame(ambulance_requests, columns=["Request ID", "Patient ID", "Driver Name", "Contact"])
                st.dataframe(ambulance_df)
            else:
                st.write("No ambulance requests found.")


# Footer with Creator Information
st.sidebar.write("---")
st.sidebar.write("Created by: Naga Koushik")
st.sidebar.write("Roll Number: CB.EN.U4AIE22046")
