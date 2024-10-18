import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ecommerce_app.models import *

# Create your views here.


def login(request):
    return render(request,'login.html')




def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')


def adminpage(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')

    return render(request,'adminpage/adminindex.html')


def deliverypage(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')

    return render(request,'deliverypage/deliveryindex.html')

def shoppage(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')


    return render(request,'shoppage/index.html')


def userpage(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')

    return render(request,'userpage/userindex.html')



def add_product_shop(request):
    p=Shop.objects.all()
    return render(request,'shoppage/product.html',{"data":p})


def add_delivery(request):
    d=Delivery.objects.all()
    return render(request,'shoppage/delivery.html',{'data':d})






def add_user(request):
    a=User.objects.all()
    return render(request,'userpage/user.html',{'data':a})



# def order_product_user(request):
#     a=Shop.objects.all()
#     return render(request,'userpage/order product.html',{'data':a})
#

def order_product_user(request):
    a=Cart.objects.get(id=id)
    return render(request,'userpage/order product.html',{'data':a})

def view_complaint_admin(request):

    v=Complaint.objects.all()
    return render(request,'adminpage/view complaint.html',{'data':v})

def view_user(request):
    u=User.objects.all()

    return render(request,'adminpage/view user.html',{'data':u})



def view_user_search(request):
    name=request.POST['name']
    u=User.objects.filter(name__icontains=name)

    return render(request,'adminpage/view user.html',{'data':u})


def sent_reply_admin(request,id):
    r=Complaint.objects.get(id=id)
    return render(request,'adminpage/sent reply admin.html',{'data':r})



def view_reply_user(request):
    v=Complaint.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'userpage/view reply.html',{'data':v})


def manage_shop_admin(request):
    m=Shop.objects.all()
    return render(request,'adminpage/manage shop.html',{'data':m})

def view_shop(request):
    s=Shop.objects.all()
    return render(request,'userpage/view shop.html',{'data':s})




# search option


def view_shop_search(request):

    name=request.POST['name']
    s=Shop.objects.filter(name__icontains=name)


    return render(request,'userpage/view shop.html',{'data':s})








def view_product_shop(request):
    v=Product.objects.filter(SHOP__LOGIN_id=request.session['lid'])
    return render(request,'shoppage/view product shop.html',{'data':v})


def view_product_shop_search(request):
    name=request.POST['name']
    v=Product.objects.filter(name__icontains=name)
    return render(request,'shoppage/view product shop.html',{'data':v})




def view_product_user(request):
    d=Product.objects.all()
    return render(request,'userpage/view product user.html',{'data':d})

def view_product_user_search(request):
    name=request.POST['name']
    d=Product.objects.filter(name__icontains=name)
    return render(request,'userpage/view product user.html',{'data':d})

def view_delivery(request):
    a=Delivery.objects.filter(SHOP__LOGIN_id=request.session['lid'])
    return render(request,'shoppage/view delivery.html',{'data':a})



def view_delivery_search(request):
    name=request.POST['name']
    a=Delivery.objects.filter(name__icontains=name)
    return render(request,'shoppage/view delivery.html',{'data':a})




def delete_product_shop(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/shoppage'</script>''')


def delete_delivery(request,id):
    d=Delivery.objects.get(id=id)
    d.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/shoppage'</script>''')




def view_feedback_admin(request):
    f=Feedback.objects.all()
    return render(request,'adminpage/view feedback admin.html',{'data':f})



def sent_feedback_user(request):

    return render(request,'userpage/sent feedback.html')


def view_order(request):
    k=Order.objects.all()
    return render(request,'shoppage/view order.html',{'data':k})




def view_order_search(request):
    date=request.POST['date']
    k=Order.objects.filter(date__icontains=date)
    return render(request,'shoppage/view order.html',{'data':k})





def view_order_user(request):
    o=Order.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'userpage/view order user.html',{'data':o})




def sent_rating_user(request,id):
    a=Shop.objects.get(id=id)

    return render(request,'userpage/sent rating.html',{'data':a})



def sent_rating_user_POST(request):

    id=request.POST['id']
    rating=request.POST['rating']
    s=Shoprating()
    s.rating=rating
    s.date=datetime.datetime.now().today()
    s.SHOP=Shop.objects.get(id=id)
    s.USER=User.objects.get(LOGIN_id=request.session['lid'])
    s.save()




    return HttpResponse('''<script>alert('sent');window.location='/userpage'</script>''')






def view_rating(request):
    v=Shoprating.objects.all()
    return render(request,'shoppage/view rating.html',{'data':v})



def approve_shop(request,id):
    v=Login.objects.filter(id=id).update(type="shop")

    return HttpResponse('''<script>alert('approved');window.location='/manage_shop_admin'</script>''')



def reject_shop(request,id):
    r=Login.objects.filter(id=id).update(type="pending")

    return HttpResponse('''<script>alert('rejected');window.location='/manage_shop_admin'</script>''')


def add_changepassword_admin(request):

    return render(request,'adminpage/change password admin.html')



def add_changepassword_user(request):
    return render(request,'userpage/change password user.html')




def shopcategory(request):
    return render(request,'adminpage/shopcategory.html')


def shopcategory_POST(request):
    categoryname=request.POST['categoryname']
    c=Shopcategory()
    c.categoryname=categoryname
    c.save()

    return HttpResponse('''<script>alert('success');window.location='/adminpage'</script>''')


def view_shopcategory(request):
    h=Shopcategory.objects.all()
    return render(request,'adminpage/view shopcategory.html',{'data':h})






def view_shopcategory_search(request):
    name=request.POST['categoryname']
    h=Shopcategory.objects.filter(categoryname__icontains=name)
    return render(request,'adminpage/view shopcategory.html',{'data':h})










def edit_shopcategory(request,id):
    e=Shopcategory.objects.get(id=id)
    return render(request,'adminpage/edit shopcategory.html',{'data':e})


def edit_product_shop(request,id):

    b=Product.objects.get(id=id)
    return render(request,'shoppage/edit product shop.html',{'data':b})


def edit_profile_shop(request):
    a=Shopcategory.objects.all()
    v=Shop.objects.get(LOGIN_id=request.session['lid'])


    return render(request,'shoppage/edit profile shop.html',{'data':a,'v':v})



def edit_profile_user(request,id):
    e=User.objects.get(id=id)
    return render(request,'userpage/edit user profile.html',{'data':e})



def edit_delivery(request,id):

    b=Delivery.objects.get(id=id)

    return render(request,'shoppage/edit delivery.html',{'c':b})








def delete_shopcategory(request,id):
    d=Shopcategory.objects.get(id=id)
    d.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/adminpage'</script>''')


