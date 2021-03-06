from django.db import connection
from contextlib import closing


def get_services():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from service""")
        services = dict_fetchall(cursor)
        return services


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories

def get_category_by_id(category_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select product.*,category.name as cat_name from product inner join category on 
        product.category_id= %s""", [category_id])
        categor = dict_fetchone(cursor)
        return categor

def get_teams():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from team""")
        teams = dict_fetchall(cursor)
        return teams
def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name from product inner join category on 
        product.category_id=category.id""")
        products = dict_fetchall(cursor)
        return products

def get_clients():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from client""")
        clients = dict_fetchall(cursor)
        return clients

def get_testimonials():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial""")
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_pricing():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from pricing""")
        pricing = dict_fetchall(cursor)
        return pricing


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
