# Example 1:
class BackendDeveloper:
    """This is a low-level module"""

    @staticmethod
    def python():
        print("Writing Python code")


class FrontendDeveloper:
    """This is a low-level module"""

    @staticmethod
    def javascript():
        print("Writing JavaScript code")


class Project:
    """This is a high-level module"""

    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self):
        self.backend.python()
        self.frontend.javascript()
        return "Develop codebase"


project = Project()
print(project.develop())


# Example 2:
class NewsPerson:
    """This is a high-level module"""

    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(NewsPaper().publish(news=news))


class NewsPaper:
    """This is a low-level module"""

    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(f"{news} Hello newspaper")


person = NewsPerson()
print(person.publish("News Paper"))

# Example 3
class User:
    def __init__(self, name: str):
        self.name = name

    def send_email(self, message: str, email: Email):
        email.send(self.name, message)

class Email:
    def send(self, name: str, message: str):
        print(f"Sending email to {name}: {message}")

class SMS:
    def send(self, name: str, message: str):
        print(f"Sending SMS to {name}: {message}")

user = User("John")
email = Email()
sms = SMS()

user.send_email("Hello, John!", email)  # Sends email
user.send_email("Hello, John!", sms) 