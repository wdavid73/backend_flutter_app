from ..Model.ModelOrder import Order, Order_Dish, Order_Drinks, Order_Complement


def calculate_total_orders(orders: Order):
    for order in orders:
        order_dish = Order_Dish.objects.filter(order=order)
        order_comple = Order_Complement.objects.filter(order=order)
        order_drink = Order_Drinks.objects.filter(order=order)
        total_dish = 0 
        total_drink = 0 
        total_complement = 0
        for od in order_dish:
            if order.code == od.order.code:
                total_dish += order.total + od.dish.price
                #order.save()
                # print(od.order.code, od.dish.price)
        for oc in order_comple:
            if order.code == oc.order.code:
                total_complement += order.total + oc.complement.price
                #order.save()
                # print(od.order.code, od.dish.price)
        for od in order_drink:
            if order.code == od.order.code:
                total_drink += order.total + od.drink.price
                #order.save()
                # print(od.order.code, od.dish.price)
        order.total = total_dish + total_drink + total_complement
        order.save()
    return True


def calculate_total_order(code: str, id: int, model):
    order = Order.objects.get(code=code)
    md = model.objects.get(id=id)
    order.total = order.total + md.price
    order.save()
