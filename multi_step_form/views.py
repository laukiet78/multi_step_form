from django.shortcuts import render
from uuid import uuid4
from django.views.generic import FormView
from django.urls import reverse_lazy
from multi_step_form.models import UserPictures
from multi_step_form.forms import Step1Form, Step2Form, Step3Form

# Create your views here.
class FormStep1(FormView):
    form_class = Step1Form
    success_url = reverse_lazy('multi_step_form:step_2')
    template_name = 'multi_step_form/step1.html'

    def get_initial(self):
        initials = super(FormStep1, self).get_initial()
        initials.update({
            'first_name': self.request.session.get('first_name', None),
            'last_name': self.request.session.get('last_name', None),
        })
        return initials
    
    def form_valid(self, form):
        post_data = self.request.POST
        if form.is_valid():
            self.request.session['first_name'] = post_data['first_name']
            self.request.session['last_name'] = post_data['last_name']
            if not self.request.session.get('user_uuid', None):
                self.request.session['user_uuid'] = str(uuid4())
        return super(FormStep1, self).form_valid(form)
        
        

class FormStep2(FormView):
    form_class = Step2Form
    success_url = reverse_lazy('multi_step_form:step_3')
    template_name = 'multi_step_form/step2.html'

    def get_initial(self):
        initials = super(FormStep2, self).get_initial()
        initials.update({
            'local_address': self.request.session.get('local_address', None),
            'permanent_address': self.request.session.get('permanent_address', None),
        })
        return initials
    
    def form_valid(self, form):
        post_data = self.request.POST
        if form.is_valid():
            self.request.session['local_address'] = post_data['local_address']
            self.request.session['permanent_address'] = post_data['permanent_address']
        return super(FormStep2, self).form_valid(form)


class FormStep3(FormView):
    form_class = Step3Form
    success_url = reverse_lazy('pdf_results:pdf')
    template_name = 'multi_step_form/step3.html'

    def get_context_data(self, **kwargs):
        context_data = super(FormStep3, self).get_context_data(**kwargs)
        user_uuid = self.request.session.get('user_uuid')
        context_data['user_images'] = UserPictures.objects.filter(
            user_uuid=user_uuid)
        return context_data
    
    
    def form_valid(self, form):
        request_files = self.request.FILES.getlist('images')
        if form.is_valid():
            user_uuid = self.request.session.get('user_uuid')
            # clear the last user pictures
            UserPictures.objects.filter(
                user_uuid=user_uuid).delete()
            for image in request_files:
                UserPictures.objects.create(user_uuid=user_uuid,
                    image=image)
        return super(FormStep3, self).form_valid(form)