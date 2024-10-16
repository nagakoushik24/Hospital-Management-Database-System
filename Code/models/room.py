from database.database import connect_db

def assign_room(room_number, patient_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO rooms (room_number, patient_id, status)
                      VALUES (?, ?, ?)''', (room_number, patient_id, status))
    conn.commit()
    conn.close()

def get_rooms():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM rooms')

    rooms = cursor.fetchall()
    conn.close()
    return rooms  # Returns all rooms as a list of tuples
