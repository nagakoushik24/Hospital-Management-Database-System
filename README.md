# Hospital Management System

This project is a Python-based Hospital Management System with a Streamlit-powered frontend. It allows users to manage hospital operations such as patient registration, doctor management, appointment booking, billing, room assignments, and more. The system supports role-based operations for applicants and managers.

## ER-Diagram of this Database

![ER-Diagram](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/ER-Diagram.png)

## Project Structure

```

HospitalManagementSystem/
│
├── database/
│   ├── database.py          # Database initialization and connection
│
├── models/
│   ├── patient.py           # Functions related to patient operations
│   ├── doctor.py            # Functions related to doctor operations
│   ├── appointment.py       # Functions for booking and managing appointments
│   ├── billing.py           # Functions for generating and retrieving bills
│   ├── room.py              # Functions related to room assignments
│   ├── ambulance.py         # Functions related to ambulance requests
│   ├── medical_records.py   # Functions for handling medical records
│   ├── manager.py           # Functions for managerial operations (e.g., remove doctor)
│
├── main.py                  # Main Streamlit application code
└── README.md                # Description and instructions for the project
```


## Features

- **Patient Management:** Register new patients, view their medical records, and handle ambulance requests.
- **Doctor Management:** Add new doctors and allow managers to remove doctors from the system.
- **Appointment Booking:** Book and manage appointments for patients.
- **Billing:** Generate and view billing details for patients.
- **Room Assignment:** Assign and manage rooms for patients.
- **Medical Records:** Store and retrieve patient medical records.
- **Ambulance Requests:** Handle and track ambulance requests for patients.
- **Role-Based Operations:** 
  - Applicants (patients/administrators) can register patients, book appointments, view records, and generate bills.
  - Managers can oversee operations and remove doctors from the system.

## Prerequisites

- Python 3.8 or higher
- Streamlit
- SQLite (for the database)

## Installation


**Install the required Python packages:**

```
pip install -r requirements.txt
```

**Run the application using Streamlit:**

```
streamlit run Code/app.py
```

### Usage

- Choose Your Role: Select either the Applicant or Manager role from the sidebar.
    - Applicant: Register patients, book appointments, and generate bills.
    - Manager: Manage hospital operations, including removing doctors.

- Navigate the Application: Use the sidebar to perform actions like registering patients, managing appointments, assigning rooms, or viewing medical records.

- Data Display: The system displays relevant data, such as patient details, appointments, bills, and medical records, in an easy-to-read format.

### Database Setup

- The system uses SQLite as the database. Upon running the application for the first time, the necessary tables will be initialized automatically by the database.py script.

---
## Screenshots of Front-end

![Image 1](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/img5.png)

![Image 2](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/img4.png)

![Image 3](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/img3.png)

![Image 4](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/img2.png)

![Image 5](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/img6.png)

![Image 6](https://github.com/nagakoushik24/Hospital-Management-Database-System/blob/main/Images/img1.png)



