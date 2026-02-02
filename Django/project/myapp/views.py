from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import JsonResponse
from django.urls import reverse_lazy

from .models import Item
from .forms import ContactForm


class HomeView(generic.TemplateView):
    template_name = 'myapp/home.html'


class ItemListView(generic.ListView):
    model = Item
    template_name = 'myapp/item_list.html'
    context_object_name = 'items'
    paginate_by = 10


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'myapp/item_detail.html'


class ItemCreateView(generic.CreateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'myapp/item_form.html'


class ItemUpdateView(generic.UpdateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'myapp/item_form.html'


class ItemDeleteView(generic.DeleteView):
    model = Item
    template_name = 'myapp/item_confirm_delete.html'
    success_url = reverse_lazy('myapp:item-list')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: send email or store message
            return redirect('myapp:home')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})


def api_items(request):
    items = list(Item.objects.values('id', 'name', 'description', 'created_at'))
    return JsonResponse({'items': items})
