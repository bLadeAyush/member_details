from django.shortcuts import render
from members.models import Member
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def Show_members(request):
    all_members = Member.objects.all()
    
    template = loader.get_template('members.html')
    context = {
        'mymembers': all_members,
    }
    return HttpResponse(template.render(context, request))

def Member_Detail(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('member_details.html')
    context = {
        'Members': mymember,
    }
    return HttpResponse(template.render(context, request))