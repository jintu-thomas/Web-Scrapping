from django.urls import path
from . import views
from pandas import *
data = read_csv("https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit#gid=0")




urlpatterns = [
    path('',views.homepage,name='index'),
    path('submit/',views.submit,name='submit'),
    


    path('amazone/<country>/id/<asin>/<product_title>',name='product'),
    path('amazone/<country>/<id>/<asin>/<imgae_url>',name='imgae'),
    path('amazone/<country>/<id>/<asin>/<price>',name='price'),
    path('amazone/<country>/<id>/<asin>/<details>',name='details'),

]