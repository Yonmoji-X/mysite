# from django.shortcuts import render

from django.http import HttpResponse
'''
■HttpResponseは、DjangooがHTTPレスポンスをクライアント（ブラウザ）に返すためのクラス。

■requestは、DjangoのHttpRequestオブジェクトで、ブラウザから送られてきたリクエスト情報（GET, POSTデータなど）を含む。

■ブラウザにHello, world. You're at the polls index.というテキストを含むHTTPレスポンスを返す。

■HTTPレスポンス：
webサーバーがブラウザからのおリクエスト(HTTPリクエスト)を受け取った後に送る「応答（レスポンス）」
'''

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")


