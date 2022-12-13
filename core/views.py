from django.shortcuts import render
from .models import *
from django.contrib.auth import login,authenticate,logout

from django.db.models import Q
from django.shortcuts import redirect

from django.http import HttpResponseRedirect

# Create your views here.

def startpage(request):
    return render(request,'index.html')

def chat_global(request):

    if not request.user.is_authenticated:
        return redirect('/signup')

    print(request.user)
    present_chatroom_chats = Message.objects.filter(message_chatroom__isnull=True,message_group__isnull=True).order_by('message_createTime')
    login_user = User.objects.get(pk=request.user.id)
    data = {
        'messages': present_chatroom_chats,
        'login_user': login_user
    }
    print(type(request.user))

    if request.method == 'POST':
        message = request.POST['message']
        newchatroom = Message(message_from=request.user, message_text=message)
        newchatroom.save()
        return redirect('/global/')

    return render(request, 'globalChat_page.html',data)



def chat_ChatRoom(request,chatroom_name):
    if not request.user.is_authenticated:
        return redirect('/signup')

    chatroom = ChatRoom.objects.get(chatroom_name=chatroom_name)
    chatroom_id = chatroom.chatroom_id
    present_chatroom_chats = Message.objects.filter(message_chatroom=chatroom_id).order_by('message_createTime')
    login_user = User.objects.get(pk=request.user.id)

    data ={
        'messages': present_chatroom_chats,
        'login_user': login_user
    }
    #
    # for i in present_chatroom_chats:
    #     print(i.message_text,type(i.message_from))
    # print(type(request.user))


    if request.method == 'POST' :
        message = request.POST['message']
        newchatroom = Message(message_from=request.user,message_text=message,message_chatroom=chatroom)
        newchatroom.save()
        return HttpResponseRedirect("/chatroom/{chatroomname}".format(chatroomname=chatroom_name))

    return render(request,'chatroom_page.html',data)



def create_ChatRoom(request):
    if not request.user.is_authenticated:
        return redirect('/signup')

    if request.method == 'POST' :
        chatroom_name = request.POST['chatroom_name']
        chatroom_passwd = request.POST['chatroom_passwd']
        chatroom_about = request.POST['chatroom_about']
        if chatroom_name == 'global':
            return redirect('/global/')

        newchatroom = ChatRoom(chatroom_name=chatroom_name,chatroom_passwd=chatroom_passwd,chatroom_about=chatroom_about,chatroom_owner=request.user)
        newchatroom.save()
        return HttpResponseRedirect("/chatroom/{chatroomname}".format(chatroomname=chatroom_name))

    return render(request,'createChatroom_page.html')




def create_group(request):
    if not request.user.is_authenticated:
        return redirect('/signup')
    data={
        'users' : User.objects.filter().all()
    }
    # for i in data['users']:

    if request.method == 'POST' :
        group_name = request.POST['group_name']
        group_about = request.POST['group_about']
        newgroup = Group(group_name=group_name,group_about=group_about)
        newgroup.save()
        newgroupAdmin = Group_Admin_User(groupAdminUser_group_id=newgroup,groupAdminUser_owner=request.user)
        newgroupAdmin.save()

    return render(request,'createGroup_page.html',data)



def all_privateChatUser(request):
    if not request.user.is_authenticated:
        return redirect('/signup')

    # user = request.user
    # print(request.user.id)
    # privateUser = User_Profile.objects.filter(pk=user.id)
    # print(privateUser)
    # # for i in privateUser:
    # #     print(i.privatechat)
    if request.method == 'POST':
        pass

    return render(request,'index.html')



def chat_privateChat(request,private_username):
    if not request.user.is_authenticated:
        return redirect('/signup')

    username_private = User.objects.get(username=private_username)

    private_chats = Message.objects.filter(Q(message_from=request.user,message_to=username_private.id ) |
                                           Q(message_from=username_private.id,message_to=request.user) ).order_by('message_createTime')
    login_user = User.objects.get(pk=request.user.id)
    data = {
        'messages': private_chats,
        'login_user': login_user
    }
    if request.method == 'POST':
        message = request.POST['message']
        newchatroom = Message(message_from=request.user, message_text=message,message_to=username_private)
        newchatroom.save()

    return render(request,'privateChat_page.html',data)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        user = authenticate(request,username=username,password=passwd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/global/")    # / in front of 'global' is important else it will be
                                                       # webpage/login/global rather then webpage/global

    return render(request,'login_page.html')



def signupPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        passwd1 = request.POST['passwd1']
        passwd2 = request.POST['passwd2']
        print(username)
        if User.objects.filter(username=username).exists():
            return redirect('/login/')
        else:
            if passwd2 == passwd1:
                newuser = User(username=username,email=email,password=passwd1)
                newuser.save()
                login(request, newuser)
                return redirect('/global/')
            else:
                return redirect('/signup/')



    return render(request,'signup_page.html')


def demo(request,group_name):
    return render(request,'test_websocket.html',{'groupname':group_name})