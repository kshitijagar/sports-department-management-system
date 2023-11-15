from datetime import datetime
from django.shortcuts import render
from .models import Equipment
from .allotmentmodel import Allotment
from .homemodel import Student
def equipaction(request):
    current_srn = request.GET.get('SRN')
    
    student = Student.objects.get(SRN=current_srn)
    if request.method == 'POST':
        # Handle the equipment selection and allocation logic here
        selected_equipment = request.POST.getlist('selected_equipment')
        print(f'Current SRN: {current_srn}')
          # Get the SRN from the URL parameter
        for equip_id in selected_equipment:
            print(f'Processing equip_id: {equip_id}')  # Debug print statement
            try:
                # equipment = Equipment.objects.get(equipid=equip_id)
                equipment = Equipment.objects.get(equipid=equip_id)
                print(f'Equipment Availability: {equipment.equipid,equipment.equipname,equipment.buydate,equipment.availability}')


                # Check availability
                if equipment.availability > 0:
                    # Update availability
                    equipment.availability -= 1
                    equipment.save()
                    current_time=datetime.now().time()
                    # Create an allotment record
                    allotment = Allotment(equipid=equipment, SRN=student,allot_time=current_time)
                    allotment.save()
                else:
                    # Handle unavailability
                    return render(request, 'error.html', {'message': f'Equipment {equipment.equipname} is not available.'})
            except Equipment.DoesNotExist:
                # Handle non-existent equipment
                return render(request, 'error.html', {'message': f'Equipment with ID {equip_id} does not exist.'})
            
        # Redirect to a success page or display a success message
        return render(request, 'equipments.html', {'SRN': current_srn})

    # Load the initial equipment selection page
    return render(request, 'equipments.html',{'SRN': current_srn})

def return_equip(request):
    current_srn=request.GET.get('SRN')
    if request.method == 'POST':
        equipid = request.POST.get('equipid')
        try:
            allotment = Allotment.objects.get(SRN=current_srn, equipid=equipid)
            allotment.delete()
            equipment=Equipment.objects.get(equipid=equipid)
            equipment.availability+=1
            equipment.save()
            # borrowed_equipment=Allotment.objects.filter(SRN=current_srn)
            # Redirect to the same page after deleting the record
            borrowed_equipment=Allotment.objects.filter(SRN=current_srn)
            return render(request,'returnequip.html', {'SRN':current_srn,'borrowed_equipment':borrowed_equipment})
        except Allotment.DoesNotExist as e:
            print(e)
            # Handle the case where the record does not exist
            return render(request, 'error.html', {'message': 'Allotment record not found.'})
    borrowed_equipment=Allotment.objects.filter(SRN=current_srn)
    return render(request,'returnequip.html',{'SRN':current_srn,'borrowed_equipment':borrowed_equipment})