# manager.py
import sqlite3
from database.database import connect_db

def remove_doctor(doctor_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Check if doctor exists before trying to delete
        cursor.execute("SELECT * FROM doctors WHERE doctor_id = ?", (doctor_id,))
        doctor = cursor.fetchone()
        
        if doctor:
            cursor.execute("DELETE FROM doctors WHERE doctor_id = ?", (doctor_id,))
            conn.commit()
            return 1
        else:
            return 0
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        conn.close()
