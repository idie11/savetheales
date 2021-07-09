from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermissionOrReadOnly(BasePermission):
    # def has_object_permission(self, request, view, obj):
    #     if obj == request.user:
    #         return True
    #     return request.user.is_superuser or request.user.is_staff
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET': 
            return True
        return obj == request.user