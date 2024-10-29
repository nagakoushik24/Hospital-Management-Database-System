from database.database import connect_db

def request_ambulance(patient_id, driver_name, contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO ambulance (patient_id, driver_name, contact)
                    VALUES (?, ?, ?)''', (patient_id, driver_name, contact))
    conn.commit()
    conn.close()

def get_ambulance_requests(ambulance_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if ambulance_id != '0':
        cursor.execute('''
            SELECT * FROM ambulance WHERE ambulance_id = ?
        ''', (ambulance_id,))
    else:
        cursor.execute('''
            SELECT * FROM ambulance
        ''')
    
    ambulances = cursor.fetchall()
    conn.close()
    return ambulances
