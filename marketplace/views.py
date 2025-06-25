from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    html_content = '''
    <html>
        <body>
            <h1>Welcome to CraftNest - Artisans Meet Buyers</h1>
        </body>
    </html>
    '''
    return HttpResponse(html_content)

def product_list(request):
    html_content = '''
        <html>
            <body>
                <h1>Product List</h1>
            </body>
        </html>
        '''
    return HttpResponse(html_content)


def contact_us(request):
    html_content = '''
        <html>
            <body>
                <h1>Contact Us</h1>
            </body>
        </html>
        '''
    return HttpResponse(html_content)

