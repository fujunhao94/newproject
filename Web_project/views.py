from django.shortcuts import render     # 创建应用时自动导入的模块
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):   # request封装了用户请求的所有内容
    return render(request, 'home.html')


