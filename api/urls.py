from django.urls import path
from .import views

urlpatterns =[

    path('users/',views.show),
    path('postusers/',views.display_message),
    path('users/<int:id>/',views.show_one),
    path('editusers/<int:id>/',views.studentUpdate),
    path('delusers/<int:id>/',views.delStudent),
]