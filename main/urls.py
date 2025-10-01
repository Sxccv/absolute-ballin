from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('',views.home,name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('prod/<str:id>/', views.view_product, name='view_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('prod/<str:id>/edit',views.edit_product,name='edit_product'),
    path('prod/<str:id>/delete',views.delete_product,name='delete_product')
]

