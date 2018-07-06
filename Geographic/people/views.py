from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegisterFormModel
from .models import Person
# Create your views here.
def register(request):
    fathers = Person.objects.filter(children__isnull=True)
    form=RegisterFormModel(fathers,request.POST or None)
    if form.is_valid():
        # data = form.cleaned_data
        # person = Person.objects.create(
        #     first_name=data['first_name'],
        #     father=data['father']
        # )

        # for country in data['nacionalidad']:
        #     person.nacionalidad.add(country)
        person = form.save()
        return JsonResponse(
            {
                'name':person.first_name,
                'father':str(person.father),
                'nacionalidad':','.join([str(country) for country in person.nacionalidad.all()])
            }

        )
    return render(request,"people/register.html",{'form':form})
