from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from backend.forms import *
from django.contrib import messages

def add_station(request):
    if request.method == 'GET' and request.user.is_staff:
        return render(request, 'stations/add_station.html', context={'form': StationForm()})
    elif request.user.is_staff:
        form = StationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Станция успешно добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении станции!')
        return redirect('add_station')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_stations')


def list_stations(request):
    return render(request, 'stations/list_stations.html', context={'stations': Station.objects.all()})


def edit_station(request, pk):
    station = Station.objects.get(pk=pk)
    if request.method == 'GET' and request.user.is_staff:
        form = StationForm(instance=station)
        return render(request, 'stations/edit_station.html', context={'form': form})
    elif request.user.is_staff:
        form = StationForm(data=request.POST, instance=station)
        if form.is_valid():
            incst = form.save(commit=False)
            incst.save()
            messages.info(request, 'Станция успешно обновлен!')
        else:
            messages.error(request, 'Ошибка при изменении станции!')
        return redirect('list_stations')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_stations')


def del_station(request, pk):
    if request.method == 'POST' and request.user.is_staff:
        Station.objects.get(pk=pk).delete()
        messages.info(request, 'Станция успешно удалена')
        return redirect('list_stations')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_stations')