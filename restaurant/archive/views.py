from django.shortcuts import render, redirect
from .models import Reservation

def test_crud(request):
    message = ''

    if request.method == 'POST' and 'create_button' in request.POST:
        try:
            user = User.objects.get(username='Guest')
            new_reservation = Reservation.objects.create(
                user=user,
                date=datetime.date.today() + datetime.timedelta(days=1),
                time=datetime.time(hour=11, minute=0),
            )
            message = 'Reservation created successfully!'
        except Exception as e:
            message = f'Error creating reservation: {e}'

    reservations = Reservation.objects.all().order_by('-id')

    if request.method == 'POST' and 'update_button' in request.POST:
        try:
            reservation_id = int(request.POST['update_id'])
            reservation_to_update = Reservation.objects.get(id=reservation_id)
            reservation_to_update.date = datetime.date.today() + datetime.timedelta(days=2)
            reservation_to_update.save()
            message = 'Reservation updated successfully!'
        except Exception as e:
            message = f'Error updating reservation: {e}'

    if request.method == 'POST' and 'delete_button' in request.POST:
        try:
            reservation_id = int(request.POST['delete_id'])
            reservation_to_delete = Reservation.objects.get(id=reservation_id)
            reservation_to_delete.delete()
            message = 'Reservation deleted successfully!'
        except Exception as e:
            message = f'Error deleting reservation: {e}'

    context = {'message': message, 'reservations': reservations}
    return render(request, 'test_crud.html', context)