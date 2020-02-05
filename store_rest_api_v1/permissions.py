from rest_framework import permissions

class IsDeveloper(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print("has obj check")
        if not (request.method in permissions.SAFE_METHODS):
            return False

        try:
            print("is developer?")
            return request.user.is_developer()
        except:
            print("exception")
            return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)