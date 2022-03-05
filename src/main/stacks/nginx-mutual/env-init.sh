
mkdir -p workspace
cd workspace

# 
# Generate Certificate Authority (CA) files 
# 
# openssl genrsa -des3 -out ca.key 4096
# openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj '/CN=ca'

openssl req -nodes -x509 -newkey rsa:4096 \
 -keyout ca.key \
 -out ca.crt \
 -days 365 \
 -subj "/CN=ca"

cat ca.key > ca.pem
cat ca.crt >> ca.pem

#
# Generating Client/User Certificates 
#

# openssl genrsa -des3 -out user.key 4096
# openssl req -new -key user.key -out user.csr -subj '/CN=user'
# openssl x509 -req -days 365 -in user.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out user.crt
# openssl pkcs12 -export -out user.pfx -inkey user.key -in user.crt -certfile ca.crt

# Certificate Key
openssl genrsa -out client.key 2048

# Certificate Signing Request
openssl req -new \
 -key client.key \
 -out client.csr \
 -subj "/CN=client" \
 -sha256

# Certificate Signing
openssl x509 -req \
 -in client.csr \
 -CA ca.crt \
 -CAkey ca.key \
 -CAcreateserial \
 -out client.crt \
 -days 1024

# checks
openssl verify -verbose -CAfile ca.crt client.crt

#
# Generating Server Certificates
#

# openssl genrsa -out server.key 4096
# openssl req -new -key server.key -out server.csr -subj '/CN=server'
# openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 1 -out server.crt

# Certificate Key
openssl genrsa -out server.key 2048

# Certificate Signing Request
openssl req -new \
 -key server.key \
 -out server.csr \
 -subj "/CN=server" \
 -sha256

# Certificate Signing
openssl x509 -req \
 -in server.csr \
 -CA ca.crt \
 -CAkey ca.key \
 -CAcreateserial \
 -out server.crt \
 -days 1024

