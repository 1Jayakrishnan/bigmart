from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from AdminApp.models import catDb, proDb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import datetime
from WebApp.models import ContactDb, userDb
from django.contrib import messages

# Create your views here.

def index(req):
    categories = catDb.objects.count()
    products = proDb.objects.count()
    date = datetime.now()
    return render(req, "index.html", {'categories':categories, 'products':products, 'date':date})

def addcat(req):
    return render(req, "addcategories.html")

def save_cat(req):
    if req.method == 'POST':
        cat = req.POST.get('cname')
        des = req.POST.get("desc")
        im = req.FILES['img']
        obj = catDb(CategoryName=cat, Description=des, Image=im)
        messages.success(req, 'Category added successfully!')
        obj.save()
        return redirect(addcat)

def view_cat(req):
    data = catDb.objects.all()
    return render(req, "viewcategories.html", {'data': data})


def editcat(req, c_id):
    data = catDb.objects.get(id=c_id)
    return render(req, "editcategory.html", {'data': data})

def updatecat(req, c_id):
    if req.method == "POST":
        cat = req.POST.get('cname')
        des = req.POST.get("desc")
        try:
            img = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = catDb.objects.get(id=c_id).Image
        catDb.objects.filter(id=c_id).update(CategoryName=cat, Description=des, Image=file)
        messages.success(req, "Category updates successfully!")
        return redirect(view_cat)


def deletecat(req, c_id):
    x = catDb.objects.get(id=c_id)
    x.delete()
    messages.error(req, "Category deleted..")
    return redirect(view_cat)


def addpro(req):
    category = catDb.objects.all()
    return render(req, "addproducts.html", {'category':category})

def savepro(req):
    if req.method == 'POST':
        cat = req.POST.get('procat')
        pro = req.POST.get("proname")
        pri = req.POST.get('price')
        des = req.POST.get("desc")
        im = req.FILES['img']
        obj = proDb(Catgories=cat, Products=pro, Price=pri,Description=des,ProductImage=im)
        obj.save()
        messages.success(req, "Product added!")
        return redirect(addpro)

def displaypro(req):
    data = proDb.objects.all()
    return render(req, "viewpro.html", {'data':data})

def editpro(req, p_id):
    data = proDb.objects.get(id=p_id)
    category = catDb.objects.all()
    return render(req, "editprod.html", {'data': data, 'category':category})

def updatepro(req, p_id):
    if req.method == 'POST':
        cat = req.POST.get('procat')
        pro = req.POST.get("proname")
        pri = req.POST.get('price')
        des = req.POST.get("desc")
        try:
            img = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = proDb.objects.get(id=p_id).ProductImage
        proDb.objects.filter(id=p_id).update(Catgories=cat, Products=pro, Price=pri,Description=des,ProductImage=file)
        messages.success(req, "Product updated!")
        return redirect(displaypro)

def deletepro(req, p_id):
    x = proDb.objects.get(id=p_id)
    x.delete()
    messages.error(req, "Product deleted!!")
    return redirect(displaypro)

# admin login page
def adminlogin(req):
    return render(req, "admin_login.html")

def admin_login(request):
    if request.method == "POST":
         un = request.POST.get("username")
         pwd = request.POST.get("password")
         if User.objects.filter(username__contains=un).exists():
             x = authenticate(username=un, password=pwd)
             if x is not None:
                 login(request, x)
                 request.session['username'] = un          #create the session while login
                 request.session['password'] = pwd
                 messages.success(request, 'Welcome to Admin dashboard!')
                 return redirect(index)
             else:
                 messages.warning(request, 'Invalid password!')
                 return redirect(adminlogin)
         else:
             messages.warning(request, 'Invalid username!')
             return redirect(adminlogin)


# delete the session while logout
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)

#see the details of customers for contact
def viewCustomers(req):
    customer = ContactDb.objects.all()
    return render(req, 'viewCustomers.html', {'customer':customer})

def deleteCustomers(req, cus_id):
    x = ContactDb.objects.get(id=cus_id)
    x.delete()
    return redirect(viewCustomers)

#registerd user details
def viewRegisters(req):
    users = userDb.objects.all()
    return render(req, 'viewRegisters.html', {'users':users})

def deleteRegisters(req, reg_id):
    x = userDb.objects.get(id=reg_id)
    x.delete()
    return redirect(viewRegisters)

