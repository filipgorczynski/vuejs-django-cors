from django.http import JsonResponse

def top_rated(request):
    return JsonResponse(
        [
            {
                'title': 'Skazani na Shawshank',
                'year': 1994
            },
            {
                'title': 'Ojciec chrzestny',
                'year': 1972
            },
            {
                'title': 'Ojciec chrzestny II',
                'year': 1974
            },
            {
                'title': 'Mroczny Rycerz',
                'year': 2008
            },
            {
                'title': 'Dwunastu gniewnych ludzi',
                'year': 1957
            }
        ],
        safe=False
    )
