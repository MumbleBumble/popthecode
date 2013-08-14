# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from search.models import Browser, Device

def home(request):
    return render_to_response('search/hom2e.html')

def about(request):
    return render_to_response('search/about.html')

def search(request):
    if request.method == 'GET':
        url = request.GET['url']
        device = request.GET['device']
        browser = request.GET['browser']

    #clean up/normalize the url (for convenience)
    from urlparse import urlparse, urlunparse
    (scheme,netloc, path, _, _, frag) = urlparse(url, "http")
    pure_url = scheme+'://'+path.split('/', 1)[0]+'/'
    if not netloc and path:
        site = urlunparse((scheme, path, "", "", "", ""))
    else:
        site = urlunparse((scheme, netloc,path, "", "", ""))

    #Here we actually look up the url and retrieve the source code
    import urllib2
    #Construct the agent_user string
    try:
        bwsr = Browser.objects.get(name = browser)
        dev = Device.objects.get(name = device)
        user_agent = (bwsr.mozilla+' '+'( '+dev.paren+')'+' '+bwsr.render+' '+dev.mobile+' '+bwsr.after)
    except:
        return render_to_response('search/page_not_found.html', {'url': site})

    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(site, None, headers)
    try:
        response = urllib2.urlopen(req)
    except:
        return render_to_response('search/page_not_found.html', {'url': site})
    page = response.read()
    pure_url = pure_url.encode('utf-8')

    #Here we clean up the page a bit (make sure all the links work)
    page = page.replace('"/', '"'+pure_url)
    page = page.replace('"//', '"'+'http://')
    page = page.replace('\'/', '\''+pure_url)
    page = page.replace('\'//', '\''+'http://')


    return render_to_response('search/result.html', {'url':url, 'source_code':page})
