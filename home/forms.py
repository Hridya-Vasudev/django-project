from django import forms
from.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'booking_date':forms.DateInput(attrs={'type':'date'})
        }
        labels={
            'p_name':"Patient Name: ",
            'p_phone':"Patient Phone: ",
            'p_email':"Patient Email Id: ",
            'doc_name':"Doctor Name: ",
            'booking_date':"Booking Date: "
        }
