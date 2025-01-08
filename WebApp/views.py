from django.shortcuts import render, redirect
from AdminApp.models import catDb, proDb
from .models import ContactDb, userDb, CartDb, OrderDb
from django.contrib import messages
import razorpay

# Create your views here.

def home(req):
    categories = catDb.objects.all()
    return render(req, "home.html", {'categories':categories})

def about(req):
    return render(req, "about.html")

def contact(req):
    return render(req, "contact.html")


#save the customer details

def save_customer(req):
    if req.method == 'POST':
        cus_name = req.POST.get('name')
        cus_email = req.POST.get("email")
        cus_phone = req.POST.get("phone")
        cus_sub = req.POST.get("subject")
        cus_msg = req.POST.get("message")
        obj = ContactDb(CustomerName=cus_name,CustomerEmail=cus_email,CustomerPhone=cus_phone,CustomerSubject=cus_sub,CustomerMessage=cus_msg)
        obj.save()
        return redirect(contact)

def allproducts(req):
    prods = proDb.objects.all()
    return render(req,'allProducts.html', {'prods':prods})

def filtered_prods(req, catName):
    prods = proDb.objects.filter(Catgories=catName)
    return render(req, 'filtered_products.html', {'prods':prods})

def single_prods(req, prodName):
    prods = proDb.objects.filter(Products=prodName)
    return render(req, 'single_products.html', {'prods':prods})

def userLogin(request):
    return render(request, 'user_login.html')

def userRegister(request):
    return render(request, 'user_register.html')

def save_userReg(request):
    if request.method == 'POST':
        u_name = request.POST.get('user')
        u_mob = request.POST.get("mob")
        u_email = request.POST.get("mail")
        u_pass = request.POST.get("pass")
        uc_pass = request.POST.get("cpass")
        obj = userDb(Username=u_name,Usermobile=u_mob,Useremail=u_email,Password=u_pass,ConfirmPass=uc_pass)
        obj.save()
        return redirect(userLogin)

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ps = request.POST.get('pass')
        if userDb.objects.filter(Username=un, Password=ps).exists():
            request.session['Username'] = un
            request.session['Password'] = ps
            messages.success(request, "Welcome to Home!")
            return redirect(home)
        else:
            messages.warning(request, "Invalid username!")
            return redirect(userLogin)
    else:
        messages.warning(request, "Invalid password!")
        return redirect(userLogin)

# delete the session while logout
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(user_login)

def cart(req):
    data = CartDb.objects.all()
    prod = CartDb.objects.filter(Username=req.session['Username'])
    sub_total = 0
    shipping_amount = 0
    total = 0
    count = 0
    for i in prod:
        sub_total += i.TotalPrice
        if sub_total > 100:
            shipping_amount = 100
        else:
            shipping_amount = 200
        total = sub_total + shipping_amount

        count += 1
    return render(req, 'cart.html', {'data': data, 'prod':prod, 'sub_total': sub_total, 'shipping_amount': shipping_amount, 'total': total, 'count':count})

def save_cart(req):
    if req.method == 'POST':
        qty = req.POST.get('qty')
        pri = req.POST.get("pri")
        tpri = req.POST.get("tpri")
        user = req.POST.get("user")
        proname = req.POST.get("proname")
        try:
            x = proDb.objects.get(Products=proname)
            img = x.ProductImage
        except proDb.DoesNotExist:
            img = None
        obj = CartDb(Username=user,ProductName=proname,Quantity=qty,Price=pri,TotalPrice=tpri,Image=img)
        obj.save()
        messages.success(req, 'Cart added successfully!')
        return redirect(cart)

def deleteCartPro(req, p_id):
    x = CartDb.objects.get(id=p_id)
    x.delete()
    messages.error(req, "Product deleted!!")
    return redirect(cart)

def checkout(req):
    prod = CartDb.objects.filter(Username=req.session['Username'])
    sub_total = 0
    shipping_amount = 0
    total = 0
    count = 0
    for i in prod:
        sub_total += i.TotalPrice
        if sub_total > 100:
            shipping_amount = 100
        else:
            shipping_amount = 200
        total = sub_total + shipping_amount

        count += 1
    return render(req, 'checkout.html',{'sub_total': sub_total, 'shipping_amount': shipping_amount, 'total': total, 'count': count})

def save_cartDetails(req):
    if req.method == 'POST':
        na = req.POST.get('name')
        em = req.POST.get("email")
        pl = req.POST.get("place")
        add = req.POST.get("add")
        mob = req.POST.get("mob")
        state = req.POST.get("state")
        pin = req.POST.get("pin")
        tpr = req.POST.get("tprice")
        ms =req.POST.get('msg') 
        obj = OrderDb(Name=na,Email=em,Place=pl,Address=add,Mobile=mob,State=state,Pin=pin,TotalPrice=tpr,Message=ms)
        obj.save()
        messages.success(req, 'Submitted successfully!')
        return redirect(paymentPage)

def paymentPage(req):
    # retrieve data from OrderDb with the specified id
    customer = OrderDb.objects.order_by('-id').first()

    # get the amount of the specified customer
    payy = customer.TotalPrice

    # convert the amount into paisa (smallest currency unit)
    amount = int(payy*100)  # assuming the payment amount in rupees

    payy_str = str(amount)

    if req.method == 'POST':
        order_currency ='INR'
        client = razorpay.Client(auth=('rzp_test_5m6Hq2UgJxODb3', 'IxGL9dAohRxmsKMKksLqS5pS'))
        payment = client.order.create({'amount':amount, 'currency':order_currency})

    return render(req, 'payment.html', {'customer':customer, 'payy_str':payy_str})
