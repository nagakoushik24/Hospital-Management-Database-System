from database.database import connect_db

def request_ambulance(patient_id, driver_name, contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO ambulance (patient_id, driver_name, contact)
                    VALUES (?, ?, ?)''', (patient_id, driver_name, contact))
    conn.commit()
    conn.close()

def get_ambulance_requests():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ambulance')
    ambulance_requests = cursor.fetchall()
    conn.close()
    return ambulance_requests  # Returns all ambulance requests as a list of tuples