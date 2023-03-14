from django.shortcuts import render
from django.core.paginator import Paginator

import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from .models import Product


import requests
from requests.adapters import HTTPAdapter, Retry
import time



oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


# Create your views here.
def boucherie(request):
    return render(request, 'boucherie/Boucherie.html')

def boulangerie(request):
    return render(request, 'boulangerie/Boulangerie.html')

def epicerie(request):
    products = Product()
    
    return render(request, 'epicerie/Epicerie.html', {
        'products': products

        
    })

def maraicher(request):
    return render(request, 'maraicher/Maraicher.html')

def poissonnerie(request):
    return render(request, 'poissonnerie/Poissonnerie.html')

def boissons(request):
    return render(request, 'boissons/Boissons.html')

def send_request(url,
    n_retries=4,
    backoff_factor=0.9,
    status_codes=[504, 503, 502, 500, 429]):
    sess = requests.Session()
    retries = Retry(connect=n_retries, backoff_factor=backoff_factor,
    status_forcelist=status_codes)
    sess.mount("https://", HTTPAdapter(max_retries=retries))
    sess.mount("http://", HTTPAdapter(max_retries=retries))
    response = sess.get(url)
    return response

# start the timer
start_time = time.time()
 
# send a request to GitHub API
url = "https://api.github.com/users"
response = send_request(url)
 
# print the status code
print(response.status_code)
 
# end timer
end_time = time.time()
 
# compute the run time
print("Run time: ", end_time-start_time)

try:
    # start execution timer
    start_time = time.time()
    url = "http://localhost:3000"
    # call send_request() method to send a request to the url
    # this will never be successful because there is no server running
    # on port 6000.
    response = send_request(url)
    print(response.status_code)
except Exception as e:
    # Catch any exception - execution will end here because
    # requests can't connect to http://localhost/6000
    print("Error Name: ", e.__class__.__name__)
    print("Error Message: ", e)
finally:
    # Pick end time
    end_time = time.time()
    # Calculate the time taken to execute.
    print("Run time: ", end_time-start_time)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )
def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("boutique/template/index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


