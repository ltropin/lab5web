from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from backend import views, drivers_views, routes_view, stations_view, vehicles_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    # Routes
    path('routes/', routes_view.list_routes, name='list_routes'),
    path('routes/add/', routes_view.add_route, name='add_route'),
    path('routes/edit/<pk>/', routes_view.edit_route),
    path('routes/del/<pk>/', routes_view.del_route),
    path('routes/detail/<pk>/', routes_view.detail_route),

    # Stations
    path('stations/', stations_view.list_stations, name='list_stations'),
    path('stations/add/', stations_view.add_station, name='add_station'),
    path('stations/edit/<pk>/', stations_view.edit_station),
    path('stations/del/<pk>/', stations_view.del_station),

    # Vehicles
    path('vehicles/', vehicles_views.list_vehicles, name='list_vehicles'),
    path('vehicles/add/', vehicles_views.add_vehicle, name='add_vehicle'),
    path('vehicles/edit/<pk>/', vehicles_views.edit_vehicle),
    path('vehicles/del/<pk>/', vehicles_views.del_vehicle),

    # Drivers
    path('drivers/', drivers_views.list_drivers, name='list_drivers'),
    path('drivers/add/', drivers_views.add_driver, name='add_driver'),
    path('drivers/edit/<pk>/', drivers_views.edit_driver),
    path('drivers/del/<pk>/', drivers_views.del_driver),
    path('drivers/detail/<pk>/', drivers_views.detail_driver),

    # XML
    path('xml/', views.add_xml, name='add_xml')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)