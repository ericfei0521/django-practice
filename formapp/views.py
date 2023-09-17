from django.shortcuts import render
from .forms import UserSignUp


# Create your views here.
def index(request):
    return render(request, "basicApp/index.html")


# def form_name_view(request):
#     form = forms.FormName()
#     if request.method == "POST":
#         form = forms.FormName(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             print(f"name: {name} , email: {email}")

#     return render(request, "basicApp/formPage.html", {"form": form})


def user(request):
    form = UserSignUp()
    if request.method == "POST":
        form = UserSignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")

    return render(request, "basicApp/user.html", {"form": form})
