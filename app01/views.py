from django.shortcuts import render, HttpResponse ,redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#json格式發回去的方式
from django.core import serializers
# from django.http import HttpResponse

def index(request):
    return HttpResponse("歡迎使用")

# def user_list(request):
#     return HttpResponse("用戶列表")
# 1.(根據app的註冊順序，逐一去他們的templates目錄中找) 優先去跟目錄找 不配置就無效
# 2.去app目錄下的templates目錄尋找user_list.html


def user_list(request):
    return render(request, "user_list.html")

# def user_add(request):
#     return HttpResponse('添加用戶')


def user_add(request):
    return render(request, "user_add.html")


def something(request):
    # requestt是一個對象，封裝了用戶發送過來的內容

    # 1.獲取請求方式 GET/POST
    print(request.method)

    # 2.在url上傳遞值 /something/?n1=123&n2=999
    print(request.GET)

    # 3.在請求體中提交數據
    print(request.POST)
    # 4.HttpResponse("返回內容")
    # return HttpResponse("返回內容")
    # 5.讀取HTML的內容 +渲染(替換)
    return render(request, "something.html", {"title": "來了"})
    # 6.[redirect]
    # return redirect("https://tw.yahoo.com/#")

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
        #return redirect("https://tw.yahoo.com/#")
    else:
        #如果是POST請求，獲取或用提交的數據
        # print(request.method)
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username =='admin' and password =='123':
            return HttpResponse("登陸成功")
        else:
            return render(request, "login.html",{"error_msg":"用戶名或密碼錯誤"})
from app01.models import UserInfo,Department
def orm(request):
    #測試ORM操作標中的數據
    # 1.新增
    # Department.objects.create(title="銷售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="運營部")
    # UserInfo.objects.create(name="admin",password="123456",age="18" )
    #2.刪除
    # Department.objects.filter(id=2).delete()
    # Department.objects.all().delete()
    #3.查詢數據
    #data_list = [物件，物件] QuerySet類型
    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password,obj.age)
    
    # data_list = UserInfo.objects.filter(id=1)
    # print(data_list)
    #取到的只有一行

    #另外一種寫法 獲取第一條數據
    # row_obj =  UserInfo.objects.filter(id=1).first()
    # print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)

    #4.更新數據
    # UserInfo.objects.all().update(age=28)
    UserInfo.objects.filter(id=1).update(age=18)


    return HttpResponse("成功")
@csrf_exempt
def info_list(request):
    #1.獲取數據庫中所有的用戶信息
    #[物件，物件，物件]
    data_list = UserInfo.objects.all()
    print(data_list)

    return render(request,"info_list.html",{"data_list":data_list})
    # data = serializers.serialize('json', data_list)
    # return HttpResponse(data, content_type='application/json')

@csrf_exempt
def info_add(request):
    if request.method=="GET":
        return render(request,'info_add.html')
    #獲取用戶提交的數據
    user = request.POST.get("user")
    pwd = request.POST.get("password")
    age = request.POST.get("age")

    #添加到數據庫
    UserInfo.objects.create(name=user,password=pwd,age=age)
    #return HttpResponse("添加成功")

    return redirect('http://127.0.0.1:8000/info/list/')