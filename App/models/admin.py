from App.database import db
from App.models.user import User

class Admin(User):
    __mapper_args__ = {
        'polymorphic_identity': 'admin'  # Identity for Admin class
    }

    def __init__(self, username, password):
        super().__init__(username, password)
