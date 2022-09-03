from django.db.models import Q
from .models import Profile, Skill

def searchprofile(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
        print('SEARCH',search_query)
        

    skills=Skill.objects.filter(name__iexact=search_query)
    profiles=Profile.objects.distinct().filter(
        Q(name__contains=search_query)|
        Q(short_intro__contains=search_query)|
        Q(username__contains=search_query)|
        Q(bio__contains=search_query)|
        Q(skill__in=skills)
            )
    
    return profiles,search_query
