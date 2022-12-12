from src.models import users, db
from secuirty import bcrypt
import os

def refresh_db():
    users.query.delete()
    db.session.commit()

def create_user(user_name='testUser001', user_email= 'testUser001@test.com', user_password='testPassword001'):
    hashed_bytes = bcrypt.generate_password_hash(user_password, int(os.getenv('BCRYPT_ROUNDS')))
    hashed_password = hashed_bytes.decode('utf-8')
    new_user = users(user_name=user_name, user_email=user_email, user_password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
