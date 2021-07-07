# Imports
import json
from qsaas.qsaas import Tenant

# Info needed to auth
key = 'Qlik API KEY'

fqdn = 'Qlik full domain name'

id = 'Qlik UserId'

# Qlik conn
q = Tenant(api_key=key, tenant=fqdn, tenant_id=id)

# To send a reload request to app
def reload(q, app_id):
    q.post('reloads', json.dumps({'appID': f'{app_id}'}))

# Sending reload request
reload(app_id, q)