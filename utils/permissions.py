from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
 """
 Custom permission to only allow owners of an object to edit it.
 """
 def has_object_permission(self, request, view, obj):
     # Read permissions are allowed to any request,
     # so we'll always allow GET, HEAD or OPTIONS requests.
     if request.method in permissions.SAFE_METHODS:
         return True
     # write permission is only allowed to the owner of the object
     return obj.created_by == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to have write permission
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner or admin to have write permission
    """
    def has_object_permission(self, request, view, obj):
         if request.method in permissions.SAFE_METHODS:
            return True
         return request.user and (obj.created_by == request.user or request.user.is_superuser)