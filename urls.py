from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
from clientes.models import Cliente
#from django.contrib.auth.views import login, logout
#from solanaABM import views
#from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solanaABM010.views.home', name='home'),
    # url(r'^solanaABM010/', include('solanaABM010.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url('^/$', redirect_to, {'url': '/admin', 'permanent': False}),
    #url(r'/$', include(admin.site.urls)),
   # url(r'^admin/treemenus/', include('treemenus.admin_urls')), 
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^login/', include(auth.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    #(r'^a/','pruebas.views.main'),
#    url(r'^admin_tools/', include('admin_tools.urls')),
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

    
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )



urlpatterns += patterns('',
    (r'^grappelli/', include('grappelli.urls')),
)

