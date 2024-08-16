from faker import Faker

fake = Faker("ru_RU")


class PostBody:
    def __init__(self, fields, *args):
        self.body = {k: v for k, v in zip(fields, args)}

    def empty_field(self, field):
        self.body[field] = ""

    def miss_field(self, field):
        del self.body[field]

    def __call__(self):
        return self.body


class MainpagePostBody:
    FIELDS = ["fio", "email", "message"]

    @staticmethod
    def body(*args: str) -> dict:
        return {k: v for k, v in zip(MainpagePostBody.FIELDS, args)}

    @staticmethod
    def body_random():
        return {
            "fio": fake.name(),
            "email": fake.email(),
            "message": fake.text()
        }

    @staticmethod
    def empty_field(field):
        body = MainpagePostBody.body_random()
        body[field] = ""
        return body

    @staticmethod
    def miss_field(field):
        body = MainpagePostBody.body_random()
        del body[field]
        return body
