from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', home_view),
    path('menu/events/', event_view),
    path('events/<int:pk>', displayevent_view),
    path('menu/', menu_view),
    path('menu/achievements/', achievement_view),
    path('achievements/<int:pk>', displayach_view),
    path('menu/projects/', project_view),
    path('projects/<int:pk>', displayproj_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('success/', authenticate_view),
    path('welcome/', home_view),

]
