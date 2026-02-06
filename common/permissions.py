from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.utils import timezone
from datetime import timedelta


class IsAnonymous(BasePermission):
    """
    Разрешает только чтение (GET, HEAD, OPTIONS)
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwner(BasePermission):
    """
    Проверка владельца объекта
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class CanEditWithIn15Minutes(BasePermission):
    """
    Редактирование только в течение 15 минут
    """
    def has_object_permission(self, request, view, obj):
        time_passed = timezone.now() - obj.created_at
        return time_passed <= timedelta(minutes=15)


class IsModerator(BasePermission):
    """
    Модератор:
    - не может создавать (POST)
    - может редактировать и удалять любые объекты
    """

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.is_staff:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
