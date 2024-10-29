import sqlite3

def connect_db():
    return sqlite3.connect('database/hospital.db')

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Create Doctors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            contact TEXT
        )
    ''')

    # Create Doctors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        specialization TEXT,
                        available BOOLEAN)''')

    # Create Appointments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER,
                        doctor_id INTEGER,
                        date TEXT,
                        time TEXT,
                        status TEXT DEFAULT 'Scheduled',
                        FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
                        FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id))''')

    # Create Billing table
    cursor.execute('''CREATE TABLE IF NOT EXISTS billing (
                        billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER,
                        total_amount REAL,
                        paid_amount REAL,
                        payment_date TEXT,
                        FOREIGN KEY(patient_id) REFERENCES patients(patient_id))''')

    # Create Rooms table
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        room_number TEXT,
                        patient_id INTEGER,
                        status TEXT,
                        FOREIGN KEY(patient_id) REFERENCES patients(patient_id))''')

    # Create Ambulance Services table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ambulance (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            driver_name TEXT,
            contact TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
    ''')

    # Create Medical Records Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            diagnosis TEXT NOT NULL,
            treatment TEXT,
            prescription TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(patient_id) REFERENCES patients(id)
        )
    ''')

    conn.commit()
    conn.close()

initialize_db()
