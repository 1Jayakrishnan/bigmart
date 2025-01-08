from django.urls import path
from AdminApp import views

urlpatterns = [
    path("index/",views.index,name="index"),
    path("addcat/",views.addcat,name='addcat'),
    path('save_cat/',views.save_cat,name="save_cat"),
    path("view_cat/",views.view_cat,name='view_cat'),
    path('editcat/<int:c_id>/',views.editcat,name="editcat"),
    path("updatecat/<int:c_id>/",views.updatecat,name="updatecat"),
    path('deletecat/<int:c_id>/',views.deletecat,name='deletecat'),

    path("addpro/",views.addpro,name="addpro"),
    path("savepro/",views.savepro,name="savepro"),
    path("displaypro/",views.displaypro,name="displaypro"),
    path('editpro/<int:p_id>/',views.editpro,name="editpro"),
    path("updatepro/<int:p_id>/",views.updatepro,name="updatepro"),
    path("deletepro/<int:p_id>/",views.deletepro,name="deletepro"),

    path("",views.adminlogin,name="adminlogin"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),

    path('viewCustomers/',views.viewCustomers,name='viewCustomers'),
    path('deleteCustomers/<int:cus_id>/',views.deleteCustomers,name='deleteCustomers'),

    path('viewRegisters/',views.viewRegisters,name='viewRegisters'),
    path('deleteRegisters/<int:reg_id>',views.deleteRegisters,name='deleteRegisters'),
]