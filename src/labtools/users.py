class UserRepository:
    def get_by_id(self, user_id):
        raise NotImplementedError


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user_name(self, user_id):
        user = self.repository.get_by_id(user_id)
        if user is None:
            return None
        return user["name"]
