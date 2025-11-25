
def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


