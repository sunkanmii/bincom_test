from django.shortcuts import render
from . models import PollingUnit, Lga
from collections import defaultdict

# Create your views here.
def home(req):
    polling_units = PollingUnit.objects.all()
    
    context = {
        'polling_units': polling_units
    }
    
    
    
    return render(req, 'index.html', context)

def pollResults(req):
    polling_units = PollingUnit.objects.all()
    lgas = Lga.objects.all()
    
    lga_ids = {}
    
    lga_names_ids = {}
    
    for item in polling_units:
        if item.lga_id == 0:
            continue
        if item.lga_id not in list(lga_ids.keys()):
            lga_ids[item.lga_id] = 1
        else:
            lga_ids[item.lga_id] += 1
    for item in lga_ids.keys():
        for innerItem in lgas:
            if item == innerItem.lga_id:
                lga_names_ids[innerItem.lga_name] = lga_ids[item]
                break

    sorted_lga_names_ids = dict(sorted(lga_names_ids.items()))
    
    context = {
        'lga_names_ids': sorted_lga_names_ids
    }
    
    return render(req, 'pollResults.html', context)


def newPollUnits(req):
    if req.method == 'POST':
        polling_unit_id = req.POST['polling_unit_id']
        ward_id = req.POST['ward_id']
        lga_id = req.POST['lga_id']
        uniquewardid = req.POST['uniquewardid']
        polling_unit_number = req.POST['polling_unit_number']
        polling_unit_name = req.POST['polling_unit_name']
        polling_unit_description = req.POST['polling_unit_description']
        lat = req.POST['lat']
        long = req.POST['long']
        entered_by_user = req.POST['entered_by_user']
        date_entered = req.POST['date_entered']
        user_ip_address = req.POST['user_ip_address']