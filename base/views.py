from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Order
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Order

def order_edit(request, pk):

    order = get_object_or_404(Order, pk=pk)

    form = OrderForm(
        request.POST or None,
        instance=order
    )

    if form.is_valid():

        form.save()

        return redirect('base:orders')

    return render(request, 'order_form.html', {
        'form': form,
        'order': order
    })

def orders_list(request):

    orders = Order.objects.all().order_by('-created_at')

    search = request.GET.get('search')
    status = request.GET.get('status')
    payment = request.GET.get('payment')

    # 🔍 Поиск по имени/заказу/телефону
    if search:
        orders = orders.filter(
            Q(client_name__icontains=search) |
            Q(order_type__icontains=search) |
            Q(phone__icontains=search)
        )

    # 📦 Фильтр статуса
    if status:
        orders = orders.filter(status=status)

    # 💰 Фильтр оплаты
    if payment:
        orders = orders.filter(payment_status=payment)

    context = {
        'orders': orders
    }

    return render(request, 'orders.html', context)

class Main(TemplateView):
    template_name = 'main.html'

from django.shortcuts import render, redirect
from .forms import OrderForm

def order_create(request):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('base:orders')

    return render(request, 'order_form.html', {
        'form': form,
        'is_edit': False
    })

def order_delete(request, pk):

    order = get_object_or_404(Order, pk=pk)

    order.delete()

    return redirect('base:orders')