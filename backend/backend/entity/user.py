from backend import db
from backend.entity.country import Country

class User(db.model):
    __tablename__ = "backend_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # foreign key constraint Foreign key to Country
    # ensures referential integrity at the database level
    # foreign key always define in the child entity <think raw SQL>
    country_id = db.Column(db.Integer, db.ForeignKey(Country.id))

    # ORM-level abstraction, navigate between related objects in Python code
    # country = Country.query.get(1)
    # for user in country.users:
    #     print(user.username)
    country = db.relationship("Country", backref="users", lazy=True)
    

    def __repr__(self):
        return f"<User {self.username}>"
    

class Profile(db.model):
    # example of one-to-one relationship
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.Date, nullable=True)
    job = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    # userlist=False means that the relationship is one-to-one
    # backref is shortcut for one-to-many, it only need one side
    # back_populates is used for two-way relationship and needs both sides
    # back_populates is now recommended as explict is better than implicit

    user = db.relationship("User", userlist=False, back_populates="profile")