import raw_data
from models import User, Offer, Order
from config import db, app


def insert_user(input_data):
    """
    Функция добавляет пользователя в таблицу user
    :param input_data: Данные пользователя
    :return: -
    """

    for row in input_data:
        db.session.add(
            User(
                id=row.get('id'),
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                age=row.get('age'),
                email=row.get('email'),
                role=row.get('role'),
                phone=row.get('phone'),
            ))
        db.session.commit()


def insert_offer(input_data):
    """
    Функция добавляет предложение в таблицу offer
    :param input_data: Данные предложения
    :return: -
    """
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get('id'),
                order_id=row.get('order_id'),
                executor_id=row.get('executor_id')
            ))
        db.session.commit()


def insert_order(input_data):
    """
    Функция добавляет заказ в таблицу order
    :param input_data: Данные заказа
    :return: -
    """
    for row in input_data:
        db.session.add(
            Order(
                id=row.get('id'),
                name=row.get('name'),
                description=row.get('description'),
                start_date=row.get('start_date'),
                end_date=row.get('end_date'),
                adress=row.get('adress'),
                price=row.get('price'),
                customer_id=row.get('customer_id'),
                executor_id=row.get('executor_id'),
            ))
        db.session.commit()


def init_db():
    """
    функция заполняет данными таблицы user, offer, order
    :return:
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_user(raw_data.users)
        insert_order(raw_data.orders)
        insert_offer(raw_data.offers)
