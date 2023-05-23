from django.urls import path, include
from django.contrib.auth import views as auth_views


from .views import *

urlpatterns = [

    #BASE URLs
    path('login', Login.as_view(), name='login' ),
    path('', DashboardView.as_view(), name='dashboard'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('index', BlankView.as_view(), name='index'),

    # Datatables translation
    path('datatables_translation', DataTablesTranslationsJsonView.as_view(), name='datatables_translation'),

    #APPS URLS
    
    
]