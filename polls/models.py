'''
from django.db import models
→django.db.modelsモジュールインポート

モデル（クラス）
→データベースの構造を定義するクラス
レコード
→モデルクラスのインスタンス

Questionクラス
→Djangoのセータベースのテーブル
→django.db.models.Modelを継承
→データベースモデルとして動作

>CharField(max_length=200)
→最大200文字の文字列を保存するフィールド

>DateTimeField('dattet publishd')
質問(Question)が公開された日時を保存するフィールド

Choice クラス
Django.db.models.Modelを継承
>question=models.ForeignKey(Question, on_delete=modeles.CASCADE)
>>models.ForeignKey
→Questionモデルへの外部キー
→一つの質問(Question)に対して、複数の選択肢(Choice)を関連付けるためにキーを使用する。
>>CASCADE
→親モデル（レコード）が削除された際に、子モデル（レコード）も削除全て削除するForeignKeyに設定する外部キー制約
>>on_dalete=models.CASCASE
親のQuestionレコードが削除されたら、それに紐づくChoiceレコードも削除


【コメント】
>モデルクラスはデータベースのテーブル自体を定義するクラス。
>Question、Choiceクラスは、データベースの一つのテーブルを定義するクラスで、クラス内で定義しているのは、列（フィールド）の定義。
つまり
>Questionクラス→「questions」テーブル
>>question_text→「質問内容」を格納するカラム
>>pub_date→「公開日」を格納するカラム
>Choiceクラス
>>choice_textz→「選択肢の内容」を格納するカラム
>>votes→「投票数」を格納するカラム
>>question→「Question」テーブルとの外部キー。
  →関連（リレーション）を格納


■def __str__(self)の意味
>__str__は、Pythonにおいて、オブジェクトを文字列として表現するためのメソット
>オブジェクトをprint()したり、管理画面(
  Django Admin）で表示したりするときに使われる文字列をカスタマイズできる。
>__str__がない場合、<QuerySet [<Question: Question object (1)>]>のような形で表示される。
→__str__がある場合、<QuerySet [<Question: What's new?>]>のように、文字列が表示される。
)

■def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
>Questionのpub_date（公開日時）が過去1日以内かどうか判定する。
→1日以内ならTrue、それ以前ならFalse
→最近公開された質問のみ表示したい時などにつかう。
>timezone.now()
→現在日時を取得する関数
→Djamgoのタイムゾーン設定に対応した現在日時を返す。
>datetime.timedelta(days=1)
→今日、1日分の時間を表す
>timezone.now() - datetime.timedelta(days=1)
→昨日の今の時刻 = これまでの日時 - 今日1日分の時間
>self.pub_date
→Questionの公開日時
>self.put_data >= timezone.now() - datetime.timedelta(days=1)
→Questionの公開日時 >= 昨日の今の時刻 を判定
→Questionが今日一日中に投稿されたか。
→このQuestionが一日以内に公開されたか。
'''
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
  question = models.ForeignKey(Question,on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text
