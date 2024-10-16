from database.database import connect_db

# Function to create a medical record for a patient
def create_medical_record(patient_id, diagnosis, treatment, prescription):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Insert the medical record into the database
    cursor.execute('''
        INSERT INTO medical_records (patient_id, diagnosis, treatment, prescription)
        VALUES (?, ?, ?, ?)
    ''', (patient_id, diagnosis, treatment, prescription))
    
    conn.commit()
    conn.close()

# Function to retrieve all medical records for a given patient
def get_medical_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medical_records')
    medical_records = cursor.fetchall()
    conn.close()
    return medical_records  # Returns all medical records as a list of tuples

