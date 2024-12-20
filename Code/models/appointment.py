from database.database import connect_db

def book_appointment(patient_id, doctor_id, date, time):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Convert the datetime.time object to a string in 'HH:MM' format
    time_str = time.strftime('%H:%M')
    
    cursor.execute('''
        INSERT INTO appointments (patient_id, doctor_id, date, time)
        VALUES (?, ?, ?, ?)
    ''', (patient_id, doctor_id, date, time_str))
    
    conn.commit()
    conn.close()
    
def get_appointments(appointment_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if appointment_id != '0':
        cursor.execute('''
            SELECT * FROM appointments WHERE appointment_id = ?
        ''', (appointment_id,))
    else:
        cursor.execute('''
            SELECT * FROM appointments
        ''')
    
    appointments = cursor.fetchall()
    conn.close()
    return appointments
