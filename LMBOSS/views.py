from django.shortcuts import render
from django.views import generic
from LMBOSS.models import PhoneNum


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'LMBOSS/index.html'
    context_object_name = 'phone_numbers'

    def get_queryset(self):
        """Return all phone numbers."""
        # return Question.objects.order_by('-pub_date')[:5]
        return PhoneNum.objects.all()


class DetailView(generic.DetailView):
    model = PhoneNum
    template_name = 'LMBOSS/detail.html'
