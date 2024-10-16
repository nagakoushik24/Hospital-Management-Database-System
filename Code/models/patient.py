from database.database import connect_db

def register_patient(name, age, gender, contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO patients (name, age, gender, contact)
                      VALUES (?, ?, ?, ?)''', (name, age, gender, contact))
    conn.commit()
    conn.close()

def get_patient_info(patient_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    return patients

