import random
from django.http import HttpResponse

# def home_view(request):
#     print("這是home view的邏輯實現部分")
#     name ="潘小明"
#     number = random.randint(0,9999)
#     return HttpResponse(f"<h1>hello {name} -- {number} </h1>")


def home_view(request):
    print("這是home_view的邏輯")
    name = "潘小明"
    number = random.randint(0, 9999)
    h1_html = f"<h1>hello {name} -- {number}!</h1>"
    p_html = f"<p>hello {name}-- {number}!</p>"

    responst_content = h1_html+ p_html

    return HttpResponse(responst_content)
