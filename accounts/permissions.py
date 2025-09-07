from rest_framework import permissions

class IsUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if obj.id == request.user.id:
            return True
        
        if request.user.is_staff or request.user.is_superuser:
            return True
        
        return False
            
    