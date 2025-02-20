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
'''

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
