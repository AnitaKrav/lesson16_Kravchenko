import json

from flask import jsonify, request, abort

from models import User, Offer, Order
from config import db, app
from utils import init_db


# -Users-
@app.route('/users', methods=["GET", "POST"])
def all_users():
    """
    Выводит всех пользователей из таблицы user в формате json
    :return: Все пользователи
    """
    try:
        if request.method == "GET":
            users = db.session.query(User).all()
            return jsonify([user.user_to_dict() for user in users])
        if request.method == "POST":
            user_data = json.loads(request.data)
            db.session.add(
                User(
                    id=user_data['id'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    age=user_data['age'],
                    email=user_data['email'],
                    role=user_data['role'],
                    phone=user_data['phone'],
                ))
            db.session.commit()
            return jsonify("User created")
    except Exception as e:
        return f'{e}'


@app.route('/users/<int:id>', methods=["GET", "PUT", "DELETE"])
def user_by_id(id):
    """
    Выводит конкретного пользователя с указанным id
    :param id: id пользователя,
    :return: данные пользователя с указанным id в формате json
    """
    try:
        user = User.query.get(id)
        if request.method == "GET":
            return jsonify(user.user_to_dict())
        elif request.method == "PUT":
            if user is None:
                abort(404)
            else:
                db.session.query(User).filter(User.id == id).update(request.json)
                # db.session.query(User).get(id).update(request.json)
                db.session.commit()
                return jsonify("User updated")
        elif request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()
            return jsonify("User deleted")
    except Exception as e:
        return f'{e}'


# Offers
@app.route('/offers/', methods=["GET", "POST"])
def all_offers():
    """
    Выводит все предложения из таблицы offer в формате json
    :return: Все предложения
    """
    try:
        if request.method == "GET":
            offers = db.session.query(Offer).all()
            return jsonify([offer.offer_to_dict() for offer in offers])
        elif request.method == "POST":
            offer_data = json.loads(request.data)
            db.session.add(
                Offer(
                    id=offer_data['id'],
                    order_id=offer_data['order_id'],
                    executor_id=offer_data['executor_id'],
                ))
            db.session.commit()
            return jsonify("Offer created")

    except Exception as e:
        return f'{e}'


@app.route('/offers/<int:id>', methods=["GET", "PUT", "DELETE"])
def offer_by_id(id):
    """
    Выводит конкретного предложения с указанным id
    :param id: id предложения,
    :return: данные предложения с указанным id в формате json
    """
    try:
        offer = Offer.query.get(id)
        if request.method == "GET":
            if offer is None:
                return jsonify("Offer not found")
            else:
                return jsonify(offer.offer_to_dict())
        elif request.method == "PUT":
            db.session.query(Offer).filter(Offer.id == id).update(request.json)
            db.session.commit()
            return jsonify("Offer updated")
        elif request.method == "DELETE":
            db.session.delete(offer)
            db.session.commit()
            return jsonify("Offer deleted")

    except Exception as e:
        return f'{e}'


# Order
@app.route('/orders', methods=["GET", "POST"])
def all_orders():
    """
    Выводит все заказы из таблицы order в формате json
    :return: Все заказы
    """
    try:
        if request.method == "GET":
            orders = db.session.query(Order).all()
            return jsonify([order.order_to_dict() for order in orders])
        elif request.method == "POST":
            order_data = json.loads(request.data)
            db.session.add(
                Order(
                    id=order_data['id'],
                    name=order_data['name'],
                    description=order_data['description'],
                    start_date=order_data['start_date'],
                    end_date=order_data['end_date'],
                    adress=order_data['adress'],
                    price=order_data['price'],
                    customer_id=order_data['customer_id'],
                    executor_id=order_data['executor_id'],
                ))
            db.session.commit()
            return jsonify("Order created")
    except Exception as e:
        return f'{e}'


@app.route('/orders/<int:id>', methods=["GET", "PUT", "DELETE"])
def order_by_id(id):
    """
    Выводит конкретный заказ с указанным id
    :param id: id заказа,
    :return: данные заказа с указанным id в формате json
    """
    try:
        order = Order.query.get(id)
        if request.method == "GET":
            return jsonify(order.order_to_dict())
        elif request.method == "PUT":
            if order is None:
                abort(404)
            else:
                db.session.query(Order).filter(Order.id == id).update(request.json)
                db.session.commit()
                return jsonify("Order updated")
        elif request.method == "DELETE":
            db.session.delete(order)
            db.session.commit()
            return jsonify("Order deleted")
    except Exception as e:
        return f'{e}'


if __name__ == '__main__':
    init_db()
    app.app_context()
    app.run()
