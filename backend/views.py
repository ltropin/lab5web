from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from backend.forms import *
from django.contrib import messages
from xml.dom import minidom as md

def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'GET' and request.user.is_anonymous:
        return render(request, 'signin.html', context={'form': SignInForm()})
    elif request.user.is_anonymous:
        username = request.POST['username']
        password = request.POST['password']
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user_active = authenticate(username=username, password=password)
            if not(user_active is None):
                messages.info(request, 'Вы успешно авторизовались!')
                login(request, user_active)
                return redirect('index')
            else:
                messages.error(request, 'Не верный логин или пароль!')
                return render(request, 'signin.html', context={'form': SignInForm(data=request.POST)})
        messages.error(request, 'Ошибка при заполнении формы авторизации!')
        return render(request, 'signin.html', context={'form': SignInForm()})
    messages.warning(request, 'У вас нет доступа к этой странице!')
    return redirect('index')


# ASd2345gl23asfLsd12
def signup(request):
    if request.method == 'GET' and request.user.is_anonymous:
        return render(request, 'signup.html', context={'form': SignUpForm()})
    elif request.user.is_anonymous:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Вы успешно зарегистрировались!')
        else:
            messages.error(request, 'Ошибка при заполнении формы')
            return render(request, 'signup.html', context={'form': SignUpForm()})
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('signup')
        login(request, user)
        messages.info(request, 'Вы автоматически вошли после регистарции!')
    messages.warning(request, 'У вас нет доступа к этой странице.')
    return redirect('index')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'Вы успешно вышли!')
        return redirect('index')
    else:
        messages.error(request, 'Пользователь не авторизован')
    return redirect('index')

def add_xml(request):
    if request.method == 'GET' and request.user.is_staff:
        return render(request, 'add_xml.html', context={'form': XMLForm()})
    elif request.user.is_staff:
        form = XMLForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            incst = form.cleaned_data['xml']
            resultXml = incst.read()
            doc = md.parseString(resultXml)

            stations = doc.getElementsByTagName('data')[0].getElementsByTagName('stations')
            vehicles = doc.getElementsByTagName('data')[0].getElementsByTagName('vehicles')
            route = Route.objects.get(pk=request.POST['route'])
            listNamesStations = []
            for station in stations:
                names = station.getElementsByTagName('name')
                positions = station.getElementsByTagName('position')[0].firstChild.data
                for name, position in zip(station.getElementsByTagName('name'), station.getElementsByTagName('position')):
                    r_name, r_position = name.firstChild.data, position.firstChild.data
                    new_station = Station(name=r_name, position=r_position, route=route)
                    new_station.save()
                    listNamesStations.append(r_name)

            listNamesVehicles = []
            for vehicle in vehicles:
                names = vehicle.getElementsByTagName('name')
                capacities = vehicle.getElementsByTagName('capacity')
                type_vs = vehicle.getElementsByTagName('type')
                for name, capacity, type_v in zip(names, capacities, type_vs):
                    r_name, r_capacity, r_type = name.firstChild.data, capacity.firstChild.data, type_v.firstChild.data
                    new_vehicle = Vehicle(name=r_name, capacity=r_capacity, type_vehicle=r_type, route=route)
                    new_vehicle.save()
                    listNamesVehicles.append(r_name)

            str_stations = ', '.join(listNamesStations)
            str_vehicles = ', '.join(listNamesVehicles)
            messages.info(request, f'XML файл успешно загружен для маршрута {route}')
            messages.info(request, f'Станции: {str_stations}')
            messages.info(request, f'Транспортные средства: {str_vehicles}')
            return redirect('add_xml')
        messages.warning(request, 'У вас нет доступа к этой странице.')
        return redirect('add_xml')

