from main import User

users = User.select()
for user in users:
    print(user.user_name, user.user_email, user.user_phone, user.user_password)