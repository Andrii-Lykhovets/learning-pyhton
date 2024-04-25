import mysql.connector
from pprint import pprint

DB_CONFIG = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '',
        'database': 'cash_flow',
    }


def get_all_transaction_records():
    """
    1. DB config must be known (/)
    2. Connect to DB
        import mysql.connector (/)
    3. Initiate cursor
    4. use cursor to execute MySQL queries
    5. Close DB connection !!!  (/)
    """

    query = """
    SELECT id, income, expenditure, date_time, description, company_id
      FROM transaction;
    """

    connection = mysql.connector.connect(**DB_CONFIG)
    
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        pprint(rows)
    
    connection.close()


def insert_new_transaction_record():
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()

    add_transaction = ("INSERT INTO transaction "
                       "(income, expenditure, description, date_time, company_id) "
                       "VALUES (%s, %s, %s, %s, %s)")

    add_transaction_tipped = """INSERT INTO transaction 
                       (income, expenditure, description, date_time, company_id) 
                       VALUES (%s, %s, %s, %s, %s)"""

    data_transaction = (135000, 0, "Дохід від реалізації послуг", "2022-10-01 16:00", 4)

    cursor.execute(add_transaction, data_transaction)

    cnx.commit()

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    get_all_transaction_records()
    # insert_new_transaction_record()
