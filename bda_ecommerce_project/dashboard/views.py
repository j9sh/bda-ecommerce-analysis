from django.shortcuts import render

# Create your views here.
def homepage(req):
    return render(req, 'homepage.html', {})
    
def ecommerce_report_page(req):
    return render(req, 'retail_report.html', {})

def marketing_report_page(req):
    return render(req, 'marketing_report.html', {})
