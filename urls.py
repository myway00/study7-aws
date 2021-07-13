from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('<str:id>',detail, name="detail" ),
    #데이터 아이디 값에 따라 값이 다르게 나오게 된다
    # 두번째 인자는 views의 함수이름
    # 마지막은 이름
    path('new/',new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]
