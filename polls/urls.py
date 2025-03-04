'''
■urls.pyの役割
urls.pyは、DjangoのURLルーティングを行う。
つまり、URLをビュー関数に紐づけるコードを書いている。

■from django.urls import
→これは,
Djangoのおpath関数をインポートしている。
これは、URLパターンを定義するための関数。

■from . import views
→同じアプリ内、（ . はカレントディレクトリ）のview.pyをインポートしている。
→views.pyに定義されたビュー関数（例:index）を使用するために必要

■urlpatterns
URLパターンリスト。
Djangoがクライアント（ユーザー）のリクエストURLを処理する際に、ここで定義されたルールを基に、適切なビュー関数を呼び出す。

■path('', view.index, name='index')
>''→URLが何も指定されていない場合
（http://example.com/やhttp://lofalhost:800/）
>view.index
→view.pyにあるindex関数を実行。
>name='index'
→このURLパターンに"index”という名前をつける。
→(テンプレートやreverse()関数で便利)

■revers()関数とは
→Djangoのreverse()関数は、URLパターンの「名前（name）」から十歳のURLを取得するための関数。
→通常、Djangoのpath()でnameを設定している場合、reverse()を使うとそのURLを動的に取得できる。これにより、ハードコーディング（URLを直接記述すること）を避けることができる。

■urls.pyにpath()コードを入力することで、viewとpolls.urlsモジュールを結びつける。

■path('url', views.メソッド名, nameオプション)
'''

# from django.urls import path

# from . import views

# ■URLの名前空間
# →mysite内に複数アプリを作ることができるため、どのアプリでのリンクか区別する必要がある。そこで、app_nameを定義する必要がある。

# app_name = 'polls'
# urlpatterns = [
#     # 例:/polls/
#     path('', views.index, name='index'),
#     # 例:/polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # 例:/polls/5/results/
#     path('<int:question_id>/results/', views.resulte, name='results'),
#     # 例:/polls.5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('<int:question_id>/', views.detail, name='detail'),
# ]

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
