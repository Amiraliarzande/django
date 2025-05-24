from django.http import HttpResponse , JsonResponse
def http_test(request):
    return HttpResponse("<h1>manmarket.ir</h1>")

def json_test(request):
    data = {
        "name": "manmarket.ir",
        "description": "A platform for buying and selling products.",
        "version": "1.0.0"
    }
    return JsonResponse(data)