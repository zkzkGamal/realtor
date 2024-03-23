from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , Group
from .models import *
from .decorators import *
from .filters import *
from django.db.models import Q
# Create your views here.
#DONE
def home(request):
    products = product.objects.filter(active = True)
    if request.method == 'POST' and request.POST.get('Q&A'):
        messageQA.objects.get_or_create(email = request.POST.get('email_QA') , qustion = request.POST.get('qustion'))
        return redirect('home')
    return render(request , 'home.html' , {'product':products})
#DONE sign and out pages
@authandicated
def sign(request):
    if request.method == 'POST':
        logina = request.POST.get('login')
        if logina:
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            user = authenticate(request , username = username , password = password)
            if user is not None:
                print('welcome' , user.get_username())
                login(request , user)
                if user.is_superuser:
                    return redirect('admin_page')
                else:
                    return redirect('home')
        else:
            username = request.POST.get('user_name')
            password = request.POST.get('password1')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('mobilenumber')
            user = User.objects.create_user(username= username , password=password , email=email)
            profile_user = profile(user = user , email = email , phone = phone , address = address , f_name = username)
            if user:
                profile_user.save()
                group = Group.objects.get(name = 'user')
                user.groups.add(group)
                login( request , user)
                return redirect('home')
    return render(request , 'login.html')
def logout_user(request):
    logout(request)
    return redirect('home')

#DONE   profile page

@login_required(login_url = 'sign')
@adminORuser
def profile_user(request):
    user = request.user
    seller = user.groups.filter(name='seller').exists()
    profileData = profile.objects.get(user = request.user)
    context = {'data':profileData , 'seller':seller}
    return render(request , 'profile-user.html' , context)
@login_required(login_url = 'sign')
@adminORuser
def edit_profile_user(request):
    profileData = profile.objects.get(user = request.user)
    context = {'data':profileData}
    if request.method == 'POST':
        profileData.f_name = request.POST.get('firstname')
        profileData.L_name = request.POST.get('lastname')
        profileData.phone = request.POST.get('phone')
        profileData.email = request.POST.get('email')
        profileData.address = request.POST.get('address')
        profileData.country = request.POST.get('country')
        profileData.picture = request.FILES.get('picture')
        profileData.save()
        print(request.FILES.get('picture'))
        return redirect('profile-user')
    return render(request , 'user-profile-sittings.html' , context)
# DONE -user upload
@login_required(login_url='sign')
@adminORuser
def add_product(request):
    profile_user = profile.objects.get(user = request.user)
    if request.method == 'POST':
        name = request.POST.get('product_name')
        Description = request.POST.get('about')
        location = request.POST.get('location')
        type_house = request.POST.get('product_type')
        style_house = request.POST.get('style')
        area = request.POST.get('area')
        price = request.POST.get('price')
        number_kitchen = request.POST.get('kitchen')
        number_bedroom = request.POST.get('num_of_bedrooms')
        number_bathroom = request.POST.get('num_of_bathrooms')
        sell_for = request.POST.get('sell_for')
        sell_option = request.POST.get('sell_option')
        pics = request.FILES.getlist('image')
        new_product = product(profile_user = profile_user , name = name , Description = Description , location = location ,
                              type_house = type_house , style_house = style_house , 
                              area = area , price = price , number_bathroom = number_bathroom , 
                              number_bedroom = number_bedroom , number_kitchen = number_kitchen , 
                              sell_type = sell_option , house_for = sell_for , pics = pics[0])
    
        if pics:
            user = request.user
            new_product.save()
            group = Group.objects.get(name = 'seller')
            user.groups.add(group)
            Product = product.objects.get(profile_user = profile_user , name = name)
            for pic in pics:
                produc_image = produc_images.objects.create(Product =Product , img = pic)
            return redirect('home')
    return render(request,'add-product.html')
# Done filtering product and all product view
def apprtments_citys(request):
    products = product.objects.filter(active = True)
    myFilter = ProductFilter(request.GET, queryset=products)
    products= myFilter.qs
    context = {'products' : products , 'filter':myFilter}
    return render(request , 'apprtments-city.html' , context )
