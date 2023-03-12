# python-django-first

pip install django

1.django-admin startproject 項目名稱

python manage.py runserver 啟動server
python manage.py 可以看到可以執行的指令


2.python manage.py startapp app01

settings.py 項目配置        常常操作
urls.py URL和函數的對應關係  常常操作
asgi.py 接收網路請求 異步
wsgi.py 接收網路請求 同步

manage.py 項目的管理 啟動項目 創建app 數據管理

3.python manage.py migrate 運行db.sqlite3 刪掉不在會自己創建


app01
      _init_.py   固定不用動 django 默認提供了admin後台管理
	admin.py	固定不用動 app啟動類
	migration	固定不用動 數據變更紀錄	
	models.py	重要 	    對數據庫操作	

4.快速上手
	1.確保app已註冊 [setting.py]
	2.編寫URL和視圖函數對應關係[urls.py]
	3.編寫視圖函數[views.py]
	4.python manage.py runserver 啟動server
4.2templates 模板

4.3靜態文件
在開發過程中一般將
	1.css
	2.js
	3.圖片
都會當作靜態文件處理
5.模板語法

第三方模塊:requests (pip install requests)

improt requests
res = requests.get()
data = res.json()
print(data)

6.https://docs.djangoproject.com/en/4.1/ref/csrf/
類似同源

7.數據庫操作
MySQL+pymysql

Django開發操作數據庫，使用orm框架
pip install mysqlclient
7.2 在[settings.py]文件中進行配置和修改
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'python_db',
         'USER':'root',
         'PASSWORD':'st923420',
         #127.0.0.1 
         'HOST':'localhost',
         'PORT':'3306'
     }
}
7.3
django 操作表

1.創建表
2.刪除表
3.修改表
創建表:
在[models.py]文件中:
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
持行命令: app01要註冊
python manage.py makemigrations
python manage.py migrate
添加新列 可以為空 或是給他值 有3種選擇 1.手動輸入值 2.設默認值 age = models.3.給空值
age = models.IntegerField(default=2)
data = models.IntegerField(null=True,blank=True)

以後在開發中如果想要對表格結構做調整
在[models.py]文件操作類即可
命令一樣
python manage.py makemigrations
python manage.py migrate
<<<<<<< HEAD

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

#案例:用戶管理+連接API

1.展示用戶列表
    --url
    --函數
2.添加用戶
    --url
    --函數
    GET 看到頁面輸入內容
    POST 提交，寫入到數據庫

###第三方庫下載
pip list 可以看當前環境下的第三方庫
pip freeze > requirements.txt 把第三方庫的環境輸出到 requirements.txt
pip freeze --local > requirements.txt 將當前的第三方庫資訊輸出道requirements.txt
pip install -r requirements.txt 下載第三方庫