# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Bus
# from .serializers import BusSerializer


# class BusListView(APIView):
#     def get(self, request):
#         buses = Bus.objects.all()
#         serializer = BusSerializer(buses, many=True)
#         return Response(serializer.data)

# class AddBusView(APIView):
#     def post(self, request):
#         serializer = BusSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # from Feature.models import Bus
# # # Fetch all buses
# # buses = Bus.objects.all()

# # for bus in buses:
# #     print(bus.bus_number, bus.brand, bus.trip)

from django.shortcuts import render, redirect,get_object_or_404
from .models import Bus
from .forms import BusForm


def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

def add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus-list')
    else:
        form = BusForm()
    return render(request, 'add_bus.html', {'form': form})
# Edit Bus View
def edit_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)  # Fetch the bus by its primary key
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('bus-list')  # Redirect to the bus list page
    else:
        form = BusForm(instance=bus)
    return render(request, 'edit_bus.html', {'form': form})

# Delete Bus View
def delete_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        bus.delete()  # Delete the bus from the database
        return redirect('bus-list')
    return render(request, 'delete_bus.html', {'bus': bus})
