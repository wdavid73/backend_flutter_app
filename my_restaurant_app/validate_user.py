from rest_framework.request import Request


def validate(request: Request, type: str) -> bool:
    if request.user.is_authenticated and request.user.position.name == type:
        return True
    return False
