from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def converte(numDecimal, base):
    vnumDecimal = 10
    if numDecimal != 0:
        numConvertido = ""
        while numDecimal > 0:
            resto = numDecimal % base
            numConvertido = str(resto) + numConvertido
            numDecimal = numDecimal // base
    else:
        numConvertido = "0"
    return numConvertido