services_registry = {}


def register_service(name, service):
    services_registry[name] = service


def get_service(name):
    service = services_registry[name]
    return service
