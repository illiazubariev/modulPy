from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Product, Wallet, Purchase, Return



def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Wallet.objects.create(user=user, balance=10)
            return redirect('store')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def store(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            # Обработка случая, когда продукт не существует
            return redirect('failure')

        wallet = Wallet.objects.get(user=request.user)
        if wallet.balance >= product.price and product.stock >= 1:
            product.stock -= 1
            product.save() 
            wallet.balance -= product.price
            wallet.save() 
            Purchase.objects.create(user=request.user, product=product, quantity=1)
            return redirect('purchases')
        else:
            return redirect('failure')
    else:
        products = Product.objects.all()
        return render(request, 'store.html', {'products': products})
    

def purchases_list(request):
    if request.method == 'GET':
       purchases = Purchase.objects.filter(user=request.user)
       context = {'purchases': purchases}
       return render(request, 'purchases.html', context)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def failure_alert(request):
    return render(request, 'failure.html')