from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.







class User_Profile(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      bio = models.TextField(max_length=120,default='')
      class Meta:
            def __init__(self):
                  self.username = None


class ChatRoom(models.Model):
      chatroom_id = models.BigAutoField(primary_key=True)
      chatroom_name = models.CharField(max_length=16,unique=True)
      chatroom_passwd = models.CharField(max_length=32)
      chatroom_owner = models.ForeignKey(User,on_delete=models.CASCADE)
      chatroom_about = models.CharField(max_length=96,default='')
      chatroom_createTime = models.DateTimeField(auto_now_add=True)


class ChatRoom_Admin(models.Model):
      chatroomAdmin_id = models.BigAutoField(primary_key=True)
      chatroomAdmin_chatroom_id = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
      chatroomAdmin_admins = models.ManyToManyField(User)

class Group(models.Model):
      group_id = models.BigAutoField(primary_key=True)
      group_name = models.CharField(max_length=64)
      group_about = models.CharField(max_length=96,default='')
      group_createTime = models.DateTimeField(auto_now_add=True)
      group_users = models.ManyToManyField(User)
      def User_Of_Group(self):
          return ',' .join([str(p) for p in self.group_users.all()])


# class Meal(models.Model):
#     name = models.CharField(max_length=255)
#     date = models.DateField()
#     members = models.ManyToManyField(Member)

#
class Group_Admin_User(models.Model):
      groupAdminUser_id = models.BigAutoField(primary_key=True)
      groupAdminUser_group_id = models.ForeignKey(Group,on_delete=models.CASCADE)
      groupAdminUser_owner = models.ForeignKey(User,on_delete=models.CASCADE)

class Message(models.Model):
      message_id = models.BigAutoField(primary_key=True)
      message_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_fromUser')
      message_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='message_toUser',null=True)
      message_text = models.TextField()
      message_createTime = models.DateTimeField(auto_now_add=True)
      message_group = models.ForeignKey(Group, on_delete=models.CASCADE,null=True)
      message_chatroom = models.ForeignKey(ChatRoom,on_delete=models.CASCADE,null=True)



@receiver(post_save,sender=User)
def create_User_Profile(sender,instance,created,**kwargs):
      if created:
            User_Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_User_Profile(sender,instance,**kwargs):
      instance.user_profile.save()

