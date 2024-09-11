import mysql.connector as connector


def check_appointment(booking_id):
    try:
        db = connector.connect(
            host="localhost",
            user="root",
            password="Abhi17@db",
            database="project_gluco"
        )

        my_cursor = db.cursor()

        
        q = "SELECT * FROM appointments WHERE booking_id=%s"
       
        v = (booking_id,)

        # Execute the query
        res=my_cursor.execute(q, v)
        data=my_cursor.fetchone()
        # Commit the transaction
        db.commit()
        
        # Success message
        res = f"Your appointment was booked successfully.\n Your Booking Details Are : \n{data}"
        return res
    
    except connector.Error as e:
        return f"An error occurred: {str(e)}"
    
    finally:
        # Close the database connection
        if db.is_connected():
            my_cursor.close()
            db.close()

#print(check_appointment("7936"))