from backend import db
from backend.entity.user import User

class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    # here the conversion is define in the children entity,
    # but norm is defined in the parent entity
    user = db.relationship("User", backref="messages", cascade="all")

    def __repr__(self):
        return f"<Message {self.id} from {self.sender.username} to {self.receiver.username}>"