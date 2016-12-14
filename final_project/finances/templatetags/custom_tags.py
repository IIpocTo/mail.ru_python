import requests
from django import template

register = template.Library()


@register.inclusion_tag('account_list.html')
def show_accounts(request):
    headers = {'Authorization': 'JWT ' + request.session["token"]}
    response = requests.get("http://localhost:8000/api/accounts/", headers=headers)
    accounts = response.json()
    return {'accounts': accounts}
