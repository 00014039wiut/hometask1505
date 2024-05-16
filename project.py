import psycopg2

db_name = "company"
password = "Sql7575"
user = 'postgres'
port = 5432
host = 'localhost'

conn = psycopg2.connect(database=db_name, password=password, user=user, port=port, host=host)
cur = conn.cursor()


def insert_data():
    name = input('Name : ')
    image = input('Image : ')
    is_liked = input("True/False: ")
    insert_data_query = "insert into products(name,image, is_liked) values(%s,%s, %s);"
    insert_data_params = (name, image, is_liked)
    cur.execute(insert_data_query, insert_data_params)
    conn.commit()


class Product:

    def __init__(self,
                 name: str,
                 image: str,
                 is_liked: bool
                 ):
        self.name = name
        self.image = image
        self.is_liked = is_liked

    def save(self):
        insert_data_query = "insert into products(name,image, is_liked) values(%s,%s, %s);"
        insert_data_params = (self.name, self.image, self.is_liked)
        cur.execute(insert_data_query, insert_data_params)
        conn.commit()


def create_product():
    name = input("Name => ")
    image = input("Image => ")
    is_liked = bool(input("0 or 1"))
    product1 = Product(name=name, image=image, is_liked=is_liked)
    product1.save()
create_product()
