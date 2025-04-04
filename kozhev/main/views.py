from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    DetailView, ListView, TemplateView
)

from main.constants import PAGINATION_NUM
from main.forms import ApplicationForm
from main.models import Product
from main.service import filter_products
from main.tasks import send_application_email


class IndexListViews(ListView):
    model = Product
    paginate_by = PAGINATION_NUM


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'post_pk'
    template_name = 'main/product_detail.html'

    def get_object(self):
        return get_object_or_404(filter_products(
            Product.objects.all()),
            pk=self.kwargs.get(self.pk_url_kwarg)
        )


class About(TemplateView):
    template_name = 'pages/about.html'


class Delivery(TemplateView):
    template_name = 'pages/delivery.html'


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def error_500(request):
    return render(request, 'pages/500.html', status=500)


def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Заявка от {name}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAILS]
            send_application_email.delay(email, message, subject, from_email, recipient_list)

            return render(request, 'main/application.html')
    else:
        form = ApplicationForm()

    context = {'form': form}
    return render(request, 'main/application.html', context)
