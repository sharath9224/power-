from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import psutil 

@csrf_exempt
def index(request):
    return render(request,'index.html')
def power_consumption(request):
    if request.method == 'POST':
        application_pid = int(request.POST.get('pid'))
        process = psutil.Process(application_pid)
        try:
            power_info = process.power_info()
            return JsonResponse(power_info)
        except psutil.AccessDenied:
            return JsonResponse({'error': 'Access denied. Make sure you have sufficient privileges.'}, status=403)
