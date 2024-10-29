from database.database import connect_db

def generate_bill(patient_id, total_amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO billing (patient_id, total_amount, paid_amount, payment_date)
                      VALUES (?, ?, ?, CURRENT_TIMESTAMP)''', (patient_id, total_amount, total_amount))
    conn.commit()
    conn.close()
    
def get_bills(bill_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if bill_id != '0':
        cursor.execute('''
            SELECT * FROM billing WHERE bill_id = ?
        ''', (bill_id,))
    else:
        cursor.execute('''
            SELECT * FROM billing
        ''')
    
    bills = cursor.fetchall()
    conn.close()
    return bills
