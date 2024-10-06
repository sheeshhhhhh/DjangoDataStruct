from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Message
import json


# Create your views here.
@csrf_exempt
def sendMessage(request):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)
    

            if data["message"] == "":
                return JsonResponse({ "status" : "fail", "error" : "message is empty" }, status=400)

            message = Message(
                name = data['name'],
                contacts = data['contact'],
                message = data['message']
            )

            message.save()

            return JsonResponse({ "status" : "success", "message" : "Message sent successfully"}, status=200)
        except Exception as error: 
            print("Error: ", error)
            return JsonResponse({ "status" : "fail", "error" : "Internal Server Error" }, status=500)