from django.urls import path, include, re_path
from .views import SendView,ConfirmMessageSend

app_name = "contact"

urlpatterns = [
    path('send/', SendView.as_view(), name="send"),
    path('confirm_message_send/', ConfirmMessageSend.as_view(), name="confirm_message_send"),

]
