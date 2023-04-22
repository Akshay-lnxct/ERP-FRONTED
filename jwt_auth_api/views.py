from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST', ])
def register(request):
    try:
        data = request.data 

        username = data['username']
        email = data['email']
        password = data['password']

        User.objects.create_user(username= username, email= email, password= password).save()

        return JsonResponse({"message": "Register SuccessFully"})

    except Exception as e:
        return JsonResponse({"error": str(e)})


@api_view(['GET', ])
def login(request):
    try:
        data = request.data 
        email_ = data['email']
        password_ = data['password']

        user = User.objects.get(email= email_)
        if not user:
            return JsonResponse({"message": "Email not Found"})

        try:
            get_user_id = User.objects.get(email=email_, password=password_)
            return JsonResponse({
                "message": "Login successfully",
                "id": get_user_id.id
            })

        except Exception as e:
            return JsonResponse({"error": "Invalid Credentionals "}) 

    except Exception as e:
        return JsonResponse({"error": str(e)})