def add_shop(request):
    a=Shopcategory.objects.all()
    return render(request,'shoppage/shop.html',{'data':a})









def view_profile_shop(request):
    s=Shop.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'shoppage/view profile shop.html',{'data':s})



def view_profile_user(request):
    v=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'userpage/view profile user.html',{'data':v})



def view_profile_delivery(request):
    u=Delivery.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'deliverypage/view profile delivery.html',{'data':u})





def sent_complaint_user(request):
    return render(request,'userpage/sent complaint.html')



def assignorder(request,id):
    # assign order in shoppage so not using shop as fk...
    a=Order.objects.get(id=id)
    e=Delivery.objects.filter(SHOP__LOGIN_id=request.session['lid'])

    return render(request,'shoppage/assignorder.html',{'data':a,'f':e})




def assignorder_user(request,id):
    a=Order.objects.get(id=id)
    e=Delivery.objects.filter(SHOP__LOGIN_id=request.session['lid'])

    return render(request,'userpage/assign order user.html',{'data':a,'f':e})









def view_assign_order(request):
    a=Assignorder.objects.filter(DELIVERY__LOGIN_id=request.session['lid'])
    return render(request,'deliverypage/view assign order.html',{'data':a})




def view_assign_order_search(request):
    date=request.POST['date']
    a=Assignorder.objects.filter(date__icontains=date)
    return render(request,'deliverypage/view assign order.html',{'data':a})

