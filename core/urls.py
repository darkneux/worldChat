from django.urls import path
from . import views
urlpatterns = [
    path('',views.chat_global),
    path('create/chatroom/',views.create_ChatRoom),
    path('chatroom/<chatroom_name>/',views.chat_ChatRoom),
    path('global/',views.chat_global),
    path('create/group/',views.create_group),
    path('all/chat',views.all_privateChatUser),
    path('chat/<private_username>',views.chat_privateChat),
    path('login/',views.loginPage),
    path('demo/<group_name>/',views.demo),
    path('signup/',views.signupPage),


]
