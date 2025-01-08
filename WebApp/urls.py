from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('save_customer/',views.save_customer,name='save_customer'),
    path('allproducts/',views.allproducts,name='allproducts'),
    path('filtered_prods/<catName>/',views.filtered_prods,name='filtered_prods'),
    path('single_prods/<prodName>/',views.single_prods,name='single_prods'),

    path('',views.userLogin,name='userLogin'),
    path('userRegister/',views.userRegister,name='userRegister'),
    path('save_userReg/',views.save_userReg,name='save_userReg'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),

    path('cart/',views.cart,name='cart'),
    path('save_cart/',views.save_cart,name='save_cart'),
    path('deleteCartPro/<int:p_id>/',views.deleteCartPro,name='deleteCartPro'),

    path('checkout/',views.checkout,name='checkout'),
    path('save_cartDetails/',views.save_cartDetails,name='save_cartDetails'),
    path('paymentPage/',views.paymentPage,name='paymentPage'),
]