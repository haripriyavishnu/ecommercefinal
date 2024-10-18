from django.db import models

# Create your models here.



class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    address=models.CharField(max_length=100)


class Shopcategory(models.Model):
    categoryname=models.CharField(max_length=100)


class Shop(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    SHOPCATEGORY=models.ForeignKey(Shopcategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)


class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)

class Feedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    feedback=models.CharField(max_length=100)


class Product(models.Model):
    SHOP=models.ForeignKey(Shop,on_delete=models.CASCADE)
    productcategory=models.CharField(max_length=100)
    productprice=models.FloatField()
    image=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    name=models.CharField(max_length=100)


class Delivery(models.Model):
    SHOP=models.ForeignKey(Shop,on_delete=models.CASCADE)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)







class Shoprating(models.Model):
    SHOP=models.ForeignKey(Shop,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    date=models.CharField(max_length=100)


class Cart(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    quantity=models.IntegerField()
    total=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class Order(models.Model):
    CART=models.ForeignKey(Cart,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    totalquantity=models.CharField(max_length=100)
    totalprice=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class Assignorder(models.Model):
    SHOP=models.ForeignKey(Shop,on_delete=models.CASCADE)
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    DELIVERY=models.ForeignKey(Delivery,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)










