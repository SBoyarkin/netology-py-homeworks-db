import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config.conf')


def create_database(conn):
    with conn.cursor() as cur:
        cur.execute(
            ''' CREATE TABLE IF NOT EXISTS client (
                    id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
             last_name VARCHAR(100) NOT NULL,
                 email VARCHAR(50) NOT NULL UNIQUE);
                                      
                CREATE TABLE IF NOT EXISTS phone_client(
                    id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES client(id)
                   ON DELETE CASCADE,
                phone VARCHAR(11) NOT NULL UNIQUE);
            ''')
        conn.commit()

def add_phone(conn, id, phone_number):
    data = (id[0], phone_number)
    with conn.cursor() as cur:
        cur.execute(
            '''
            INSERT INTO phone_client (client_id, phone)
            VALUES (%s,%s) RETURNING id;
            ''', data)


def add_client(conn, first_name, last_name, email, phone=None):
    data = (first_name, last_name, email)
    with conn.cursor() as cur:
        cur.execute(
            '''
            INSERT INTO client(first_name, last_name, email)
            VALUES (%s,%s,%s) RETURNING id;
            ''', data)
        id = cur.fetchone()
        conn.commit()
        if phone:
            add_phone(conn=conn, id=id, phone_number=phone)
            conn.commit()
    return print(id[0])


def add_phone_exist_client(conn, email, phone):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT *
              FROM client
             WHERE email LIKE %s; 
            """, (email,))
        id = cur.fetchone()
        add_phone(conn=conn, id=id, phone_number=phone)
        print(id)


def add_test_data(conn):
    with conn.cursor() as cur:
        cur.execute(
            '''
            INSERT INTO client(first_name, last_name, email)
            VALUES ('Иван', 'Иванов','invanov@mail.ru'),
                   ('Петр', 'Петров','petrov@mail.ru'),
                   ('Сергей', 'Сергеев','sergeev@mail.ru'),
                   ('Михайл', 'Михайлов','mikhailov@mail.ru'),
                   ('Сидор', 'Сидоров','sidorov@mail.ru');
            
            INSERT INTO phone_client (client_id, phone)
            VALUES ('1','89220000000'),
                   ('1','89220000001'),
                   ('2','89220000002'),
                   ('3','89220000003'),
                   ('4','89220000004');
            ''',)
        conn.commit()


def search_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        request = """
                SELECT first_name, last_name, email, phone_client.phone
                  FROM client
                  JOIN phone_client
                    ON client.id = phone_client.client_id
                 WHERE"""
        params = []
        if first_name:
            request += " first_name = %s"
            params.append(first_name)
        if last_name:
            if len(params) > 0:
                request += " AND last_name = %s"
            else:
                request += " last_name = %s"
            params.append(last_name)
        if email:
            if len(params) > 0:
                request += " AND email = %s"
            else:
                request += " email = %s"
            params.append(email)
        if phone:
            if len(params) > 0:
                request += " AND phone = %s"
            else:
                request += " phone = %s"
            params.append(phone)
        cur.execute(request, params)
        id = cur.fetchall()
        print(id)




def delete_phone(conn, phone):
    with conn.cursor() as cur:
        cur.execute(
            '''
            DELETE FROM phone_client
             WHERE phone = %s
             ''', (phone,))


def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute(
            '''
            DELETE FROM client
            WHERE id = %s
            ''', str(client_id))



def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute(
            '''
            SELECT phone_client.id, phone_client.phone
              FROM client
              LEFT JOIN phone_client
                ON client.id = phone_client.client_id
             WHERE client.id = %s
            '''
            , client_id)
        length = cur.fetchall()
        if len(length) > 1:
            print('Введите индекс номера, который нужно заменить')
            for index, phone_num in length:
                print(index, phone_num)
            i = input('Индекс: ')
            params = []
            params.append(phone)
            params.append(i)
            cur.execute(
                '''
                UPDATE phone_client
                   SET phone = %s
                 WHERE id = %s;
                ''', params)
            print(params)
        else:
            params = []
            params.append(phone)
            params.append(client_id)
            cur.execute(
                '''
                UPDATE phone_client
                   SET phone = %s
                 WHERE id = %s;
                ''', params)
        params = []
        request = '''
            UPDATE client
               SET'''
        if first_name:
            request += " first_name = %s"
            params.append(first_name)
        if last_name:
            if len(params) > 0:
                request += ", last_name = %s"
            else:
                request += " last_name = %s"
            params.append(last_name)
        if email:
            if len(params) > 0:
                request += ", email = %s"
            else:
                request += " email = %s"
            params.append(email)
        if params:
            request += '\n WHERE id = %s'
            params.append(client_id)
            cur.execute(request, params)



with psycopg2.connect(database=config['AUTH']['database'],
                      user=config['AUTH']['username'],
                      password=config['AUTH']['password']) as conn:
    
    # Создание и наполнение БД
    create_database(conn)
    add_test_data(conn)

    # Добавление клиента сномером телефона и без
    add_client(conn=conn, first_name='Магомед', last_name='Магомедов', email='magomedov@mail.ru')
    add_client(conn=conn, first_name='Ильяс', last_name='Ильясов', email='ilyasov@mail.ru', phone='89111111111')

    # Добавление существующему клиенту, номера телефона
    add_phone_exist_client(conn=conn, email='magomedov@mail.ru', phone='89222222222')



    #Изменение данных о клиентею
    change_client(conn=conn, client_id='5',first_name='Олег', phone='0')

    # Удаление клиента
    delete_client(conn, 1)

    #Удаление номера у клиента
    delete_phone(conn, phone='123')

    #Поиск клиента по ФИО и номеру тел.
    search_client(conn=conn, first_name='Ильяс', phone='89111111111')