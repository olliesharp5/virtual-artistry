from django.shortcuts import render
from django.contrib import messages
from .forms import HelpForm
from .models import HelpRequest

# Create your views here.
def help_page(request):

    if request.method == "POST":
        help_form = HelpForm(data=request.POST)
        if help_form.is_valid():
            help_request = HelpRequest()
            help_request = help_form.save()
            messages.add_message(request, messages.SUCCESS, "Customer service request received! Response to be expected within 2 days")
        else:
            messages.add_message(request, messages.ERROR, "There was an error in your form. Please try again.")
    else:
        help_form = HelpForm()
    
    return render(
        request, 
        'help.html', 
        {
        "help_form": help_form
        }, 
    )