def individual_user(user):
    return {
        "id": str(user["_id"]),
        "name" : user["name"],
        "email" : user["email"],
        "password" : user["password"],
        "age" : user["age"]
    }

def all_users(users):
    return [individual_user(user) for user in users]