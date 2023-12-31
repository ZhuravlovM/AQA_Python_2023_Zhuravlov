from lesson29_sqlalchemy.session_handler import session
from lesson29_sqlalchemy.models.users import Users
from sqlalchemy.sql.expression import Insert
from sqlalchemy import insert

from sqlalchemy import select


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_user_by_name(self, first_name):
        return self.__session.query(Users).filter_by(first_name=first_name)

    def get_user_by_id_2(self, user_id):
        return self.__session.get(Users, {'id': user_id})

    def add_one_row(self, user_id, first_name, last_name, age, email):
        stmt = insert(Users).values(id=user_id,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    age=age,
                                                    email=email)
        stmt


    #select(User).where(User.id == 5)

    def get_all(self):
        bunch_of_users = []
        for user in self.__session.query(Users).all():
            bunch_of_users.append(user)
        return bunch_of_users


users_repository = UsersRepository()
#first_user = users_repository.get_user_by_id('BBBBBBBB')
#print(first_user)
users_repository.add_one_row('cccccccc', 'CCCC', 'CCCC', 5, 'ccccc@ccc.ccc')
all_users_2 = users_repository.get_all()
print(all_users_2)
