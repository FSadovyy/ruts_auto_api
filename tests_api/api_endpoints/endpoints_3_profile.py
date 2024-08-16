from ruts_auto_api.tests_api.api_base.api_base import GetRequest, PostRequest, PutRequest, PatchRequest


class Achievements(GetRequest):
    PATH = "/profile/achievements"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "countEvents": {
                "type": "integer"
            },
            "sumDistance": {
                "type": "integer"
            },
            "countLocations": {
                "type": "integer"
            }
        },
        "required": [
            "countEvents",
            "sumDistance",
            "countLocations"
        ]
    }


class AvatarGet(GetRequest):
    PATH = "/profile/avatar"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "name": {
                "type": ["string", "null"]
            },
            "surname": {
                "type": ["string", "null"]
            },
            "middlename": {
                "type": ["string", "null"]
            },
            "birthday": {
                "type": ["string", "null"]
            },
            "numberPhone": {
                "type": ["string", "null"]
            },
            "photo": {
                "type": ["string", "null"]
            }
        },
        "required": [
            "name",
            "surname",
            "middlename",
            "birthday",
            "numberPhone",
            "photo"
        ]
    }


class AvatarPut(PutRequest):
    PATH = "/profile/avatar"


class CommandsGet(GetRequest):
    PATH = "/profile/commands"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "photo": {
                        "type": ["string", "null"]
                    },
                    "name": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "photo",
                    "name"
                ]
            }
        ]
    }


class CommandsPost(PostRequest):
    PATH = "/profile/commands"
    FIELDS = {
        "clubName": "string",
        "email": "string"
    }


class MyEvents(GetRequest):
    PATH = "/profile/myevents"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {
                        "type": ["string", "null"]
                    },
                    "photo": {
                        "type": ["string", "null"]
                    },
                    "date": {
                        "type": ["string", "null"]
                    },
                    "city": {
                        "type": ["string", "null"]
                    },
                    "countPeople": {
                        "type": ["string", "null"]
                    },
                    "isPaid": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "id",
                    "photo",
                    "date",
                    "city",
                    "countPeople",
                    "isPaid"
                ]
            }
        ]
    }


class NextEvents(GetRequest):
    PATH = "/profile/nextevents"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {
                        "type": ["string", "null"]
                    },
                    "photo": {
                        "type": ["string", "null"]
                    },
                    "date": {
                        "type": ["string", "null"]
                    },
                    "city": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "id",
                    "photo",
                    "date",
                    "city"
                ]
            }
        ]
    }


class Password(PutRequest):
    PATH = "/profile/password"
    FIELDS = {
        "oldPassword": "string",
        "password": "string",
        "confirmPassword": "string"
    }


class UserDataGet(GetRequest):
    PATH = "/profile/userdata"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "name": {
                "type": ["string", "null"]
            },
            "surname": {
                "type": ["string", "null"]
            },
            "middlename": {
                "type": ["string", "null"]
            },
            "gender": {
                "type": ["string", "null"]
            },
            "birthday": {
                "type": ["string", "null"]
            },
            "numberPhone": {
                "type": ["string", "null"]
            },
            "extraPhone": {
                "type": ["string", "null"]
            },
            "adress": {
                "type": ["string", "null"]
            },
            "email": {
                "type": ["string", "null"]
            },
            "profession": {
                "type": ["string", "null"]
            },
            "command": {
                "type": ["string", "null"]
            },
            "photo": {
                "type": ["string", "null"]
            }
        },
        "required": [
            "name",
            "surname",
            "middlename",
            "gender",
            "birthday",
            "numberPhone",
            "extraPhone",
            "adress",
            "email",
            "profession",
            "command",
            "photo"
        ]
    }


class UserDataPatch(PatchRequest):
    PATH = "/profile/userdata"
    FIELDS = {
        "name": "string",
        "surname": "string",
        "middlename": "string",
        "gender": "string",
        "birthday": "2024-08-01T15:26:37.206Z",
        "numberPhone": "string",
        "extraPhone": "string",
        "adress": "string",
        "email": "string",
        "profession": "string",
        "command": "string"
    }


class UserTitleData(GetRequest):
    PATH = "/profile/usertitledata"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "name": {
                "type": ["string", "null"]
            },
            "surname": {
                "type": ["string", "null"]
            },
            "middlename": {
                "type": ["string", "null"]
            },
            "phone": {
                "type": ["string", "null"]
            },
            "email": {
                "type": ["string", "null"]
            },
            "adress": {
                "type": ["string", "null"]
            }
        },
        "required": [
            "name",
            "surname",
            "middlename",
            "phone",
            "email",
            "adress"
        ]
    }
