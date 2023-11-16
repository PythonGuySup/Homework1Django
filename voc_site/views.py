from django.shortcuts import render, redirect
import voc_site.logic as logic
# Create your views here.
def home_page(request):
    return render(request, "home.html")
def table(request):
    context = {
        "words": logic.read_from_file()
    }
    return render(request, "table.html", context)
def add_word(request):
    if request.method == "GET":
        return render(request, "add_word.html")
    elif request.method == "POST":
        data = request.POST
        logic.add_to_file(data["english_word"], data["russian_word"])
        return redirect("home")
