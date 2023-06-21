from django.urls import path
from szartapp.views import index, item_response, show_paintings, show_ceramics, contact_response, aboutme_response

urlpatterns = [
    path('szart/', index, name='szart'),
    path('ceramika/', show_ceramics, name='ceramika'),
    path('malarstwo/', show_paintings, name='malarstwo'),
    path('omnie/', aboutme_response, name='omnie'),
    path('kontakt/', contact_response, name='kontakt'),
    path('item/<int:id>', item_response, name='item'),
]
