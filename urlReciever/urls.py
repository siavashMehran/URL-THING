



from urlReciever.views import home, result_page, short_redirect
from django.urls.conf import path


urlpatterns = [
    path('', home),
    path('result-<int:shortUrldRandint>', result_page, name='resultPage'),
    path('<int:shorturl>', short_redirect, name='redirectRoute'),
]
