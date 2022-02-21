from django.shortcuts import render, redirect
from django.http import HttpResponse # モジュールの読み込み
from .forms import ImageForm, LoginForm, SignUpForm # 追加
from django.contrib.auth import login, authenticate # 追加
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required # 追加
from django.conf import settings
from .models import ModelFile
from .forms import ImageForm
from django.views.generic import ListView
import joblib
import numpy as np
import torch
#import iPERCore.iPERCore.services.run_imitator
import subprocess

# GPU上で保存された重みをCPU上で読み込む場合
# load_path = 'model/personalized.pth'
# load_weights = torch.load(load_path, map_location={'cuda:0': 'cpu'})
# loaded_model = model.load(load_weights)
#loaded_model = model.load_state_dict(load_weights)
#loaded_model = joblib.load(load_path)

@login_required
def index(request):
    return render(request, 'django_app/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            # 読み取った情報をログインに使用する情報として new_user に格納
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                # new_user の情報からログイン処理を行う
                login(request, new_user)
                # ログイン後のリダイレクト処理
                return redirect('index')
            
    # POST で送信がなかった場合の処理
    else:
        form = SignUpForm()
    
    return render(request, 'django_app/signup.html', {'form': form})

# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'django_app/login.html'

# ログアウトページ
class Logout(LogoutView):
    template_name = 'django_app/base.html'

# @login_required
# class ImageList(ListView):
#     template_name = 'django_app/list.html' # template_name='表示するhtmlファイル'
#     model = ModelFile

@login_required
def img_list(request):
    imgs = ModelFile.objects.all()
    return render(request, 'django_app/list.html', {'imgs': imgs})


@login_required
def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_name = request.FILES['image']
            img_url = '../media/documents/{}'.format(img_name)
            return render(request, 'django_app/image.html', {'img_url':img_url})    
    # POST で送信がなかった場合の処理
    else:
        form = ImageForm()
        return render(request, 'django_app/upload.html', {'form': form})


@login_required
def result(request):
    #if request.method == 'POST':
        #result = subprocess.run(['python -m'], stdout=iPERCore.services.run_imitator)
    return render(request, 'django_app/result.html') #, {'mv_url': result.returncode})