
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('technology/',views.technology,name='technology'),
    path('contact/',views.contact,name='contact'),
    # path('service/', include('service.urls',namespace='service')),
    path('cloud-transformation-and-management/', views.cloud,name='cloud'),
    path('big-data/', views.bigData,name='bigData'),
    path('data-analtics/', views.dataAnalysis,name='dataAnalysis'),
    path('devOps/', views.devOps,name='devOps'),
    path('iot/', views.iot,name='iot'),
    path('ML/', views.ml,name='ml'),
    path('AI/', views.ai,name='ai'),
    path('Data Security/', views.dataSecurity,name='dataSecurity'),
    path('Cyber Security/', views.cyber,name='cyber'),
    path('UI-UX/', views.uiux,name='uiux'),
    path('Software Development/', views.software,name='software'),
    path('Application Service/', views.application,name='application'),


    path('crm/', views.crm,name='crm'),
    path('eLearning/', views.eLearning,name='eLearning'),
    path('ecommerce/', views.ecommerce,name='ecommerce'),
    path('erp/', views.erp,name='erp'),
    path('SmartFarming/', views.SmartFarming,name='SmartFarming'),
    path('hospital-management-system/', views.hospital,name='hospital'),
    path('asset-management/', views.assetManagement,name='assetManagement'),
    path('pos/', views.pos,name='pos'),
    path('supply-chain-management/', views.chain,name='chain'),
    path('human-resources/', views.human,name='human'),
    # path('solution/', include('solution.urls',namespace='solution')),    
        
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)