from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from backend.forms import *
from django.contrib import messages

def add_route(request):
    if request.method == 'GET' and request.user.is_staff:
        return render(request, 'routes/add_route.html', context={'form': RouteForm()})
    elif request.user.is_staff:
        form = RouteForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, 'Маршрут успешно добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении маршрута!')
        return redirect('list_routes')

    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_routes')


def list_routes(request):
    return render(request, 'routes/list_routes.html', context={'routes': Route.objects.filter(pk__gt=1).all()})


def edit_route(request, pk):
    route = Route.objects.get(pk=pk)
    if request.method == 'GET' and request.user.is_staff:
        form = RouteForm(instance=route)
        return render(request, 'routes/edit_route.html', context={'form': form})
    elif request.user.is_staff:
        form = RouteForm(data=request.POST, files=request.FILES, instance=route)
        if form.is_valid() or len(request.FILES) == 0:
            incst = form.save(commit=False)
            incst.save()
            messages.info(request, 'Маршрут успешно обновлен!')
        else:
            messages.error(request, 'Ошибка при изменении маршрута!')
        return redirect('list_routes')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_routes')


def del_route(request, pk):
    if request.method == 'POST' and request.user.is_staff:
        Route.objects.get(pk=pk).delete()
        messages.info(request, 'Маршрут успешно удален')
        return redirect('list_routes')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_routes')


def detail_route(request, pk):
    if request.method == 'GET' and request.user.is_staff:
        route = Route.objects.get(pk=pk)
        return render(request, 'routes/detail_route.html', context={'route': route})
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('list_routes')