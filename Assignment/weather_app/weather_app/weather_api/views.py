from django.shortcuts import render
from django.http import JsonResponse,Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


def weather_view(request, city):
    if city in weather_data:
        return JsonResponse(weather_data[city])
    else:
        raise Http404("City not found")
    

@csrf_exempt
def weather_list(request):
    if request.method == 'POST':
        new_data = request.POST.dict()
        city = new_data.pop('city')
        weather_data[city] = new_data
        return JsonResponse(weather_data[city], status=201)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def weather_detail(request, city):
    if city in weather_data:
        if request.method == 'GET':
            return JsonResponse(weather_data[city])
        elif request.method == 'PUT':
            updated_data = request.PUT.dict()
            weather_data[city].update(updated_data)
            return JsonResponse(weather_data[city])
        elif request.method == 'DELETE':
            del weather_data[city]
            return HttpResponse(status=204)
    else:
        raise Http404("City not found")  