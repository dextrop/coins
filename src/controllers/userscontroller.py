from src.models.users import Users
from src.models.userstoken import UsersToken
from src.serializers.usersserializer import UsersSerializer
from src.lib.helperfns import password_hashing
from django.core.exceptions import ValidationError

model_fields = ['name', 'email', 'password']

class UsersController():
    def check_if_user_exits(self, email):
        objects = Users.objects.filter(email=email)
        if (objects.count() < 1):
            return None
        return objects[0]

    def generate_session(self, object):
        token, created = UsersToken.objects.get_or_create(user_id=object)
        user_info = UsersSerializer(object, many=False).data
        user_info["token"] = token.access_token
        return user_info

    def login(self, email, password):
        obj = self.check_if_user_exits(email=email)
        if obj == None:
            raise ValidationError("Email Does not exits")

        password_req, _ = password_hashing(password, obj.salt)
        if password_req != obj.password:
            raise ValidationError("Invalid Password")

        return self.generate_session(obj)

    def signup(self, request_data):
        obj = self.check_if_user_exits(email=request_data["email"])
        if obj != None:
            raise ValidationError("User Already Exits")

        for field in model_fields:
            if field not in request_data:
                raise ValidationError("Missing key '{}'".format(field))
        request_data["password"], request_data["salt"] = password_hashing(request_data["password"])                
        user_obj = Users.objects.create(**request_data)
        return self.generate_session(user_obj)