def apprtments_citys_type(request , type_sell):
    products = product.objects.filter(active = True , sell_type = type_sell)
    myFilter = ProductFilter(request.GET, queryset=products)
    products= myFilter.qs
    context = {'products' : products , 'filter':myFilter ,'d':1}
    return render(request , 'apprtments-city.html' , context )
def appartment(request):
    products = product.objects.filter(active = True)
    listt = []
    for e in products:
        listt.append(e.location)
    listt = list(set(listt))
    myFilter = ProductFilter(request.GET, queryset=products)
    products= myFilter.qs
    context = {'loction':listt , 'filter':myFilter}
    return render(request , 'apprtments-1.html' , context)
def apprtments_citys_location(request , location):
    products = product.objects.filter(active = True , location = location)
    myFilter = ProductFilter(request.GET, queryset=products)
    products= myFilter.qs
    context = {'products' : products , 'filter':myFilter ,'ds':1}
    return render(request , 'apprtments-city.html' , context )
def ShowAppartmentDetail(request , pk , name):
    productDetail = product.objects.get(id = pk)
    context = {'detail':productDetail}
    return render(request , 'aprtmebt-information.html' , context)
# done product proccess 
@login_required(login_url='sign')
@adminORuser
def pay(request):
    if request.method == 'POST':
        return redirect('checkout')
    return render(request , 'payment.html')
@login_required(login_url='sign')
@adminORuser
def checkout(req):
    return render(req , 'coming-soon.html')
#Done - Adimn in our page checking requests
@only_admin
def admin_page(request):
    message = messageQA.objects.all()
    return render(request , 'admin-page.html' , {'msgs':message})
@only_admin
def check_upload(request):
    requested_product = product.objects.filter(active = False)
    context = {'products':requested_product}
    return render(request , 'reguest-uplaod.html' , context)
@only_admin
def accept_upload(request , id):
    uploaded_product = product.objects.get(id = id)
    uploaded_product.active = True
    uploaded_product.save()
    return redirect('check_upload')
@only_admin
def reject_upload(request , id):
    uploaded_product = product.objects.get(id = id)
    uploaded_product.delete()
    return redirect('check_upload')
# conect form application
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings
def contactus(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('PhoneNumber')
        email = request.POST.get('email')
        message = request.POST.get('message')
        x = EmailMessage(
             f'New Contact Form Submission from {username}' ,
             f'From: {email}\n\n{message}' ,
              email,
            ['realtorappams@gmail.com'] 
        )
        # x.send()
        return redirect('contact')
    return render(request , 'contact-us.html')







#----------------------------------------------------------------------------------

# work in it  --- add pay in html only


@login_required(login_url='sign')
def check_message(request , pk , name):
    user = request.user
    profile_user = profile.objects.filter(user = user)
    if profile_user:
        profile_user = profile_user.first()
        recevier = profile.objects.get(f_name = name , id = pk)
        if profile_user.user.username == recevier.user.username:
            return redirect('home')
        messagess = saved_message.objects.filter(Q(reciver = profile_user) | Q(sender = profile_user)).order_by('time_stamp')
        context = {'name':name , 'id': pk,'messages': messagess , 
                'profile': profile_user , 'status':recevier.status}
        return render(request ,'chat-user.html' , context)
    else:
        return redirect('home')

@login_required(login_url='sign')
def check_message_seller(request):
    profile_user = profile.objects.get(user = request.user)
    messagess = saved_message.objects.filter(reciver = profile_user)
    senders = []
    for sd in messagess:
        senders.append(sd.sender)
    senders = list(set(senders))
    return render(request , 'chat-admin.html' , {'senders':senders , 'profile':profile_user})


@login_required(login_url='sign')
def check_message_seller_mes(request , pk , name):
    user = request.user
    profile_user = profile.objects.get(user = user)
    messagess = saved_message.objects.filter(Q(reciver = profile_user) | Q(sender = profile_user)).order_by('time_stamp')
    senders = []
    for sd in messagess:
        senders.append(sd.sender)
    senders = list(set(senders))
    sender_data = profile.objects.get(id = pk , f_name = name)
    context = {'name':name , 'id': pk ,'messages': messagess 
               , 'senders':senders , 'profile':profile_user , 'sd_data':sender_data}
    return render(request , 'chat-admin-room.html' , context)
