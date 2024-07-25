from django.shortcuts import render
from django.views import View


# Create your views here.
class UserView(View):
    userview = "User view"

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

    def fetch(self, request):
        pass