"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''

■from django.contrib import admin
→Djangoの管理サイト（Django admin)を使うためのadminモジュールをインポート。
→Djangoにはデフォルトで管理画面（Django Admin）が用意されており、これを利用するためには、admin.site.urlsをurlpatternsに追加する必要がある。

■from django.urls import include
→includeは、pathとは別のURL設定ファイル（他のアプリのurls.py）を取り込むための関数。

■path('admin/', admin.site.urls),
>admin/
→http://localhost:8000/admin/ にアクセスしたときに Django の管理画面を表示するためのルート。
>admin,site.urls
→Djangoの管理サイト（Django Admin）のURLパターンを定義したもの。これを、urlpatternsに追加することで、管理画面が利用可能になる。

'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
