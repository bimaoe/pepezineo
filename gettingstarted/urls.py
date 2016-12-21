from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^create-cards', hello.views.create_cards, name='create-cards'),
    url(r'^insert-cards-into-db', hello.views.insert_cards_into_db, 
        name='insert-cards-into-db'),
    url(r'^test', hello.views.test, name='test'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
