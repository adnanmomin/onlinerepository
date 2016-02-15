from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from models import RepositoryUploaddata
from form import UploadForm
# Create your views here.

def get_content(request):
    content = RepositoryUploaddata.objects.order_by('file_name')
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            if request.FILES['upload_data']._size < 1024:
                size = request.FILES['upload_data']._size
            else:
                size = request.FILES['upload_data']._size /1024
            name = request.FILES['upload_data']
            file = RepositoryUploaddata(upload_data = request.FILES['upload_data'],
                                        file_name = name, file_size = size)
            file.save()
            return HttpResponseRedirect('uploaded')
    else:
        upload_form = UploadForm()
    return render_to_response('Home.html', { 'files': content, 'upload_form': upload_form },
                              context_instance=RequestContext(request))

def upload_success(request):
        return render_to_response('uploaded.html')

def not_allowed(request):
        return render_to_response('accessdenied.html')