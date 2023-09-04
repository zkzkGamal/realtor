from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    # admin url 
    path('realtor/admin-page/page1' , views.admin_page , name='admin_page'),
    path('realtor/admin-page/page1/check-upload-request' , views.check_upload , name='check_upload'),
    path('realtor/admin-page/page1/accept/<int:id>/done' , views.accept_upload , name='accept_upload'),
    path('realtor/admin-page/page1/rejected/<int:id>/done' , views.reject_upload , name='rejected_upload'),
    path('admin/', admin.site.get_urls , name='adminsite'),

    # users url
    path('' ,views.home, name='home'),
    path('realtor/sign', views.sign , name='sign'),
    path('realtor/contact' , views.contactus , name='contact'),
    path('realtor/logout' , views.logout_user , name='logout'),
    path('realtor/citys/appartment' , views.apprtments_citys , name='citys'),
    path('realtor/citys/appartment/11010_<str:type_sell>_11010/search_for_Sell_type' , views.apprtments_citys_type , name='citys_f'),
    path('realtor/citys/appartment/11010_<str:location>_11010d/search_for_Sell_type' , views.apprtments_citys_location , name='citys_f_loc'),
    path('realtor/citys/appartment/aprtmentdetail/he1<int:pk>2h1o2<str:name>*1hhe' , views.ShowAppartmentDetail , name='detail'),
    path('realtor/user/profile' , views.profile_user , name='profile-user'),
    path('realtor/user/add-product' , views.add_product , name='add-product'),
    path('realtor/user/profile/edit' , views.edit_profile_user , name='edit-profile-user'),
    path('realtor/apprtment/' , views.appartment , name='apprtment'),
    path('user/payment',views.pay , name = 'pay'),
    path('user/checkout/soon' , views.checkout , name='checkout'),


    # chat message
    path('realtor/page/page1/messages/123<int:pk>324<str:name>' , views.check_message , name='chat_message'),
    path('user/page/message/' , views.check_message_seller , name='chat_message_seller'),
    path('user/page/message/123<int:pk>324<str:name>' , views.check_message_seller_mes , name='chat_message_seller_mes')

]