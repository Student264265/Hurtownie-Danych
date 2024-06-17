from django.shortcuts import render
from django.http import HttpResponse
from .models import HDData
from .forms import CreateNewData
from .KNN import k_nearest_neighbours



# Create your views here.

def home(response):
    queryset = HDData.objects.order_by('x')

    msg = ""

    if response.method == "POST":
        form = CreateNewData(response.POST)

        if form.is_valid():
            _x = form.cleaned_data["x"]
            _y = form.cleaned_data["y"]



            _k = form.cleaned_data["k"]
            _criteria = [s[0] for s in HDData.Shape.choices]
            _data = [[hd.shape, hd.x, hd.y] for hd in queryset.all()]
            _test = [_x, _y]

            try:
                _shape = k_nearest_neighbours(_k, _criteria, _data, _test)

                obj = HDData(x=_x, y=_y, shape=_shape)
                obj.save()
            except Exception as inst:
                print(inst)
                msg = "Nope"
    else:
        form = CreateNewData()



    titles = [s[1] for s in HDData.Shape.choices]
    data = []

    for s in HDData.Shape.choices:
        s_i = s[0]
        sh_arr = []
        for hd in queryset.filter(shape=s_i):
            sh_arr.append([hd.x, hd.y])
        data.append(sh_arr)



    context = {
        "titles": titles,
        "data": data,
        "form": form,
        "msg": msg,
    }
    return render(response, "main/home.html", context)