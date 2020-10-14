import json
from requests.auth import HTTPBasicAuth
import Globals
import requests

class UserHandler:

    def get_users(self):
        url = Globals.artifactory + f"/api/security/users"
        res = requests.get(url=url, auth=HTTPBasicAuth(Globals.admin_user, Globals.admin_pass))
        assert res.status_code == 200
        _res = json.loads(res.text)
        return _res

    def create_or_replace_user(self, user_name: str, password: str, is_admin='false'):
        url = Globals.artifactory + f"/api/security/users/{user_name}"
        body = {
            "email": f"{user_name}@jfrog.com",
            "password": password,
            "admin": is_admin
        }
        res = requests.put(url=url, auth=HTTPBasicAuth(Globals.admin_user, Globals.admin_pass), json=body)
        if res.status_code == 200 or res.status_code == 201:
            return True
        return False

    def update_user(self, user_name: str, password: str, is_admin='false'):
        url = Globals.artifactory + f"/api/security/users/{user_name}"
        body = {
            "email": f"{user_name}@jfrog.com",
            "password": password,
            "admin": is_admin
        }
        res = requests.post(url=url, auth=HTTPBasicAuth(Globals.admin_user, Globals.admin_pass), json=body)
        if res.status_code == 200 or res.status_code == 201:
            return True
        return False

    def get_user_details(self, user_name: str):
        url = Globals.artifactory + f"/api/security/users/{user_name}"
        res = requests.get(url=url, auth=HTTPBasicAuth(Globals.admin_user, Globals.admin_pass))
        assert res.status_code == 200, "Failed to get user details."
        _res = json.loads(res.text)
        return _res

    def delete_user(self, user_name: str):
        url = Globals.artifactory + f"/api/security/users/{user_name}"
        res = requests.delete(url=url, auth=HTTPBasicAuth(Globals.admin_user, Globals.admin_pass))
        assert res.status_code == 200, f"Failed to remove user: {user_name}."

    def login(self, user_name: str, password: str):
        """
        Send a login request with credentials and get a token from the server.
        :return: access token in string format.
        """
        url = Globals.artifactory + f"/api/security/token"
        body = {
            "username": "John",
            "scope": "member-of-groups:readers",
        }
        res = requests.post(url=url, auth=HTTPBasicAuth(user_name, password), data=body)
        if res.status_code == 200:
            return True
        return False

