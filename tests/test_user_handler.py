from Handlers.artifactory_user_handler import UserHandler

new_user = "Alex"
new_user_password = "password"


def test_user_handler():
    uh = UserHandler()
    # Get a list of system users.
    users = uh.get_users()
    user_found = False
    for user in users:
        if new_user in user['name']:
            user_found = True
    assert user_found is False, "User found in the system before creation request was sent."
    create = uh.create_or_replace_user(user_name=new_user, password=new_user_password)
    assert create, "Failed to create new user."
    user_details = uh.get_user_details(user_name=new_user)
    assert user_details['admin'] is False, f"Unexpected permission level: {user_details['admin']}."
    update = uh.update_user(user_name=new_user, password=new_user_password, is_admin="true")
    assert update, "Failed to update the user."
    updated_user_details = uh.get_user_details(user_name=new_user)
    assert updated_user_details['admin'], f"Unexpected permission level: {user_details['admin']}."
    uh.delete_user(user_name=new_user)
    user_found = False
    users = uh.get_users()
    for user in users:
        if new_user in user['name']:
            user_found = True
    assert user_found is False, f"User {new_user} found in the system after delete request was sent."
    assert uh.login(user_name=new_user, password=new_user_password) is False, "Fail: Successfully loged in to deleted" \
                                                                              " user."


def delete_user():
    uh = UserHandler()
    users = uh.get_users()
    uh.delete_user(user_name=new_user)
    user_found = False
    users = uh.get_users()
    for user in users:
        if new_user in user['name']:
            user_found = True
    assert user_found is False, f"User {new_user} found in the system after delete request was sent."
