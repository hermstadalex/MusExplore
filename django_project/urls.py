from django.conf.urls import patterns, include, url
import views
from django.template import loader
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^help/', views.help, name='help'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^formtest_start/', views.formtest_start, name='formtest_start'),
    url(r'^results_page/', views.results_page, name='results_page'),
    url(r'^test_loc/', views.test_loc, name='test_loc'),


] 
