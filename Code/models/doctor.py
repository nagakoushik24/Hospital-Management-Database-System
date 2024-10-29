from database.database import connect_db

def register_doctor(name, specialization, available):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO doctors (name, specialization, available)
                    VALUES (?, ?, ?)''', (name, specialization, available))
    conn.commit()
    conn.close()
    doctor_id = cursor.lastrowid
    return doctor_id

def get_doctor_info(doctor_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if doctor_id != '0':
        cursor.execute('''
            SELECT * FROM doctors WHERE doctor_id = ?
        ''', (doctor_id,))
    else:
        cursor.execute('''
            SELECT * FROM doctors
        ''')
    
    doctors = cursor.fetchall()
    conn.close()
    return doctors
