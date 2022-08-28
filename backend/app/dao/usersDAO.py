from sqlalchemy.orm import Session
import schemas

class UsersDAO:
    def get_user_by_username(username: str, db: Session):
        pass

    def create_user(user: schemas.UserCreate, db: Session):
        pass

    def get_user_dict(username: str, db: Session):
        pass

    def get_user(user_id: int, db: Session):
        pass

    def delete_user(db: Session, user: schemas.User):
        pass

    def read_user(user_id: int, db: Session):
        pass

    def update_user(user_id: int, updated_fields: schemas.UserUpdate, db: Session):
        pass

    def get_users(db: Session):
        pass

