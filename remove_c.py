import sqlite3

def remove_c_examples():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Delete the C_Examples user
    cursor.execute("DELETE FROM users WHERE name='C_Examples'")
    
    # Delete the code examples associated with C_Examples
    cursor.execute("DELETE FROM codes WHERE receiver='C_Examples'")
    
    conn.commit()
    conn.close()
    print("Successfully removed the C_Examples user and their C code examples from the database.")

if __name__ == '__main__':
    remove_c_examples()
