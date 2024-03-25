from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reservation, User

def home(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(user=request.user)  # Assuming your model
    else:
        reservations = None

    context = {'reservations': reservations}  # Add reservations to context
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def list_reservation(request):
    return render(request, 'list_reservation.html')

def view_reservation(request):
    return render(request, 'view_reservation.html')

def reservation_success(request):
    return render(request, 'reservation_success.html')

def test_crud(request):
    return render(request, 'test_crud.html')
    
    
@login_required
def my_reservations(request):
    if request.method == 'POST':
        user = request.user
        user.profile.name = request.POST['name']
        user.profile.save()
        messages.success(request, 'User information updated successfully!')
        return redirect('my_reservations')

    reservations = Reservation.objects.filter(user=request.user)
    context = {'reservations': reservations}
    return render(request, 'my_reservations.html', context)

@login_required
def create_reservation(request):
    if request.method == 'POST':
        try:
            date = request.POST['date']
            time = request.POST['time']
            number_of_guests = request.POST['number_of_guests']
            occasion = request.POST['occasion']
            

            reservation = Reservation.objects.create(user=request.user, date=date, time=time, number_of_guests=number_of_guests, occasion=occasion)
            messages.success(request, 'Reservation created successfully!')
            return redirect('my_reservations')
        except Exception as e:
            messages.error(request, f'Error creating reservation: {e}')

    return render(request, 'create_reservation.html')

@login_required
def view_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id, user=request.user)
        context = {'reservation': reservation}
        return render(request, 'view_reservation.html', context)
    except Reservation.DoesNotExist:
        messages.error(request, 'Reservation not found!')
        return redirect('my_reservations')

@login_required
def update_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id, user=request.user)
        if request.method == 'POST':
            try:
                reservation.date = request.POST['date']
                reservation.time = request.POST['time']
                reservation.save()
                messages.success(request, 'Reservation updated successfully!')
                return redirect('my_reservations')
            except Exception as e:
                messages.error(request, f'Error updating reservation: {e}')

        context = {'reservation': reservation}
        return render(request, 'update_reservation.html', context)
    except Reservation.DoesNotExist:
        messages.error(request, 'Reservation not found!')
        return redirect('my_reservations')

@login_required
def delete_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id, user=request.user)
        reservation.delete()
        messages.success(request, 'Reservation deleted successfully!')
        return redirect('my_reservations')
    except Reservation.DoesNotExist:
        messages.error(request, 'Reservation not found!')
        return redirect('my_reservations')

@login_required
def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        user.profile.name = request.POST['name']
        user.profile.save()
        messages.success(request, 'User information updated successfully!')
        return redirect('my_reservations')

    return render(request, 'my_reservations.html')
