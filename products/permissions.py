from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOmly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.method == 'GET':
            return True
        else:
            return False