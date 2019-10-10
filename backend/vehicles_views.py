from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from backend.forms import *
from django.contrib import messages

def add_vehicle(request):
    if request.method == 'GET' and request.user.is_staff:
        return render(request, 'vehicles/add_vehicle.html', context={'form': VehicleForm()})
    elif request.user.is_staff:
        form = VehicleForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Транспортное средство успешно добавлено!')
        else:
            messages.error(request, 'Ошибка при добавлении транспортного средства!')
        return redirect('add_vehicle')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_vehicles')

def list_vehicles(request):
    return render(request, 'vehicles/list_vehicles.html', context={'vehicles': Vehicle.objects.all()})


def edit_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'GET' and request.user.is_staff:
        form = VehicleForm(instance=vehicle)
        return render(request, 'vehicles/edit_vehicle.html', context={'form': form})
    elif request.user.is_staff:
        form = VehicleForm(data=request.POST, instance=vehicle)
        if form.is_valid():
            incst = form.save(commit=False)
            incst.save()
            messages.info(request, 'Транспортное средство успешно обновлено!')
        else:
            messages.error(request, 'Ошибка при изменении транспортного средства!')
        return redirect('list_vehicles')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_vehicles')


def del_vehicle(request, pk):
    if request.method == 'POST' and request.user.is_staff:
        Vehicle.objects.get(pk=pk).delete()
        messages.info(request, 'Транспортное средство успешно удалено')
        return redirect('list_vehicles')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_vehicles')