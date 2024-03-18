from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HelpForm
from .models import HelpRequest

# Create your views here.
def help_page(request):
    """
    Handles the creation of a new customer service request from :model:`accounts.HelpRequest`.

    **Arguments:**

    ``request``
    The HTTP request.

    **POST:**

    Help form information is validated and if valid, a new HelpRequest instance is created and saved. 
    A success message is displayed.

    **GET:**

    An empty HelpForm is displayed.

    **Context**

    ``help_form``
    An instance of HelpForm.

    **Template:**

    :template:`help.html`
    """

    if request.method == "POST":
        help_form = HelpForm(data=request.POST)
        if help_form.is_valid():
            help_request = HelpRequest()
            help_request = help_form.save()
            messages.add_message(request, messages.SUCCESS, "Customer service request received! Response to be expected within 2 days")
            return redirect('home')  # Redirect to home page
        else:
            messages.add_message(request, messages.ERROR, "There was an error in your form. Please try again.")
    else:
        help_form = HelpForm()
    
    return render(
        request, 
        'help/help.html', 
        {
        "help_form": help_form
        }, 
    )