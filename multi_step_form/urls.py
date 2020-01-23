from django.urls import path

from multi_step_form.views import FormStep1, FormStep2, FormStep3

app_name = 'multi_step_form'
urlpatterns = [
    path('', FormStep1.as_view(), name='step_1'),
    path('step-2', FormStep2.as_view(), name='step_2'),
    path('step-3', FormStep3.as_view(), name='step_3'),
]
