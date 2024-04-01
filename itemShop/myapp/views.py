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
        product = Product.objects.get(id=product_id)
        wallet = Wallet.objects.get(user=request.user)
        if wallet.balance >= product.price:
            wallet.balance -= product.price
            wallet.save()
            # Здесь можно добавить логику для обработки покупки товара
            return redirect('success')
        else:
            return redirect('failure')
    else:
        products = Product.objects.all()
        return render(request, 'store.html', {'products': products})