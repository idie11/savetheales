from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermissionOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True 
        return obj == request.user or obj == request.is_staff