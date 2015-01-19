
"""
Definition of urls for iamhungry.
相对定位有两个作用： 
1、在保证元素原始占位不变的情况下，偏移元素，这个有很多地方用得到，
    比如微调元素的位置，还有就是有种居中的实现方式就是利用了这一点； 
2、作为子元素的定位父元素，也就是说，如果某个元素相对定位了，那其下的子孙元素，
    在没有其他定位元素隔离的情况下，将以这个父元素的包围框为基准做绝对定位。
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
           
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about$', 'app.views.about', name='about'),
    url(r'^faq$', 'app.views.faq', name='faq'),
    url(r'^blog$', 'app.views.blog', name='blog'),
    url(r'^termofuse$', 'app.views.termofuse', name='termofuse'),
    url(r'^addyourrestaurant$', 'app.views.addyourrestaurant', name='addyourrestaurant'),
    url(r'^career$', 'app.views.career', name='career'),
    url(r'^signup$', 'app.views.signup', name='signup'),
    url(r'^signup$', 'app.views.privacy', name='privacy'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),

    url(r'^logout$', 'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },  name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),)
