from django.shortcuts import render, redirect, get_object_or_404
from .models import Borrower
from .forms import BorrowerForm

def add_borrower(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrower_list')
    else:
        form = BorrowerForm()
    return render(request, 'borrower/add_borrower.html', {'form': form})

def update_borrowed_date(request, borrower_id):
    borrower = get_object_or_404(Borrower, id=borrower_id)
    if request.method == 'POST':
        form = BorrowerForm(request.POST, instance=borrower)
        if form.is_valid():
            form.save()
            return redirect('borrower_list')
    else:
        form = BorrowerForm(instance=borrower)
    return render(request, 'borrower/update_borrowed_date.html', {'form': form, 'borrower': borrower})

def borrower_list(request):
    borrowers = Borrower.objects.select_related('book').all()
    return render(request, 'borrower/borrower_list.html', {'borrowers': borrowers})
