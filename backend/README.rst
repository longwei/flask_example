follow https://github.com/serlesen/backend-flask

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


# why ORM-level abstraction, navigate between related objects in Python code
# country = Country.query.get(1)
# for user in country.users:
#     print(user.username)
# backref here the conversion is define in the children entity,
# but norm is defined in the parent entity

# foreign key constraint Foreign key to Country
# ensures referential integrity at the database level
# foreign key always define in the child entity <think raw SQL>

# userlist=False means that the relationship is one-to-one
# backref is shortcut for one-to-many, it only need one side
# back_populates is used for two-way relationship and needs both sides
# back_populates is now recommended as explict is better than implicit

# final though on ORM...it is crazy, it make simple thing slightly easier
# and make complicated thing even more complicated.
# I will stick with raw SQL for now.