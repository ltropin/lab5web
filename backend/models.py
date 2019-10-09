from django.db import models


class Route(models.Model):
    BUS = 'BS'
    SHUTTLE = 'SE'
    TRAM = 'TM'
    TYPE_CHOICE = [
        (BUS, 'Автобус'),
        (SHUTTLE, 'Маршрутное такси'),
        (TRAM, 'Трамвай')
    ]

    code = models.CharField(max_length=50)
    start = models.TimeField()
    end = models.TimeField()
    type_route = models.CharField(max_length=2, choices=TYPE_CHOICE, default=BUS)
    map_city = models.ImageField(default='maps/none.png', upload_to='maps', unique=True)

    def __str__(self):
        return f"Code: {self.name}"

class Station(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    BUS = 'BS'
    SHUTTLE = 'SE'
    TRAM = 'TM'
    TYPE_CHOICE = [
        (BUS, 'Автобус'),
        (SHUTTLE, 'Маршрутное такси'),
        (TRAM, 'Трамвай')
    ]

    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    type_vehicle = models.CharField(max_length=2, choices=TYPE_CHOICE, default=BUS)
    route = models.ForeignKey(Route, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    vahicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(default='avatars/none.png', upload_to='avatars', unique=True)


    def __str__(self):
        return self.name