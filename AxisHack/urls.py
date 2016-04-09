"""AxisHack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Views
    url(r'^$', 'merchants.views.index'),
    url(r'^details$', 'merchants.views.details'),
    url(r'^declarations$', 'merchants.views.declarations'),
    url(r'^confirmation$', 'merchants.views.confirmation'),
    url(r'^getkit$', 'merchants.views.getkit'),
    #validations urls
    url(r'^validations/account$', 'merchants.validations.account_no'),
    url(r'^validations/customer$', 'merchants.validations.customer_id'),
    url(r'^validations/company$', 'merchants.validations.company_name'),
    url(r'^validations/pincode$', 'merchants.validations.pincode'),
    url(r'^validations/website$', 'merchants.validations.website'),
    url(r'^validations/verify$', 'merchants.validations.verify'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
