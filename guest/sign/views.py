from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event
# Create your views here.
def index(request):
    return render(request, "index.html")

# 登录处理
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        # if username == '123' and password == '456':
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600) #添加cookie
            request.session['user'] = username  # 添加session
            return response
        else:
            return render(request, 'index.html', {'error': "登录名或密码有错误"})

# 会议管理页面处理
@login_required  # 登录限制，无法直接输入地址访问，必须登录
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # cookies的读取
    event_list = Event.objects.all()
    username = request.session.get('username', '')
    return render(request, "event_manage.html", {"user": username, "events": event_list})
