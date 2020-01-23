from django.shortcuts import render

from multi_step_form.models import UserPictures
from wkhtmltopdf.views import PDFTemplateView

# Create your views here.
class PDFResults(PDFTemplateView):
    template_name = 'pdf_results/pdf.html'
    file_name = 'user_details.pdf'
    show_content_in_browser = True
    cmd_options = {
        'margin-top': '5mm',
    }
    
    def get_context_data(self, **kwargs):
        context_data = super(PDFResults, self).get_context_data(**kwargs)
        user_uuid = self.request.session.get('user_uuid')
        context_data.update({
            'first_name': self.request.session.get('first_name'),
            'last_name': self.request.session.get('first_name'),
            'local_address': self.request.session.get('first_name'),
            'permanent_address': self.request.session.get('first_name'),
            'user_images': UserPictures.objects.filter(user_uuid=user_uuid)
        })
        del self.request.session['first_name']
        del self.request.session['last_name']
        del self.request.session['local_address']
        del self.request.session['permanent_address']
        del self.request.session['user_uuid']
        return context_data
    