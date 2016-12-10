import json

import requests
from django import template

register = template.Library()


@register.inclusion_tag('account_list.html')
def show_accounts(request):
    headers = {'Authorization': 'JWT ' + request.session["token"]}
    response = requests.get("http://localhost:8000/api/accounts/", headers=headers)
    account_json = json.loads(response.content.decode())
    accounts_list = []
    for elem in account_json:
        accounts_list.append(list(elem.values()))
    accounts = sum(accounts_list, [])
    return {'accounts': accounts}
