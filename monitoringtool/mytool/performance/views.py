from django.shortcuts import render
import json


def home(request):
    return render(request, 'home.html')


def tools(request):
    return render(request, 'tools.html')


def monitor(request):
  url='https://www.iserveradmin.com/'
  json_file_path = "iserveradmin.json"
  with open(json_file_path, encoding='utf8') as j:
    contents = json.loads(j.read())
    for key, value in contents.items():
      # print(key)
      print(value)
    fcp= contents["configSettings"]['maxWaitForFcp']
    load= contents["configSettings"]['maxWaitForLoad']
    performance= contents["categories"]['performance']['score']
    accessibility= contents["categories"]["accessibility"]['score']
    bp= contents["categories"]["best-practices"]['score']
    seo= contents["categories"]["seo"]['score']
    pwa= contents["categories"]["pwa"]['score']
    return render(request,
                  'monitor.html',
                  {'per': performance,
                   'acc': accessibility,
                   'bp': bp,
                   'seo': seo,
                   'pwa': pwa,
                   'url':url,
                   'fcp':fcp,
                   'load':load,
                   }
                  )