# assgorder--->order-->USER-->LOGIN {path}

# filter-->view all
def view_assign_order_user(request):
    b=Assignorder.objects.filter(ORDER__USER__LOGIN_id=request.session['lid'])
    return render(request,'userpage/view assign order user.html',{'data':b})




def sent_complaint_user_POST(request):
     complaint=request.POST['complaint']
     a=Complaint()
     a.date=datetime.datetime.now().today()
     a.complaint=complaint

     a.USER=User.objects.get(LOGIN_id=request.session['lid'])

     a.reply="pending"

     a.save()

     return HttpResponse('''<script>alert('send');window.location='/userpage'</script>''')


def add_shop_POST(request):
    SHOPCATEGORY=request.POST['select']
    name=request.POST['name']
    image=request.FILES['image']
    address=request.POST['address']
    phone=request.POST['phone']
    email=request.POST['email']

    fs= FileSystemStorage()
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") +'.JPG'
    fs.save(date,image)
    path=fs.url(date)



    c=Login()
    c.username=email
    c.password=phone
    c.type="pending"
    c.save()


    d=Shop()
    d.name=name
    d.SHOPCATEGORY=Shopcategory.objects.get(id=SHOPCATEGORY)
    d.image=path
    d.address=address
    d.phone=phone
    d.email=email
    d.LOGIN = c
    d.save()


    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')




def add_user_POST(request):
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    image=request.FILES['image']
    address=request.POST['address']



    fs= FileSystemStorage()
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") +'.JPG'
    fs.save(date,image)
    path=fs.url(date)


    a=Login()
    a.username=email
    a.password=phone
    a.type="user"
    a.save()


    b=User()
    b.name=name
    b.phone=phone
    b.email=email
    b.image=path
    b.address=address
    b.LOGIN=a
    b.save()


    return HttpResponse('''<script>alert('success');window.location='/'</script>''')













def add_delivery_POST(request):

    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    email=request.POST['email']

    a=Login()
    a.username=email
    a.password=phone
    a.type="delivery"
    a.save()



    b=Delivery()
    b.name=name
    b.SHOP=Shop.objects.get(LOGIN_id=request.session['lid'])
    b.phone=phone
    b.address=address
    b.email=email

    b.LOGIN=a
    b.save()

    return HttpResponse('''<script>alert('added');window.location='/shoppage'</script>''')


def add_product_shop_POST(request):

    name=request.POST['name']

    productcategory=request.POST['productcategory']
    productprice=request.POST['productprice']
    image=request.FILES['image']
    quantity=request.POST['quantity']



    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') +'.JPG'
    fs.save(date,image)
    path=fs.url(date)




    f=Product()
    f.name=name
    f.productcategory=productcategory
    f.productprice=productprice
    f.image=path
    f.quantity=quantity
    f.SHOP=Shop.objects.get(LOGIN_id=request.session['lid'])
    f.save()
    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')






def order_product_user(request,id):
    a=Cart.objects.get(id=id)
    return render(request,'userpage/order product.html',{'data':a})



