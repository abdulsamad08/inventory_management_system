from django.shortcuts import render

# def userlogin(request):
#     return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def productList(request):
    return render(request, 'product/list.html')


def productadd(request):
    return render(request, 'product/add.html')

def productgrid(request):
    return render(request, 'product/grid.html')

def productdetails(request):
    return render(request, 'product/details.html')

def productedit(request):
    return render(request, 'product/edit.html')


def categorieslist(request):
    return render(request, 'categories/list.html')

def categoriesadd(request):
    return render(request, 'categories/add.html')

def categoriesedit(request):
    return render(request, 'categories/edit.html')


# orders
def orderslist(request):
    return render(request, 'orders/list.html')

def orderinvoices(request):
    return render(request, 'orders/invoices.html')

def ordersdetails(request):
    return render(request, 'orders/details.html')


# customers
def customersdetails(request):
    return render(request, 'customers/details.html')
