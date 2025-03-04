# 公式

https://docs.djangoproject.com/ja/3.0/intro/tutorial01/

https://blog.codecamp.jp/programming-python-django

## 仮想環境

$ python --version
→3.10.6
$ django-admin --version
→5.1.6

仮想環境名
→myenv1

仮想環境起動
$ source myenv1/bin/activate

仮想環境終了
$ deactivate

## サーバーの起動と終了

起動（ポート番号はデフォルト 8000。）
$ python manage.py runserver 8000

終了
CONTROL+C

マイグレート
→ モデルの変更を反映。
$ python manage.py makemigrations polls

マイグレーションで実行された SQL コマンドの確認
$ python manage.py sqlmigrate polls 0001

モデルの変更をデータベースに反映
$ python manage.py migrate

シェル起動
$ python manage.py migrate

データベース管理画面
http://127.0.0.1:8000/admin/login/?next=/admin/

パスワードの生成
python manage.py createsuperuser

> > user 名:admin
> > メール:yonmoji.x0505@gmail.com
> > pass:Takayama0505

テンプレートとして認識される、ファイル作成コマンド
※ルートディレクトリで行う。(mysite)
mkdir -p polls/templates/polls
touch polls/templates/polls/index.html
→-p はすでに存在する場合は無視。

## 進捗

その 5
