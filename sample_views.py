"""Django の views に対応するようなファイル"""
from django.http.request import HttpRequest
from django.shortcuts import render

from sample_forms import SampleForm
from sample_predict import sample_predict


def index(request: HttpRequest):
    """入力をもとに推論をし、結果を表示する view. template は適宜いい感じしてみてください。"""
    if request.method == "POST":
        # POST の場合は form のデータを取得して、推論し、その結果を返す
        form = SampleForm(request.POST)
        if not form.is_valid():
            # form の内容が is_valid であればエラー用のページを表示する
            return render(request, "validation_error.html", {"errors": form.errors})
        # 推論を行う
        output = sample_predict(form.keyword)
        # 推論の結果を template に受け渡す
        render(request, "result.html", {"result": output})
    # GET の場合は入力フォームが表示されるようにしてあげる
    return render(request, "form.html")
