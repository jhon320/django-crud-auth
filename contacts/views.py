from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm


@login_required
def contacts(request):

    contacts = Contact.objects.filter(user=request.user)

    return render(request, 'contacts.html', {
        'contacts': contacts
    })


@login_required
def create_contact(request):

    if request.method == 'GET':

        return render(request, 'create_contact.html', {
            'form': ContactForm()
        })

    form = ContactForm(request.POST)

    if form.is_valid():

        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()

        return redirect('contacts')

    return render(request, 'create_contact.html', {
        'form': form,
        'error': 'Error al crear el contacto.'
    })


@login_required
def contact_detail(request, contact_id):

    contact = get_object_or_404(
        Contact,
        id=contact_id,
        user=request.user
    )

    return render(request, 'contact_detail.html', {
        'contact': contact
    })


@login_required
def update_contact(request, contact_id):

    contact = get_object_or_404(
        Contact,
        id=contact_id,
        user=request.user
    )

    if request.method == 'GET':

        return render(request, 'create_contact.html', {
            'form': ContactForm(instance=contact)
        })

    form = ContactForm(request.POST, instance=contact)

    if form.is_valid():
        form.save()
        return redirect('contacts')

    return render(request, 'create_contact.html', {
        'form': form,
        'error': 'Error al actualizar el contacto.'
    })


@login_required
def delete_contact(request, contact_id):

    contact = get_object_or_404(
        Contact,
        id=contact_id,
        user=request.user
    )

    if request.method == 'POST':
        contact.delete()
        return redirect('contacts')

    return render(request, 'delete_contact.html', {
        'contact': contact
    })