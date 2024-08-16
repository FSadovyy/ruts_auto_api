import ruts_auto_api.tests_api.api_base.api_base as api_base
import inspect


def request_list(module, method):
    req_parser = {}

    for name, obj in inspect.getmembers(api_base):
        if inspect.isclass(obj) and "METHOD" in obj.__dict__:
            req_parser.update({obj.METHOD: obj})

    if method not in req_parser:
        raise ValueError("Incorrect method in list maker")

    method_list = []

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, req_parser[method]) and obj != req_parser[method]:
            method_list += [obj]

    print(method_list)

    return method_list
