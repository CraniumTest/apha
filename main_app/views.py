from django.shortcuts import render
from .models import HealthRecord

def view_health_records(request):
    records = HealthRecord.objects.filter(user_id=request.user.id)
    return render(request, 'view_records.html', {'records': records})
