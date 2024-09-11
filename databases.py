import mysql.connector as connector
import random

def book_appointment(name, email, phn, date, time, dr, desc):
    try:
        db = connector.connect(
            host="localhost",
            user="root",
            password="Abhi17@db",
            database="project_gluco"
        )

        my_cursor = db.cursor()

        # Generate a random booking ID
        booking_id = random.randint(1000, 9999)

        # SQL query to insert appointment details including booking_id
        q = """
        INSERT INTO appointments(booking_id, name, email, phone, date, time, doctor, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        v = (booking_id, name, email, phn, date, time, dr, desc)

        # Execute the query
        my_cursor.execute(q, v)

        # Commit the transaction
        db.commit()

        # Success message
        res = f"Your appointment was booked successfully.\nYour Booking ID is {booking_id}.Save for Future Refrences.."
        return res
    
    except connector.Error as e:
        return f"An error occurred: {str(e)}"
    
    finally:
        # Close the database connection
        if db.is_connected():
            my_cursor.close()
            db.close()

# Sample checkup
#x = book_appointment("Abhishek", "ashek@gmail.com", "7204489644", "2024-09-10", "09:23", "Dr. John", "Just for a checkup")
#print(x)
