from datetime import datetime
from django.shortcuts import render
from .models import Court
from .bookingmodel import Booking
from home.models import Student

def courtaction(request):
    current_srn=request.GET.get('SRN')
    student = Student.objects.get(SRN=current_srn)
    if request.method == 'POST':
        # Handle the equipment selection and allocation logic here
        selected_court = request.POST.getlist('selected_court')
        print(f'Current SRN: {current_srn}')
          # Get the SRN from the URL parameter
        for court_id in selected_court:
            print(f'Processing court_id: {court_id}')  # Debug print statement
            try:
                # equipment = Equipment.objects.get(equipid=equip_id)
                court = Court.objects.get(courtid=court_id)
                
                # Check availability
                if court.avail > 0:
                    # Update availability
                    court.avail -= 1
                    court.save()
                    current_time=datetime.now().time()
                    # Create an allotment record
                    booking = Booking(courtid=court, SRN=student,start_time=current_time)
                    booking.save()
                else:
                    # Handle unavailability
                    return render(request, 'error.html', {'message': f'Court {court.courttype} is not available.'})
            except Court.DoesNotExist:
                # Handle non-existent equipment
                return render(request, 'error.html', {'message': f'Court with ID {court_id} does not exist.'})
            
        # Redirect to a success page or display a success message
        return render(request, 'courts.html', {'SRN': current_srn})

    # Load the initial equipment selection page
    return render(request, 'courts.html',{'SRN': current_srn})

def return_court(request):
    current_srn=request.GET.get('SRN')
    student = Student.objects.get(SRN=current_srn)
    if request.method == 'POST':
        court_id = request.POST.get('courtid')
        try:
            booking = Booking.objects.get(SRN=student, courtid=court_id)
            booking.delete()
            court=Court.objects.get(courtid=court_id)
            court.avail+=1
            court.save()
            # borrowed_equipment=Allotment.objects.filter(SRN=current_srn)
            # Redirect to the same page after deleting the record
            occupied_court=Booking.objects.filter(SRN=student)
            return render(request,'returncourt.html', {'SRN':current_srn,'occupied_court':occupied_court})
        except Booking.DoesNotExist as e:
            print(e)
            # Handle the case where the record does not exist
            return render(request, 'error.html', {'message': 'Booking record not found.'})
    occupied_court=Booking.objects.filter(SRN=student)
    return render(request,'returncourt.html',{'SRN':current_srn,'occupied_court':occupied_court})
