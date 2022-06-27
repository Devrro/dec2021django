from django.urls import path
from apps.pc_shop.views import PcModelView, PcReadUpdateDestroy

urlpatterns = [
    path('', PcModelView.as_view()),
    path('/<int:pk>', PcReadUpdateDestroy.as_view()),
]