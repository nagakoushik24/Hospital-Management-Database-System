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
    
    if patient_id != '0':
        cursor.execute('''
            SELECT * FROM patients WHERE id = ?
        ''', (patient_id,)) 
    else:
        cursor.execute('''
            SELECT * FROM patients
        ''')
    
    patients = cursor.fetchall()
    conn.close()
    return patients
