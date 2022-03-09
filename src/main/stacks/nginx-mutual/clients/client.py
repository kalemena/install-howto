import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

resp = requests.get(
    'https://hello.service.local/',
    cert=('/security/client.crt', '/security/client.key'),
    verify='/security/ca.crt',
)

if resp.status_code != 200:
    print('Failure. Expected status_code 200 but got {}'.format(resp.status_code))
    exit(1)
else:
    print('Success !')