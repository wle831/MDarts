from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^standings/', 'signups.views.standings', name='standings'),
    url(r'^about/', 'signups.views.about', name='about'),
    url(r'^statistics/', 'signups.views.statistics', name='statistics'),
    url(r'^schedules/', 'signups.views.schedules', name='schedules'),
    url(r'^contact/', 'signups.views.contact', name='contact'),
    url(r'^register/', 'signups.views.register', name='register'),

)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
								document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
								document_root=settings.MEDIA_ROOT)