from django.urls import path

from . import views

urlpatterns = [
    path('', views.game, name='Game')
    # path('',views.firstpage,name='firstpage'),
    # path('ipv4addressing/sim/',views.sim,name='sim'),
    # #dev
    # path('simpleparitycheck/',views.experiment2,name='simpleparitycheck'),
    # path('simpleparitycheck/sim/',views.simpleparitycheck,name='simpleparitychecksim')
]
