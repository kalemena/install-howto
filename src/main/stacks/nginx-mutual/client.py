import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

resp = requests.get(
    'https://localhost/',
    cert=('/security/workspace/client.crt', '/security/workspace/client.key'),
    verify='/security/workspace/ca.crt',
)

if resp.status_code != 200:
    print('Failure. Expected status_code 200 but got {}'.format(resp.status_code))
    exit(1)
else:
    print('Success !')