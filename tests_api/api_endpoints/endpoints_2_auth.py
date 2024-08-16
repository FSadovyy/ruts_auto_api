from ruts_auto_api.tests_api.api_base.api_base import GetRequest, PostRequest


class Check(PostRequest):
    PATH = "/code/check"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "email": {
                "type": "string"
            },
            "code": {
                "type": "string"
            }
        },
        "required": [
            "email",
            "code"
        ]
    }


class Google(GetRequest):
    PATH = "/auth/google"


class Logout(PostRequest):
    PATH = "/auth/logout"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            }
        },
        "required": [
            "message"
        ]
    }


class Me(GetRequest):
    PATH = "/users/me"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "_id": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        },
        "required": [
            "_id",
            "email"
        ]
    }


class Send(PostRequest):
    PATH = "/code/send"
    FIELDS = {
        "email": "string"
    }
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            }
        },
        "required": [
            "message"
        ]
    }


class Signin(PostRequest):
    PATH = "/auth/signin"
    FIELDS = {
        "email": "string",
        "password": "string",
        "remember": True
    }
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "_id": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        },
        "required": [
            "_id",
            "email"
        ]
    }


class Signup(PostRequest):
    SUCCESS_CODE = 201
    PATH = "/auth/signup"
    FIELDS = {
        "email": "string",
        "password": "string",
        "confirmPassword": "string"
    }
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "_id": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        },
        "required": [
            "_id",
            "email"
        ]
    }


class Vk(GetRequest):
    PATH = "/auth/vk/confirm"
