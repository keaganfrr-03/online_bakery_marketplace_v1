from .models import ActivityLog


def log_activity(user, action, details=None, request=None, ip_address=None):
    """Create an activity log entry for a user."""
    if not user or not user.is_authenticated:
        return

    # Get IP from request if possible
    if not ip_address and hasattr(request, "META"):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    ActivityLog.objects.create(
        user=user,
        action=action,
        details=details or "",
        ip_address=ip_address,
    )

