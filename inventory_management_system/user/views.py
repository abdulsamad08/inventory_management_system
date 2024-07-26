from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import User
import json
from django.core.exceptions import ValidationError
from django.db import IntegrityError

@csrf_exempt
@require_http_methods(["POST"])
def createuser(request):
    try:
        data = json.loads(request.body)
        user_firstname = data.get('firstname')
        user_lastname = data.get('lastname')
        user_email = data.get('email')
        user_password = data.get('password')
        user_date_of_birth = data.get('date_of_birth')
        user_phone_number = data.get('phone_number')

        # Validate required fields
        if not all([user_firstname, user_lastname, user_email, user_password]):
            return JsonResponse({'success': False, 'message': 'Missing required fields'}, status=400)

        # Create the user
        user = User.objects.create(
            first_name=user_firstname,
            last_name=user_lastname,
            email=user_email,
            password=user_password,
            date_of_birth=user_date_of_birth,
            phone_number=user_phone_number
        )
        
        response_data = {
            'success': True,
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'date_of_birth': user.date_of_birth,
            'phone_number': user.phone_number
        }
        
        return JsonResponse(response_data, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)
    except ValidationError as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)
    except IntegrityError:
        return JsonResponse({'success': False, 'message': 'email should be unique'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': 'An unexpected error occurred', 'details': str(e)}, status=500)
    

# get all users
# def getcustomers(request):
#     if request.method == 'GET':
#         customers = User.objects.all()

#         customer_list = list(customers.values('id', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number'))
        # return JsonResponse(customer_list, safe=False, status=200)

#         print(customer_list)
#         return render(request, 'templates/customers/list',{'customers' : customer_list})

#     return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def getcustomers(request):
    
    # if request.method == 'GET':
    print("get_customers view called")
    try:
        customers = User.objects.all()
        customer_list = list(customers.values('id', 'first_name', 'last_name', 'email'))
        return render(request, 'customers/list.html', {'customers': customer_list})
    except Exception as e:
        print(f"Error fetching customers: {e}")
        return JsonResponse({'success': False, 'message': 'Error fetching customers'}, status=500)
    

@csrf_exempt
def deletecustomers(request, id):
    if request.method == 'DELETE':
        customers = User.objects.get(id=id)
        customers.delete()
        return JsonResponse({'success': True, 'message': 'Customer Deleted Successfully'}, status=200)

