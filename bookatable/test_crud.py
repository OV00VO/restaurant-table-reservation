# Reference in modified parts below: Code Institute Curriculum and Code Star Project   
# Reference in modified parts below: https://github.com/flatplanet/Django-CRM
# Reference in modified parts below: https://www.pythonpool.com/python-unittest-vs-pytest/
# Notes: Below code is based on the above references and modifed for the project


from django.test import TestCase

from .models import Reservation

# Reference in modified parts below: https://www.pythonpool.com/python-unittest-vs-pytest/
class ReservationTests(TestCase):
    """Tests for Reservation model functionality using a PostgreSQL database."""

    def setUp(self):
        """
        Override settings with environment variable values (if `pytest-django` is not used).

        This approach assumes you set DATABASE_URL in your environment.
        """
        from django.core.exceptions import ImproperlyConfigured
        try:
            from django.conf import settings
            settings.configure(**os.environ.get('DJANGO_SETTINGS_MODULE'))
        except ImproperlyConfigured:
            pass

    def test_create_reservation(self):
        """Test creating a reservation."""
        reservation = Reservation.objects.create(
        )
        self.assertEqual(reservation.name, "John Doe")

    def test_read_reservation(self):
        """Test reading a reservation."""
        reservation = Reservation.objects.create(
        )
        fetched_reservation = Reservation.objects.get(pk=reservation.pk)
        self.assertEqual(fetched_reservation.name, "Jane Doe")

    def test_update_reservation(self):
        """Test updating a reservation."""
        reservation = Reservation.objects.create(
        )
        reservation.name = "Updated Name"
        reservation.save()
        updated_reservation = Reservation.objects.get(pk=reservation.pk)
        self.assertEqual(updated_reservation.name, "Updated Name")

    def test_delete_reservation(self):
        """Test deleting a reservation."""
        reservation = Reservation.objects.create(
        )
        reservation_count = Reservation.objects.count()
        reservation.delete()
        self.assertEqual(Reservation.objects.count(), reservation_count - 1)