def order_product_user_POST(request,id):

    cid=Cart.objects.get(id=id)
    tq=cid.quantity
    tp=cid.total
    cid.status='add'
    cid.save()

    a=Order()
    a.CART=cid
    a.totalquantity=tq
    a.totalprice=tp
    a.status='ordered'
    a.date=datetime.datetime.now().today().date()
    a.USER = User.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('success');window.location='/userpage'</script>''')





def update_order(request,id):
    #assignorder table to  changed
    r=Assignorder.objects.filter(id=id).update(status="delivered")

    return HttpResponse('''<script>alert('updated');window.location='/view_assign_order'</script>''')






# def update_order(request):
#     a=Cart.objects.get(id=id)
#     return render(request,'deliverypage/update order.html',{'data':a})
#



# def update_order_POST(request):
#     u=Cart.objects.get(id=id)
#     b=u.totalquantity
#     c=u.totalprice
#     b.status='add'
#     b.save()
#
#     a=Order()
#     a.Cart=u
#     a.totalquantity=b
#     a.totalprice=c
#     a.status="updated"
#
#     a.date=datetime.datetime.now().today().date()
#     a.save()
#
#     return HttpResponse('''<script>alert('success');window.location='/deliverypage'</script>''')
#
#












def add_cart(request,id):
    c=Product.objects.get(id=id)


    return render(request,'userpage/add cart.html',{'data':c})

def add_cart_POST(request):
    quantity=request.POST['quantity']

    # id=product id
    id=request.POST['id']

    cc=Product.objects.get(id=id)
    # price= if floating price * floating value of quantity
    tt=cc.productprice * float(quantity)



    a=Cart()
    a.quantity=quantity
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.PRODUCT=Product.objects.get(id=id)
    a.total=tt
    a.status='cart'
    a.date=datetime.datetime.now().today()

    a.save()
    return HttpResponse('''<script>alert('success');window.location='/userpage'</script>''')



# def order_product_user_POST(request):
#
#
#
#        return HttpResponse('''<script>alert('success');window.location='/userpage'</script>''')


def edit_shopcategory_POST(request):
    id=request.POST['id']
    categoryname=request.POST['select']
    c=Shopcategory.objects.get(id=id)
    c.categoryname=categoryname
    c.save()
    return HttpResponse('''<script>alert('success');window.location='/adminpage'</script>''')


def edit_product_shop_POST(request):
    id=request.POST['id']
    name=request.POST['name']
    productcategory=request.POST['productcategory']
    productprice=request.POST['productprice']

    quantity=request.POST['quantity']




    w=Product.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.JPG'
        fs.save(date, image)
        path = fs.url(date)
        w.image = path

    w.name=name
    w.productcategory=productcategory
    w.productprice=productprice
    w.quantity=quantity
    w.save()
    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')




def edit_delivery_POST(request):
    id=request.POST['id']

    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    email=request.POST['email']

    a=Delivery.objects.get(id=id)
    a.name=name

    a.phone=phone
    a.address=address
    a.email=email
    a.save()
    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')






def edit_view_profile_shop_POST(request):
    id=request.POST['id']
    categoryname = request.POST['select']
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    email=request.POST['email']

    h=Shop.objects.get(id=id)


    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.JPG'
        fs.save( date,image)
        path = fs.url(date)
        h.image = path

    h.name=name
    h.address=address
    h.phone=phone
    h.email=email
    h.SHOPCATEGORY=Shopcategory.objects.get(id=categoryname)
    h.save()
    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')



def edit_profile_user_POST(request):
    id=request.POST['id']
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    address=request.POST['address']


    f=User.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M=%S") + '.JPG'
        fs.save(date,image)
        path = fs.url(date)
        f.image=path



    f.name=name
    f.phone=phone
    f.email=email
    f.address=address
    f.save()


    return HttpResponse('''<script>alert('success');window.location='/userpage'</script>''')




def view_cart(request):
    v=Cart.objects.filter(USER__LOGIN_id=request.session['lid'],status='cart')
    return render(request,'userpage/view cart.html',{'data':v})




def view_cart_search(request):
    date=request.POST['date']
    v=Cart.objects.filter(date__icontains=date)
    return render(request,'userpage/view cart.html',{'data':v})






















def add_changepassword_admin_POST(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    p=Login.objects.filter(password=oldpassword,id=request.session['lid'])


    if p.exists():
        if newpassword==confirmpassword:
            d=Login.objects.filter(password=oldpassword,id=request.session['lid']).update(password=confirmpassword)

            return HttpResponse('''<script>alert('confirmed');window.location='/adminpage'</script>''')

        else:
            return HttpResponse('''<script>alert('confirmed');window.location='/adminpage'</script>''')


    else:
        return HttpResponse('''<script>alert('confirmed');window.location='/adminpage'</script>''')




def add_changepassword_shop(request):
    return render(request,'shoppage/change password shop.html')



def add_changepassword_shop_POST(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']

    h=Login.objects.filter(password=oldpassword,id=request.session['lid'])
    if h.exists():
        if newpassword==confirmpassword:
            v=Login.objects.filter(password=oldpassword,id=request.session['lid']).update(password=confirmpassword)

            return HttpResponse('''<script>alert('update');window.location='/shoppage'</script>''')

        else:
            return HttpResponse('''<script>alert('invalid');window.location='/shoppage'</script>''')


    else:
        return HttpResponse('''<script>alert('invalid');window.location='/shoppage'</script>''')





def add_changepassword_user_POST(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']

    v=Login.objects.filter(password=oldpassword,id=request.session['lid'])

    if v.exists():
        if newpassword==confirmpassword:
            p=Login.objects.filter(password=oldpassword,id=request.session['lid'].update(newpassword=confirmpassword))

            return HttpResponse('''<script>alert('confirmed');window.location='/userpage'</script>''')


        else:
            return HttpResponse('''<script>alert('confirmed');window.location='/userpage'</script>''')


    else:
        return HttpResponse('''<script>alert('confirmed');window.location='/shoppage'</script>''')

















def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    l=Login.objects.filter(username=username,password=password)

    if l.exists():
        m=Login.objects.get(username=username,password=password)
        request.session['lid']=m.id


        if m.type=='admin':
            return redirect('/adminpage')

        elif m.type=="shop":
            ob=Shop.objects.filter(LOGIN_id=m.id)
            if ob.exists():

                return redirect('/shoppage')
            else:
                return HttpResponse('''<script>alert('invalid');window.location='/'</script>''')

        elif m.type=="user":
            return redirect('/userpage')

        elif m.type=="delivery":
            return redirect('/deliverypage')

        else:
            return redirect('/')


    else:
        return redirect('/')



def sent_reply_admin_post(request):
    id=request.POST['id']
    reply=request.POST['reply']
    c=Complaint.objects.get(id=id)
    c.reply=reply
    c.status="replied"
    c.save()

    return HttpResponse('''<script>alert('replied');window.location='/adminpage'</script>''')




def sent_feedback_POST(request):
    feedback=request.POST['feedback']
    f=Feedback()
    f.feedback=feedback
    f.USER=User.objects.get(LOGIN_id=request.session['lid'])
    f.date=datetime.datetime.now().today()
    f.save()
    return HttpResponse('''<script>alert('send');window.location='/userpage'</script>''')




def assignorder_POST(request):
    id=request.POST['id']
    DELIVERY=request.POST['s']


    h=Assignorder()
    h.date=datetime.datetime.now().today()
    h.ORDER=Order.objects.get(id=id)
    h.SHOP=Shop.objects.get(LOGIN_id=request.session['lid'])
    h.DELIVERY=Delivery.objects.get(id=DELIVERY)
    h.date=datetime.datetime.now().today()
    h.status="assigned"
    h.save()

    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')




def assignorder_POST_user(request):
    id=request.POST['id']
    DELIVERY=request.POST['s']


    h=Assignorder()
    h.date=datetime.datetime.now().today()
    h.ORDER=Order.objects.get(id=id)
    h.SHOP=Shop.objects.get(LOGIN_id=request.session['lid'])
    h.DELIVERY=Delivery.objects.get(id=DELIVERY)

    h.status="assigned"
    h.save()

    return HttpResponse('''<script>alert('success');window.location='/shoppage'</script>''')











