from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOrReadOmly(BasePermission):
    def has_object_permission(self, request, view):
        # if request.method in ['PUT', 'PATCH']:
        #     # return request.user == request.is_staff or request.user == rew\
        return request.user or request.user.is_superuser or request.user.is_staff
