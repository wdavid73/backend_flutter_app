from django.db import models
from django.urls import reverse

from api_admin.Table.Model.ModelTable import Table
from api_admin.Drink.Model.ModelDrink import Drink
from api_admin.Complement.Model.ModelComplement import Complement
from api_admin.Dish.models.DishModel import Dish
from auth_app.CustomUser import CustomUser


class Order(models.Model):
    code = models.CharField(max_length=250, null=False, blank=False, unique=True, primary_key=True,
                            error_messages={'unique': "The code entered is already registered, please try another"})
    date = models.DateField()  # [YYYY-MM-DD]
    table = models.ForeignKey(
        Table, db_column="table_id", on_delete=models.CASCADE, null=False)
    total = models.BigIntegerField(null=False, blank=True, default=0)
    action = models.SmallIntegerField(default=1, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    drink = models.ManyToManyField(Drink, through="Order_Drinks")
    complement = models.ManyToManyField(Complement, through="Order_Complement")
    dish = models.ManyToManyField(Dish, through="Order_Dish")
    user = models.ManyToManyField(CustomUser, through="Order_User")

    def __str__(self):
        return "date {} , table {} , total $ {} , code {} | drink {} - complement {}  - dish {}".format(
            self.date, self.table.ref, self.total, self.code, self.drink.name, self.complement.name, self.dish.name
        )

    class Meta:
        db_table = "Order"


class Order_Drinks(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column="order_code")
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Order_Drinks"


class Order_Complement(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column="order_code")
    complement = models.ForeignKey(Complement, on_delete=models.CASCADE)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Order_Complement"


class Order_Dish(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column="order_code")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "order code {} , dish {}".format(self.order.code, self.dish)

    class Meta:
        db_table = "Order_Dish"


class Order_User(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column="order_code")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "order {} - user {}".format(self.order, self.user)

    class Meta:
        db_table = "Order_User"
