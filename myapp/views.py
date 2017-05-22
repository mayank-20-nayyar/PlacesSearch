from django.shortcuts import render
from myapp.models import Places
from myapp.forms import PlaceForm

def place(request):
    file = open('new2.txt','w') 
    file.write('this is before if')
    if request.method == "POST":
        file.write('h')
        
        MyPlace = PlaceForm(data = request.POST)
        file.write(str(request.POST))
        file.write(str(MyPlace.is_valid()) + str(MyPlace.errors) + str(type(MyPlace.errors)))
        if MyPlace.is_valid():
            placename  = MyPlace.cleaned_data['placename']
            print(placename)
            file.write(placename)
            #places = Places.objects.create(place_name = placename)
            place = Places()
            place.place_name = placename
            place.save()
            place_back = Places.objects.all()
            file.write(str(place_back) + ' this is there inside database')  
            file.close()
            
    else:
        MyPlace = PlaceForm()
        file.write('this is else')
    return render(request, "place_back.html", {'place_back':place_back})


