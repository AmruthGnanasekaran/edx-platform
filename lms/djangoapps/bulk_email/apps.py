# lint-amnesty, pylint: disable=missing-module-docstring
from django.apps import AppConfig


class BulkEmailConfig(AppConfig):
    """
    Application Configuration for bulk_email.
    """
    name = 'lms.djangoapps.bulk_email'

    def ready(self):
        import lms.djangoapps.bulk_email.signals
        from edx_ace.signals import ACE_EMAIL_SENT

