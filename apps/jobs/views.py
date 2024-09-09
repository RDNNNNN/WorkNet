from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from lib.models.paginate import paginate_queryset

from .forms.jobs_form import JobForm
from .models import Job


def index(request):
    jobs = Job.objects.order_by("-id")
    return render(request, "jobs/index.html", {"jobs": jobs})



def show(request, id):
    job = get_object_or_404(Job, pk=id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("jobs:show", job.id)
        else:
            return render(request, "jobs/edit.html", {"form": form, "job": job})
    return render(request, "jobs/show.html", {"job": job})


def edit(request, id):
    job = get_object_or_404(Job, pk=id)
    form = JobForm(instance=job)
    return render(request, "jobs/edit.html", {"form": form, "job": job})


def delete(request, id):
    job = get_object_or_404(Job, pk=id)
    job.mark_delete()
    return redirect("jobs:index")
