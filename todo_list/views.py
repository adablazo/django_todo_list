from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, EditForm

def home(request):
    return render(request, 'home.html', {"user":"adablazo"})
def about(request):
    my_name = "Adrian Ablazo"
    context = {'myname': my_name}
    return render(request, 'about.html', context)
def contact(request):
    return render(request, 'contact-us.html', {"user": "adablazo"})

def listings(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all() # select * from List;
            context = {'all_items': all_items, 'user':'adablazo'}
            return render(request, 'listings.html', context)
    else:
        all_items = List.objects.all() # select * from List;
        context = {'all_items': all_items, 'user':'adablazo'}
        return render(request, 'listings.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id) # select * from List where pk == list_id;
    item.delete() #delete from List where pk == list_id
    return redirect('listings')

def strike(request, list_id):
    item = List.objects.get(pk=list_id) # select * from List where pk == list_id;
    item.completed = True # update List set completed = True where pk == list_id;
    item.save() # executes the update to the db
    return redirect('listings')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id) # select * from List where pk == list_id;
    item.completed = False # update List set completed = False where pk == list_id;
    item.save() # executes the update to the db
    return redirect('listings')

def edit(request, list_id):
    if request.method == 'POST':
        list_item = List.objects.get(pk=list_id)
        form = EditForm(request.POST or None)
        if form.is_valid():
            updated_item = form.cleaned_data.get('item')
            list_item.item = updated_item
            list_item.save()
            return redirect('listings')
    else:
        list_item = List.objects.get(pk=list_id) # select * from List;
        context = {'list_id': list_id, 'list_item':list_item}
        return render(request, 'edit.html', context)



        
