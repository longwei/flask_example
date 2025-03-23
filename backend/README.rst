

curl localhost:5000/login \
    -H "Content-Type: application/json" \
    -d '{"username":"longwei", "password": "my-password"}' \
    -vvv

curl localhost:5000/users \
    -H "Authorization: Bearer $BEARER_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"name":"longwei"}' \
    -vvv