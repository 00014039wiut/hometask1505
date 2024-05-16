import psycopg2


db_name = "company"
password = "Sql7575"
user = 'postgres'
port = 5432
host = 'localhost'

conn = psycopg2.connect(database=db_name, password=password, user=user, port=port, host=host)
cur = conn.cursor()


def create_table():
    create_table_query = """create table Products(
    ID serial primary key,
    name varchar(50),
    image varchar(255),
    is_liked boolean,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp
    )"""
    cur.execute(create_table_query)
    conn.commit()


# create_table()

def insert_data():
    name = input('Name : ')
    image = input('Image : ')
    is_liked = input("True/False: ")
    insert_data_query = "insert into products(name,image, is_liked) values(%s,%s, %s);"
    insert_data_params = (name, image, is_liked)
    cur.execute(insert_data_query, insert_data_params)
    conn.commit()


# insert_data()

def show_all():
    select_all_query = """select * from products"""
    cur.execute(select_all_query)
    all_data = cur.fetchall()
    for data in all_data:
        print(data)


# show_all()

def fetch_one():
    Id = int(input("The ID : "))
    select_one_query = """select * from products where id = %s;"""
    cur.execute(select_one_query, (Id,))
    fetched = cur.fetchone()
    conn.commit()
    print(fetched)


# fetch_one()

def update_one():
    update_data_query = """update products set name = %s,image = %s where id = in %s"""
    name = input('Enter name : ')
    image = input('Enter Image : ')
    Id = int(input('ID : '))
    cur.execute(update_data_query, (name, image, Id))
    conn.commit()


# update_one()

def delete_data():
    Id = int(input('ID : '))
    delete_data_query = 'delete from products where id = %s;'
    cur.execute(delete_data_query, (Id,))
    conn.commit()


# delete_data()

def menu():
    print("1 => create data")
    print("2 => show all data")
    print("3 => show one data")
    print("4 => update data")
    print("5 => delete data")
    choice = int(input("Choose:  "))
    if choice == 1:
        insert_data()
    elif choice == 2:
        show_all()
    elif choice == 3:
        fetch_one()
    elif choice == 4:
        update_one()
    elif choice == 5:
        delete_data()
    else:
        print("choose a proper option")


while True:
    menu()


