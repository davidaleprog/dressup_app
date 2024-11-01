# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Outfit
from .forms import ItemForm, OutfitForm

# view to display all items in the database
def item_list(request):
    items = Item.objects.all() # get all items from the database
    return render(request, 'dressup_app/index.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'dressup_app/detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'dressup_app/create.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'dressup_app/update.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')

def outfit_list(request):
    outfits = Outfit.objects.all() # get all outfits from the database
    return render(request, 'dressup_app/outfits.html', {'outfits': outfits})

def outfit_detail(request, pk):
    outfit = get_object_or_404(Outfit, pk=pk)
    return render(request, 'dressup_app/outfit_detail.html', {'outfit': outfit})

def outfit_create(request):
    if request.method == 'POST':
        form = OutfitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outfit_list')
    else:
        form = OutfitForm()
    return render(request, 'dressup_app/outfit_create.html', {'form': form})

def outfit_update(request, pk):
    outfit = get_object_or_404(Outfit, pk=pk)
    if request.method == 'POST':
        form = OutfitForm(request.POST, instance=outfit)
        if form.is_valid():
            form.save()
            return redirect('outfit_list')
    else:
        form = OutfitForm(instance=outfit)
    return render(request, 'dressup_app/outfit_update.html', {'form': form})

def outfit_delete(request, pk):
    outfit = get_object_or_404(Outfit, pk=pk)
    outfit.delete()
    return redirect('outfit_list')