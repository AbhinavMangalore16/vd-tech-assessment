from django.shortcuts import render
from django.utils.timezone import now
from .models import Order
from datetime import timedelta
from django.db.models import Sum

# Create your views here.
def top_customers(req):
    sixmonths = now()-timedelta(days=180)
    top_customers = (
        Order.objects.filter(order_date__gte=sixmonths).values('customer__username')
        .annotate(total_spent=Sum('total_amount'))
        .order_by('-total_spent')[:5]
    )
    return render(req, 'customers/top_customers.html', {'top_customers': top_customers})
