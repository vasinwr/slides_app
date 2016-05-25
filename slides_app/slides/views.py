from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Current, Slides

# Create your views here.

def index(request):
    return render(request, 'slides/index.html') 

def lecturer(request):
    return lecture(request, True)

def student(request):
    return lecture(request, False)

def lecture(request, isLecturer):
    current = get_object_or_404(Current, pk=1)
    '''
    qs = Slides.objects.filter(slide_text=current.slide_name)
    qs = qs.filter(page = current.page)
    slide = qs.reverse()[:1]
    return render(request, 'slides/index.html', {'slide': slide})
    '''
    slide = get_object_or_404(Slides, pk=current.page)
    if(isLecturer):
        return render(request, 'slides/lecture.html', {'slide':slide, 'lecturer':True})
    else:
        return render(request, 'slides/lecture.html', {'slide':slide, 'student':True})

def next_page(request):
    current = get_object_or_404(Current, pk=1)
    current.page += 1
    current.save()
    return lecture(request, True)
#    return HttpResponseRedirect(reverse('slides:lecture', args=(True,)))

def prev_page(request):
    current = get_object_or_404(Current, pk=1)
    current.page -= 1
    current.save()
    return lecture(request, True)
#    return HttpResponseRedirect(reverse('slides:lecture', args=(True,)))
