

curl localhost:5000/login \
    -H "Content-Type: application/json" \
    -d '{"username":"longwei", "password": "my-password"}' \
    -vvv

curl localhost:5000/users \
    -H "Authorization: Bearer $BEARER_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"name":"longwei"}' \
    -vvv

docker run -d -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_USER=longwei -e POSTGRES_PASSWORD=my-password -e POSTGRES_DB=backenddb -p 5432:5432 postgres:13