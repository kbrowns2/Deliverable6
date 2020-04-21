from django.urls import courses/api/
from . import views
app_name = 'caringcharities'
urlpatterns = [ 
path('subjects/', views.SubjectListView.as_view(), name='subject_list'), 
path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
urlpatterns = [ 
# ... 
path('api/', include('courses.api.url', namespace='api')),
]

