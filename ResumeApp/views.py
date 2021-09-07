from django.shortcuts import render
from ResumeApp.models import Resume
from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateResponseMixin


# Create your views here.


def resumeData(request,id):
    resume_data = Resume.objects.get(id=id)

    content = {
        'resume_data':resume_data
    }

    return render(request,'template.html',content)


class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Resume
    template_name = 'user_detail.html'

def displayName(request):
    displayData=Resume.objects.all()
    content = {
        'displaydata':displayData
    }

    return render(request,'home.html',content)

def ResumeForm(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        number=request.POST.get('number')
        gender=request.POST.get('gender')
        state=request.POST.get('state')
        summary=request.POST.get('summary')
        ssc_year=request.POST.get('ssc_year')
        ssc_school=request.POST.get('ssc_school')
        ssc_board=request.POST.get('ssc_board')
        ssc_aggregate=request.POST.get('ssc_aggregate')
        hsc_year=request.POST.get('hsc_year')
        hsc_school=request.POST.get('hsc_school')
        hsc_board=request.POST.get('hsc_board')
        hsc_aggregate=request.POST.get('hsc_aggregate')
        ug_year=request.POST.get('ug_year')
        ug_collage=request.POST.get('ug_collage')
        ug_board=request.POST.get('ug_board')
        ug_aggregate=request.POST.get('ug_aggregate')
        technical_skill=request.POST.get('technical_skill')
        project=request.POST.get('project')
        internship=request.POST.get('internship')
        certificate=request.POST.get('certificate')
        language_known=request.POST.get('language_known')
        hobbies=request.POST.get('hobbies')
        r=Resume(Name=name,Email=email,Dob=dob,Number=number,Gender=gender,Birth_place=state,Summary=summary,
               Ssc_year=ssc_year,Ssc_school=ssc_school,Ssc_board=ssc_board,Ssc_aggregate=ssc_aggregate,Hsc_year=hsc_year,
               Hsc_school=hsc_school,Hsc_board=hsc_board,Hsc_aggregate=hsc_aggregate,Ug_year=ug_year,Ug_collage=ug_collage,
               Ug_board=ug_board,Ug_aggregate=ug_aggregate,Technical_skill=technical_skill,Project=project,
               Internship= internship,Certificate=certificate,Language_known=language_known,Hobbies=hobbies)
        r.save()

    return render(request,'resumeForm.html')