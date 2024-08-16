from ruts_auto_api.tests_api.api_base.api_base import GetRequest, PostRequest


class AboutUs(GetRequest):
    PATH = "/mainpage/aboutUs"

    SCHEMA = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "type": "array",
        "items": {
            "type": "string"
        }
    }


class Cities(GetRequest):
    PATH = "/mainpage/cities"

    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "eventName": {
                        "type": "string"
                    },
                    "date": {
                        "type": "string"
                    },
                    "city": {
                        "type": "string"
                    },
                    "cityLink": {
                        "type": "string"
                    },
                    "media": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "eventName",
                    "date",
                    "city",
                    "cityLink",
                    "media"
                ]
            }
        ]
    }


class HowitWas(GetRequest):
    PATH = "/mainpage/howItWas"

    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "media": {
                        "type": "string"
                    },
                    "mediaPreview": {
                        "type": "string"
                    },
                    "feedback": {
                        "type": "object",
                        "properties": {
                            "login": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "login",
                            "text"
                        ]
                    }
                },
                "required": [
                    "title",
                    "media",
                    "mediaPreview",
                    "feedback"
                ]
            }
        ]
    }


class Mainpage(GetRequest):
    PATH = "/mainpage"

    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "aboutAs": {
                "type": "array",
                "items": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "string"
                    }
                ]
            },
            "cities": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "eventName": {
                                "type": "string"
                            },
                            "date": {
                                "type": "string"
                            },
                            "city": {
                                "type": "string"
                            },
                            "media": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "eventName",
                            "date",
                            "city",
                            "media"
                        ]
                    }
                ]
            },
            "howItWas": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string"
                            },
                            "media": {
                                "type": "string"
                            },
                            "mediaPreview": {
                                "type": "string"
                            },
                            "feedback": {
                                "type": "object",
                                "properties": {
                                    "login": {
                                        "type": "string"
                                    },
                                    "text": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "login",
                                    "text"
                                ]
                            }
                        },
                        "required": [
                            "title",
                            "media",
                            "mediaPreview",
                            "feedback"
                        ]
                    }
                ]
            },
            "partners": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "media": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "name",
                            "media"
                        ]
                    }
                ]
            }
        },
        "required": [
            "aboutAs",
            "cities",
            "howItWas",
            "partners"
        ]
    }


class Partners(GetRequest):
    PATH = "/mainpage/partners"
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "mainPartner": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "photo": {
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "photo"
                ]
            },
            "partners": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "photo": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "name",
                            "photo"
                        ]
                    }
                ]
            }
        },
        "required": [
            "mainPartner",
            "partners"
        ]
    }


class Reqcity(PostRequest):
    PATH = "/mainpage/reqcity"
    FIELDS = {
        "fio": "string",
        "email": "string",
        "message": "string"
    }


class Question(PostRequest):
    PATH = "/mainpage/question"
    FIELDS = {
        "fio": "string",
        "email": "string",
        "message": "string"
    }
