from django.shortcuts import render, redirect
from team.models import Team
from testimonials.models import Testimonial
from lead.models import Lead

# Create your views here.

def index (request):
    teams = Team.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    context = {
        'teams' : teams,
        'testimonials' : testimonials,
    }
    return render(request, 'pages/index.html', context=context)

def create_lead(request):
    if request.method == 'POST':
        lead = Lead()
        lead.name = request.POST.get('name')
        lead.email = request.POST.get('email')
        lead.subject = request.POST.get('subject')
        lead.message = request.POST.get('message')
        lead.save()
        return redirect('index')