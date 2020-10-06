from django.urls import path
from . import views

urlpatterns = [
    # index : 종목 번호
    path('', views.index, name='index'),
    # path 첫 번째 인자에 / 빼먹지 말것.
    path('<str:stock_id>/', views.detail, name='detail'),
    path('results/', views.results, name='results')
]
