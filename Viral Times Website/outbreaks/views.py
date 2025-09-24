from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import modelform_factory
from .models import Outbreak, Report

OutbreakForm = modelform_factory(Outbreak, exclude=[])
ReportForm = modelform_factory(Report, exclude=[])

def new_outbreak(request):
    OutbreakForm = modelform_factory(Outbreak, exclude=[])
    form = OutbreakForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('outbreaks')

    return render(request, 'outbreaks/new_outbreak.html', {'form': form})

def new_report(request):
    ReportForm = modelform_factory(Report, exclude=[])
    form = ReportForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('report_list')

    return render(request, 'reports/new_report.html', {'form': form})

def welcome(request):
    return render(request, 'outbreaks/welcome.html')

def about(request):
    return HttpResponse("This website provides information about historical and modern outbreaks.")

def outbreaks(request):
    outbreaks_count = Outbreak.objects.count()
    all_outbreaks = Outbreak.objects.all()
    return render(request, 'outbreaks/outbreak_list.html', {
        'num_outbreaks': outbreaks_count,
        'outbreaks': all_outbreaks
    })

def outbreak_details(request, outbreak_name):
    outbreak = get_object_or_404(Outbreak, name=outbreak_name)
    return render(request, 'outbreaks/outbreak_detail.html', {
        'outbreak': outbreak,
        'outbreak_name': outbreak.name,
        'disease': outbreak.disease,
        'date_range': outbreak.date_range,
        'death_low': outbreak.death_toll_low,
        'death_high': outbreak.death_toll_high,
        'transmission': outbreak.transmission_type,
        'regions': outbreak.regions_affected,
        'symptoms': outbreak.symptoms,
        'impact': outbreak.impact
    })

def report_list(request):
    reports= Report.objects.all()
    reports_count = Report.objects.count()
    outbreaks_count = Outbreak.objects.count()
    return render(request, 'reports/report_list.html', {
        'num_reports': reports_count,
        'num_outbreaks': outbreaks_count,
        'reports': reports
    })

def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_detail.html', {
        'report': report,
    })
