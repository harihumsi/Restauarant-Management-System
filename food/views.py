from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Contact, Order, Food_Item, Review
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    print(request.user, type(request.user))
    if str(request.user) == "AnonymousUser":
        return redirect("/login")
    else:
        return render(request, 'base.html')
    
def review(request):
    if request.method == "POST":
        name = request.POST["username"]
        content = request.POST["content"]
        #print( request.user.email, name, content)
        if(len(name) == 0 or len(content) == 0):
            messages.warning(request, "Please check your review form.")
        
        else:
            data = Review(name = name, review= content)
            data.save()
            messages.success(request, "Review sent successfully !")
            return redirect("/")
    return render(request, "review.html")
    
def read(request):
    return render(request, "read.html")
    
def logouts(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("/login")


def Signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['name']
        email = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(first_name, last_name, email)
        
        if password1 != password2:
            messages.warning(request, "Passwords mismatch")
        
        else:
            if len(username)<2 or len(email)<3 or len(password1)<8 or len(email)<15:
                messages.error(request, "Please check the form")
            
            else:
                data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                data.save()
                messages.success(request, "Registration Successful")
                return redirect('/login')
       
    return render(request, 'signup.html')


def loginn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username= username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, "Login successfully")
            return redirect('/')
        
        else:
            messages.error(request, "Login unsuccessful")
        
    return render(request, 'login.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        print(name, email, phone, content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            return redirect('/')
        
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def order(request):
    if request.method == "POST":
        name = request.POST["name"]
        number = request.POST["number"]
        item_name = request.POST["item_name"]
        item_quantity = request.POST["item_quantity"]
        print(name, number, item_name, item_quantity)
        if int(item_quantity) <= 0 :
            messages.error(request, "Item quantity should be atleast one.")
        else:
            data = Order(name=name, number=number, item_name=item_name, item_quantity=item_quantity)
            data.save()
            messages.success(request, "Order successful !")
            return redirect("/")
    return render(request, 'order.html')

def menu(request):
    all_items = Food_Item.objects.all()
    context = {
        'all_items' : all_items
    }
    
    for i in all_items:
        print(i.name)
    
    return render(request, "menu.html", context)

def search(request):
    query=request.GET['query']
    print(query)
    allPosts1 = Food_Item.objects.filter(name__icontains=query)
    allPosts2 = Food_Item.objects.filter(item_price__icontains = query)
    allPosts =  allPosts1.union(allPosts2)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
        return redirect("/")
    else:
        params={'allPosts': allPosts, 'query': query}    
        return render(request, 'search.html', params)
    
def payment(request):
    return render(request, "payment.html")

def bill(request):
    if request.method == "POST":
        query = request.POST["table"]
        char = request.POST["character"]
        dict = {}
        sub_total = 0
        total = 0
        d = 0
        t = 0
        discount = {"S":0.15, "V":0.3 , "R" : 0.10}
        all_posts1 = Order.objects.filter(number = int(query)).values()
        for i in all_posts1:
            
            item = Food_Item.objects.filter(name = i["item_name"]).values()
            for x in item:
                sub_total += i["item_quantity"]*int(x["item_price"][3:])
                dict[i["item_name"]] = {"name" : i["item_name"], "price":x["item_price"], "quantity" : i["item_quantity"], "sub_price": sub_total}
                
            total += sub_total
            sub_total = 0
        t =total
        if char in discount:
            total -= total*discount[char]
            d = t*discount[char]
        context={
            "allposts" : dict,  "total": total , 'discount': d, "t" : t
        }
        return render(request, "bill.html", context)
        
    

# Create your views here.
