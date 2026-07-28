# ==========================================
# User Authentication System
# A simple login system with regular users
# and an admin role that can delete users.
# ==========================================

class User:

    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    def check_password(self, attempt):
        # Compare the given attempt with the real password
        if self.password == attempt:
            return True
        else:
            return False

    def login(self, attempt):
        # Try to log in using the given password attempt
        if self.check_password(attempt):
            print(f"Access granted for {self.username} (role: {self.role})")
        else:
            print("Access denied")


class AdminUser(User):
    # AdminUser inherits everything from User (check_password, login)
    # and always gets role="admin" — this can never be overridden.

    def __init__(self, username, password):
        super().__init__(username, password, role="admin")

    def delete_user(self, target_username):
        # Only AdminUser has this ability, regular User does not
        print(f"{self.username} deleted user '{target_username}'")


# ------------------------------------------
# Create a regular user and an admin user
# ------------------------------------------
usertest = User("test", "1234")
Ruby = AdminUser("taha", "tah2dmin")

# ------------------------------------------
# Test login with correct password
# ------------------------------------------
usertest.login("1234")
Ruby.login("tah2dmin")

# ------------------------------------------
# Test login with wrong password
# ------------------------------------------
usertest.login("wrongpass")
Ruby.login("wrongpass")

# ------------------------------------------
# Test delete_user (only AdminUser has it)
# ------------------------------------------
Ruby.delete_user("usertest")

# Uncomment the line below to see what happens —
# regular User objects don't have delete_user, so this
# will raise: AttributeError: 'User' object has no attribute 'delete_user'
# sara.delete_user("taha")