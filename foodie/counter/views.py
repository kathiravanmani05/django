from django.shortcuts import render
import requests,json

#AsgZpssqijlGaR9rp0USww==krcxMIxGZKb1RZa0

def home(request):

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'AsgZpssqijlGaR9rp0USww==krcxMIxGZKb1RZa0'})
        if response.status_code == requests.codes.ok:
            api = json.loads(response.text)
        
        else:
           api = 'oops! There was an error'

        return render(request, 'home.html',{'api':api, })
    else:
        return render(request, 'home.html',{'query':'Enter a Valid Query'})
