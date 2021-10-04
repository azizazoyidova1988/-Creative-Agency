from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories


def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(id) from category""")
        categories_count = dict_fetchall(cursor)
        return categories_count


def get_categories_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(product.id),category.name ,product.category_id
        FROM category LEFT JOIN product
		ON product.category_id=category.id
		GROUP BY product.category_id, category.name
        """)
        categories = dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product""")
        products = dict_fetchall(cursor)
        return products


def get_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from product""")
        products_count = dict_fetchall(cursor)
        return products_count


def get_teams():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from team""")
        team = dict_fetchall(cursor)
        return team


def get_teams_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from team""")
        teams_count = dict_fetchall(cursor)
        return teams_count


def get_service():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from service""")
        services = dict_fetchall(cursor)
        return services

def get_services_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from service""")
        services_count = dict_fetchall(cursor)
        return services_count

def get_pricing():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from pricing""")
        pricing = dict_fetchall(cursor)
        return pricing


def get_testimonial():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial""")
        testimonial = dict_fetchall(cursor)
        return testimonial





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
