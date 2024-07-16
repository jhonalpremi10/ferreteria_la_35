from django.shortcuts import render

def page_list(request):
    return render(request, 'pages/page_list.html')

def page_detail(request, page_id):
    return render(request, 'pages/page_detail.html', {'page_id': page_id})



