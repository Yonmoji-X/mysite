# from django.shortcuts import render


'''
■HttpResponseは、DjangooがHTTPレスポンスをクライアント（ブラウザ）に返すためのクラス。

■requestは、DjangoのHttpRequestオブジェクトで、ブラウザから送られてきたリクエスト情報（GET, POSTデータなど）を含む。

■ブラウザにHello, world. You're at the polls index.というテキストを含むHTTPレスポンスを返す。

■HTTPレスポンス：
webサーバーがブラウザからのおリクエスト(HTTPリクエスト)を受け取った後に送る「応答（レスポンス）」

■Djangoのビュー関数
→リクエストを受け取り、レスポンス(HttpResponse)を返す。
→それぞれの関数は、URLから受け取ったquestion_idでテキストを表示する。

■def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)
>question_id = 3の時
→/polls/3/
→"You're looking at question 3."を表示

■%s フォーマット
>「%s」は文字列のどこに埋め込むかを意味するプレースホルダー
>% 変数 の部分に描かれた変数を代入する（ここではquestion_id)
>実例
return HttpResponse("You're looking at question %s." %  question_id)
→question_id = 3の場合
→表示："You're looking at question 3."

■リスト内包表記→for文は下記のように書ける。
>リストなし
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
  squares.append(num ** 2)
print(squares) #[1, 4, 9, 16, 25]
↓
>リスト内包表記
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

■index関数について。
→htmlのテンプレートを取得
→context（テンプレートに埋め込むデータ）を入れる。
→render()でレンダリング
→レンダリング結果をHttpResponseで返す。

>latest_qurstion_list = Question.objects.order_by('-pub_date')[:5]
→pub_date（公開日）が新しい順に並べる。
→[:5] 最新のお5件のみ取得

>output = ', '.join([q.question_text for q in latest_question_list])
→output = []の配列に、latest_qurstion_listからq.question_textを入れていく。
>', '.joinで、output配列を、","区切りで、一つの文字列に変換する。

>template = loader.get_tetmplatte('polls/index.html')
→polls/templates/polls/index.htmlをロード
→Djangoのloader.get_template()を持ちいてHTMLテンプレートを取得

>context = {'latest_question_list: latest_qurstion_list,}
→contextとは、テンプレートに渡すデータの辞書型オブジェクト
→latest_question_list には、最新の質問リスト5件を取得している。

>return HttpResponse(template.render(context, request))
→.render(context,request)
→contextのデータをpolls/index.htmlに適応させ、HTMLを生成（レンダリング）
→HttpResponse()で最終的に生成されたHTMLをレスポンスと知ってブラウザに返す。

reverse
→URLのパターンの名前からURLを生成するための関数

pk
→Primary Key
モデル（データベース）の各インスタンス（行）を識別するID



>
'''
  # ----------------------------------------------------
# from django.http import HttpResponse
# from django.http import Http404
# from django.template import loader
# from django.shortcuts import render
  # ----------------------------------------------------
  # return HttpResponse("Hello, world. You're at the polls index.")
  # latest_question_list = Question.objects.order_by('')
  # ----------------------------------------------------
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)
  # ----------------------------------------------------
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
  # ----------------------------------------------------
  # HttpResponseをimportしない方法
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
  # ----------------------------------------------------
# def resulte(request, question_id):
#   response = "You're looking at the resulte of question %s."
#   return HttpResponse(response % question_id)

# ||||||||||||||||||||||||||||||||||||||||||||||||||
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

# from .models import Choice, Question

# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   context = {'latest_question_list': latest_question_list}
#   return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/detail.html', {'question':question})


# def resulte(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html',{'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# ||||||||||||||||||||||||||||||||||||||||||||||||||# ||||||||||||||||||||||||||||||||||||||||||||||||||
"""
Django における モデル (Model) ：データベースのテーブルの構造を定義するクラス
"""

# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render #エラー表示かviewレンダリング
# from django.urls import reverse #urlpattarnsのnameからURL生成する関数
# from django.views import generic #Django汎用view利用のためのモジュール
# from .models import Choice, Question

# class IndexView(generic.ListView): #汎用viewのクラスベースView
#   """
#   generic.ListView
#   →Djangoが提供する汎用viewの一つ
#   →データベースのレコードをリスト表示する。
#   """
#   #このViewがレンダリングするtemplateの名前指定
#   template_name = 'polls/index.html'
#   # viewで取得したデータをtemplateで使うための変数。
#   context_object_name = 'latest_question_list' #

#   def get_queryset(self):
#     """
#     viewがデータを表示するか決める関数
#     直近5つの公開された質問を返す（表示する）
#     """
#     return Question.objects.order_by('-pub_date')[:5]

#   class DetailView(generic.DetailView): # Djangoの汎用View
#     """
#     generic.DetailView
#     →特定のモデルの詳細viewを作成するクラス
#     """
#     # このviewが表示するデータのモデルを指定
#     model = Question
#     # このviewがレンダリングするtamplateの名前指定
#     template_name = 'polls/results.html'

# class ResultsView(generic.DetailView):
#   model = Question
#   template_name = 'polls/results.html'


  # ----

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# データベース内のデータをリストとして、表示するクラス。
class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """最新5件を返す"""
    return Question.objects.order_by('-pub_date')[:5]

# データベース内の詳細viewを返すクラス。
class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls.detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question':question})
