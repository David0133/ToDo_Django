from django.urls import path

from To_Do_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('markDone/<int:pk>', views.markDone, name='markDone'),
    path('markUndone/<int:pk>', views.markUndone, name='markUndone'),
    path('delete/<int:pk>',views.deleteTask,name='deleteTask'),
    path('addTask',views.addTask,name='addTask'),
    path('editPage/<int:pk>',views.editPage,name='editPage'),
    path('updateTask/<int:pk>',views.updateTask,name='updateTask')
]