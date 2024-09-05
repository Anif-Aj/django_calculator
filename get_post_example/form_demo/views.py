# form_demo/views.py

from django.shortcuts import render
from django.http import HttpResponse

def form_view(request):
    return render(request, "form_demo/form.html")

def submit_view(request):
    if request.method == 'POST':
        # Get form data
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")

        a=int(num1) 
        b=int(num2)

        # result = request.POST.get(num1 + num2)
        # Process the data (in this example, just displaying it)
        return render(request, "form_demo/submit.html", {"result": (a + b)})
    else:
        # Redirect to the form page if accessed via GET
        return render(request, "form_demo/form.html")