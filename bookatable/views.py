from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.dispatch import receiver

from allauth.account.forms import UserForm

from .models import Reservation

reservations = Reservation.objects.all()

@login_required
def update_user_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information updated successfully!')
            return redirect('create_reservation')
    else:
        form = UserForm(instance=request.user)
    context = {'form': form}
    return render(request, 'create_reservation.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)

def menu(request):
    context = {}
    return render(request, 'menu.html', context)

def reservation(request):
    context = {'message': 'Your reservation has been successfully created!'}
    return render(request, 'reservation.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def login(request):
    context = {}
    return render(request, 'account/login.html', context)

def logout(request):
    context = {}
    return render(request, 'logout.html', context)

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.name = request.name
            reservation.save()
            return redirect('reservation_success')
        else:
          form = ReservationForm()
    else:
        form = ReservationForm()
    return render(request, 'create_reservation.html', {'form': form})

def read_reservation(request):
    reservations = Reservation.objects.all()
    context = {'reservation': reservations}
    return render(request, 'reservation_list.html', context)

def update_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return render(request, 'reservation_list.html', context)
    else:
        form = ReservationForm(instance=reservation)
    context = {'form': form}
    return render(request, 'update_reservation.html', context)

def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    context = {'reservation': reservation}
    return render(request, 'reservation_confirm_delete.html', context)

def list_reservation(request):
    reservations = Reservation.objects.all()
    context = {'reservation': reservations}
    return render(request, 'reservation_list.html', context)

def reservation_success(request):
    context = {'message': 'Your reservation has been successfully created!'}
    return render(request, 'reservation_success.html', context)

def record(request):
    context = {'message': 'record'}
    return render(request, 'record.html', context)

def my_reservations(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(user=request.user)
    else:
        return render(request, 'not_authenticated.html')

    return render(request, 'my_reservations.html', {'reservations': reservations})

def all_bookings(request):
    if request.user.is_superuser:
        bookings = Reservation.objects.all()
        return render(request, 'my_reservations.html', {'my_reservations': bookings})
    else:
        return render(request, 'unauthorized.html')

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