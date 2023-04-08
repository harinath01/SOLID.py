# Example 1
class Account:
    """Demo bank account class """

    def __init__(self, account_no: str):
        self.account_no = account_no

    def get_account_number(self):
        """Get account number"""
        return self.account_no

    def save(self):
        """Save account number into DB"""
        pass


# Example 2
class User:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def get_user_info(self):
        """
        Returns the user's name, email, and phone number as a dictionary
        """
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    def save_to_database(self):
        """
        Saves the user's name, email, and phone number to a database
        """
        database = Database()
        database.connect()
        database.execute(
            f"INSERT INTO users (name, email, phone) VALUES ('{self.name}', '{self.email}', '{self.phone}')"
        )
        database.disconnect()