
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stupost/', views.student_post),
    path('stuget/<int:pk>', views.student_jsonresponse),
]
