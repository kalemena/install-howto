
mkdir -p workspace
cd workspace

# 
# Generate Certificate Authority (CA) files 
# 
openssl genrsa -des3 -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj '/CN=ca'

cat ca.key > ca.pem
cat ca.crt >> ca.pem

#
# Generating Client/User Certificates 
#

openssl genrsa -des3 -out user.key 4096
openssl req -new -key user.key -out user.csr -subj '/CN=user'
openssl x509 -req -days 365 -in user.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out user.crt
openssl pkcs12 -export -out user.pfx -inkey user.key -in user.crt -certfile ca.crt
# checks
openssl verify -verbose -CAfile ca.crt user.crt

#
# Generating Server Certificates
#

openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr -subj '/CN=server'
openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 1 -out server.crt

