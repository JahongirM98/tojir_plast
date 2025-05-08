from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductFormType
from .forms import OrderRequestForm
from django.db.models import Q
import random

def catalog_view(request):
    query = request.GET.get('q')
    layer_filters = request.GET.getlist('layers')
    volume_filters = request.GET.getlist('volumes')
    form_type_filters = request.GET.getlist('form_type')

    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query) | Q(volume__icontains=query))

    if layer_filters:
        products = products.filter(layers__in=layer_filters)

    if volume_filters:
        products = products.filter(volume__in=volume_filters)

    if form_type_filters:
        products = products.filter(form_type__name__in=form_type_filters)

    return render(request, 'products/catalog.html', {
        'products': products
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = OrderRequestForm()

    if request.method == 'POST':
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('product_detail', pk=pk)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'form': form,
        'images': product.images.all()
    })
