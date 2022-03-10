const fs = require('fs');
const https = require('https');

console.info('Connecting to https://hello.service.local');

https.get(
  {
    hostname: 'hello.service.local',
    port: 443,
    path: '/',
    method: 'GET',
    cert: fs.readFileSync('/security/client.crt'),
    key: fs.readFileSync('/security/client.key'),
    ca: fs.readFileSync('/security/ca.crt')
  },
  res => {
    if (res.statusCode != 200) {
      console.error(`expected status 200 but found ${res.statusCode}`);
      return process.exit(1);
    } else {
        console.info('Success !')
    }
  }
).on('error', error => {
  console.error(error);
  process.exit(1);
});
