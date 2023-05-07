from django.shortcuts import render
from leads.forms import LeadForm
from leads.models import Lead
from django.contrib import messages

# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        form = LeadForm(data=request.POST)
        if form.is_valid():
            new_lead = Lead.objects.create(**form.cleaned_data)
            messages.success (request, '{}, your massege has been successfully sent'.format(new_lead.name))
        else:
            messages.error (request, 'Something is goin wrong')
    form = LeadForm
    context={
        'form' : form,
    }
    
    return render(request, 'leads/contact.html', context=context )