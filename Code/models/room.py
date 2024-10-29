from database.database import connect_db

def assign_room(room_number, patient_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO rooms (room_number, patient_id, status)
                      VALUES (?, ?, ?)''', (room_number, patient_id, status))
    conn.commit()
    conn.close()

def get_rooms(room_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if room_id != '0':
        cursor.execute('''
            SELECT * FROM rooms WHERE room_id = ?
        ''', (room_id,))
    else:
        cursor.execute('''
            SELECT * FROM rooms
        ''')
    
    rooms = cursor.fetchall()
    conn.close()
    return rooms
