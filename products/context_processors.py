from .models import Product, ProductFormType

def product_filter_data(request):
    available_volumes = Product.objects.order_by('volume').values_list('volume', flat=True).distinct()
    available_form_type = ProductFormType.objects.order_by('name').values_list('name', flat=True).distinct()

    selected_volumes = request.GET.getlist('volumes')
    selected_form_types = request.GET.getlist('form_type')
    selected_layers = request.GET.getlist('layers')

    return {
        'available_volumes': available_volumes,
        'available_form_type': available_form_type,
        'selected_volumes': selected_volumes,
        'selected_form_types': selected_form_types,
        'selected_layers': selected_layers,
    }
