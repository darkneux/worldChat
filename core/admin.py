from django.contrib import admin
from .models import *
# Register your models here.


class Message_AdminSite(admin.ModelAdmin):
    list_display = ('message_from',
                    'message_text',
                    'message_createTime',
                     'message_chatroom',
                     'message_to'

                    )

admin.site.register(Message,Message_AdminSite)



#
class ChatRoom_AdminSite(admin.ModelAdmin):
    list_display = ('chatroom_id',
                    'chatroom_name',
                    'chatroom_about',
                    'chatroom_createTime',
                    'chatroom_owner')

admin.site.register(ChatRoom,ChatRoom_AdminSite)




class Group_AdminSite(admin.ModelAdmin):
    list_display = ('group_name',
                    'group_about',
                    'group_createTime',
                    'User_Of_Group',

                    )

admin.site.register(Group,Group_AdminSite)



class Group_Admin_User_AdminSite(admin.ModelAdmin):
    list_display = (
                    'groupAdminUser_group_id',
                    'groupAdminUser_owner',
                    # 'group_owner'
                    )

admin.site.register(Group_Admin_User,Group_Admin_User_AdminSite)




class ChatRoomAdmin_AdminSite(admin.ModelAdmin):
    list_display = ('chatroomAdmin_id',
                    # 'chatroomAdmin_chatroom_id ',
                    # 'chatroomAdmin_admins',
                   )

admin.site.register(ChatRoom_Admin,ChatRoomAdmin_AdminSite)



# class PrivateChat_AdminSite(admin.ModelAdmin):
#     list_display = ('privatechat_id ',
#                      'privatechatTo_user ',
#                     # 'chatroomAdmin_admins',
#                    )
#
# admin.site.register(PrivateChat)

admin.site.register(User_Profile)