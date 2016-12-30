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
    url(r'^dashboard', hello.views.dashboard, name='dashboard'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^insert-cards-into-db', hello.views.insert_cards_into_db, 
        name='insert-cards-into-db'),
    url(r'^insert-or-update-my-card-into-db', 
        hello.views.insert_or_update_my_card_into_db, 
        name='insert-or-update-my-card-into-db'),
    url(r'^update-card', hello.views.update_card, name='update-card'),
    url(r'^upgrade-card', hello.views.upgrade_card, name='upgrade-card'),
    url(r'^test', hello.views.test, name='test'),
    url(r'^admin/', include(admin.site.urls)),
]
