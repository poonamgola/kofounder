from django.shortcuts import render, redirect
from .models import Contact, Faq
from django.contrib import messages

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        company = request.POST.get('company')
        message = request.POST.get('message')
        
        # Create a new Contact instance
        data = Contact(
            name=name,
            email=email,
            phone=number,
            company=company,
            Message=message
        )
        
        # Save the instance to the database
        data.save()

        # Provide a success message to the user
        messages.success(request, 'Message was successfully sent!')
        return redirect('contact')
    
    # Render the contact page if not a POST request
    return render(request, 'contact.html')

def faqs(request):
    faq = Faq.objects.all()
    context = {
        'faqs':faq,
    }
    return render(request,'faq.html', context)