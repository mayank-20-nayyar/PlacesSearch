from django.shortcuts import render
from myapp.models import Places
from myapp.forms import PlaceForm

def place(request):
    file = open('new.txt','w') 
    file.write('this is before if')
    if request.method == "POST":
        file.write('h')
        MyPlace = PlaceForm(data = request.POST)
        file.write(str(MyPlace.is_valid()))
        if MyPlace.is_valid():
            placename  = MyPlace.cleaned_data['placename']
            print(placename)
            file.write('placename')
            places = Places.objects.create(place_name = placename,)
            place_back = Places.objects.all()
            file.close()
            
    else:
        MyPlace = PlaceForm()
        file.write('this is else')
    return render(request, "place_back.html", {'place_back':place_back})


