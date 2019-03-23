from rest_framework.decorators import api_view
from rest_framework.response import Response

from eospy.cleos import Cleos

from backend.settings import PRIVATE_KEY


@api_view(http_method_names=['POST'])
def create_eos_account(request):
    account_name = request.data['account_name']
    owner_key = request.data['owner_key']
    active_key = request.data['active_key']

    ce = Cleos(url='https://jungle2.cryptolions.io:443')
    resp = ce.create_account('eosio', PRIVATE_KEY, account_name,
                             owner_key,
                             active_key,
                             stake_net='1.0000 EOS', stake_cpu='1.0000 EOS',
                             ramkb=8, permission='active', transfer=False,
                             broadcast=True)

    return Response('ok')
