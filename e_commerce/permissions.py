from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsOwnerOrders(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.customer, request.user)
        return obj.customer == request.user