from rest_framework.permissions import BasePermission


class ExamplePermission(BasePermission):
    """
    Base Permissions for example app.  Can expand from this for other API routes.
    """
    PUBLIC_METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    AUTHENTICATED_METHODS = []
    ADMIN_METHODS = []

    def has_permission(self, request, view):
        if request.method in self.PUBLIC_METHODS:
            return True
        if (request.user and
                request.user.is_active and
                request.user.is_authenticated()):
            if request.method in self.AUTHENTICATED_METHODS:
                return True
            if request.user.is_staff and request.method in self.ADMIN_METHODS:
                return True
        return False


class CarPermission(ExamplePermission):
    PUBLIC_METHODS = ['GET']
    AUTHENTICATED_METHODS = ['POST', 'PUT']
    ADMIN_METHODS = ['DELETE']
