from django.shortcuts import render
from django.utils.timezone import now
from .models import Order
from datetime import timedelta
from django.db.models import Sum
import logging

logger = logging.getLogger(__name__)
def top_customers(req):
    try:
        sixmonths = now()-timedelta(days=180)
        top_customers = (
            Order.objects.filter(order_date__gte=sixmonths).values('customer__username')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
        logger.info(f"Successfully fetched top customers: {top_customers}")
        return render(req, 'customers/top_customers.html', {'top_customers': top_customers})
    except Exception as e:
        logger.error(f"An error occurred while fetching top customers: {str(e)}") 
        return render(req, 'customers/error.html', {'error': str(e)})
