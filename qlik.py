# Imports
import json
from qsaas.qsaas import Tenant

# Informações necessárias para autenticação
# Chave API
key = 'Qlik API KEY'
# Domínio completo
fqdn = 'Qlik full domain name'
# ID de usuário
usr_id = 'Qlik UserId'

# Qlik connection
qconn = Tenant(api_key=key, tenant=fqdn, tenant_id=usr_id)

# Função para enviar um request de recarga à aplicação
def reload(qlik_connection, app_id):
    qlik_connection.post('reloads', json.dumps({'appID': f'{app_id}'}))

# Sending reload request
reload(app_id, qconn)
