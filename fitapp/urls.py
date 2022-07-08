from django.urls import path
# from django.conf.paths import path

from . import views


urlpatterns = [
    # OAuth authentication
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path(r'^login/$', views.login, name='fitbit-login'),
    path(r'^complete/$', views.complete, name='fitbit-complete'),
    path(r'^error/$', views.error, name='fitbit-error'),
    path(r'^logout/$', views.logout, name='fitbit-logout'),

    # Subscriber callback for near realtime updates
    path(r'^update/$', views.update, name='fitbit-update'),

    # Fitbit data retrieval
    path(r'^get_data/(?P<category>[\w]+)/(?P<resource>[/\w]+)/$',
        views.get_data, name='fitbit-data'),
    path(r'^get_steps/$', views.get_steps, name='fitbit-steps'),
]
