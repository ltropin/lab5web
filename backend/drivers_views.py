from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from backend.forms import *
from django.contrib import messages

def add_driver(request):
    if request.method == 'GET' and request.user.is_staff:
        return render(request, 'drivers/add_driver.html', context={'form': DriverForm()})
    elif request.user.is_staff:
        form = DriverForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Водитель успешно добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении водителя!')
        return redirect('list_drivers')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_drivers')


def list_drivers(request):
    return render(request, 'drivers/list_drivers.html', context={'drivers': Driver.objects.all()})


def edit_driver(request, pk):
    if request.method == 'GET' and request.user.is_staff:
        driver = Driver.objects.get(pk=pk)
        form = DriverForm(instance=driver)
        return render(request, 'drivers/edit_driver.html', context={'form': form})
    elif request.user.is_staff:
        driver = Driver.objects.get(pk=pk)
        form = DriverForm(data=request.POST, files=request.FILES, instance=driver)
        print(form.errors)
        if form.is_valid() or len(request.FILES) == 0:
            incst = form.save(commit=False)
            incst.save()
            messages.info(request, 'Водитель успешно обновлен!')
        else:
            messages.error(request, 'Ошибка при изменении водителя!')
        return redirect('list_drivers')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_drivers')


def del_driver(request, pk):
    if request.method == 'POST' and request.user.is_staff:
        Driver.objects.get(pk=pk).delete()
        messages.info(request, 'Водитель успешно удален')
        return redirect('list_drivers')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_drivers')


def detail_driver(request, pk):
    if request.method == 'GET' and request.user.is_staff:
        driver = Driver.objects.get(pk=pk)
        return render(request, 'drivers/detail_driver.html', context={'driver': driver})
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_drivers')