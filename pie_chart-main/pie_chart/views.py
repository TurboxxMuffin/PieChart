from django.shortcuts import render


def index(request):
    components_of_air = [
        {"label": "Nitrogen", "y": 78},
        {"label": "Oxygen", "y": 21},
        {"label": "Carbon Dioxide", "y": 0.04},
        {"label": "Other Gases\n(mostly Argon)", "y": 0.96},
    ]

    return render(request, 'index.html', {"components_of_air": components_of_air})