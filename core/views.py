from django.shortcuts import render, redirect
from pathlib import Path
from django.conf import settings
from products.forms import OrderRequestForm
from products.models import Product


def home_view(request):
    popular_products = Product.objects.filter(
        name__in=[
            "Бочка 1000л круглая 2-слойная",
            "Бочка 1000л круглая 1-слойная",
            "Бочка 550л круглая 2-слойная"
        ]
    )
    return render(request, 'core/home.html', {
        'popular_products': popular_products
    })


def contacts_view(request):
    form = OrderRequestForm()
    if request.method == 'POST':
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.product = None  # заявка не привязана к товару
            contact.save()
            return redirect('contacts')  # перезагрузка или сообщение "Спасибо"

    return render(request, 'core/contacts.html', {'form': form})


def about_view(request):
    open_dir = Path(settings.STATICFILES_DIRS[0]) / 'images' / 'open'
    static_images = sorted([
        f'images/open/{file.name}'
        for file in open_dir.glob('*')
        if file.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp'}
    ])
    return render(request, 'core/about.html', {'static_images': static_images})


