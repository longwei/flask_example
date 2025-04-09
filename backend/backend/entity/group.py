from backend import db

users_to_groups_association = db.Table(
    "users_to_groups",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("group.id"), primary_key=True)
)
class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    users = db.relationship(
        "User",
        secondary=users_to_groups_association,
        backref=db.backref("groups", lazy="dynamic"),
        lazy="dynamic"
    )

    def __repr__(self):
        return f"<Group {self.name}>"