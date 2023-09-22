from django.http import HttpResponse
import datetime

# Create your views here.
def v1(request):
    n = datetime.datetime.now()
    seg = n.second
    rest = HttpResponse("<h1>Justo en este segundo se paró, si pones F5, cambia el segundo</h1>" % seg)
    return rest

def v2(request):
    n2 = datetime.datetime.now()
    seg2 = n2.second
    rest2 = HttpResponse("<h1>Justo en este segundo se paró, si pones F5, cambia el segundo</h1>" % seg2)
    return rest2