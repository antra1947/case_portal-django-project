from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Case, Document, Hearing, Notification
from .forms import CaseForm, DocumentForm, HearingForm

# =====================
# LOGIN (ANY USER)
# =====================
def open_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to authenticate
        user = authenticate(request, username=username, password=password)

        if user is None:
            # Optional: create user if it doesn't exist
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.save()
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'core/login.html')


# =====================
# DASHBOARD
# =====================
@login_required
def dashboard(request):
    cases = Case.objects.filter(created_by=request.user)
    ongoing_cases = cases.filter(status="Ongoing")
    closed_cases = cases.filter(status="Closed")

    context = {
        "cases": cases,
        "ongoing_cases": ongoing_cases,
        "closed_cases": closed_cases,
    }
    return render(request, "core/dashboard.html", context)


# =====================
# CASE LIST
# =====================
@login_required
def case_list(request):
    cases = Case.objects.filter(created_by=request.user)
    return render(request, "core/case_list.html", {"cases": cases})


# =====================
# CASE DETAIL
# =====================
@login_required
def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk, created_by=request.user)
    return render(request, "core/case_detail.html", {"case": case})


# =====================
# ADD CASE
# =====================
@login_required
def add_case(request):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.created_by = request.user
            case.save()
            return redirect("case_list")
    else:
        form = CaseForm()
    return render(request, "core/add_case.html", {"form": form})


# =====================
# ADD DOCUMENT
# =====================
@login_required
def add_document(request, case_id):
    case = get_object_or_404(Case, pk=case_id, created_by=request.user)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.uploaded_by = request.user
            doc.case = case
            doc.save()
            return redirect("case_detail", pk=case.id)
    else:
        form = DocumentForm()
    return render(request, "core/add_document.html", {"form": form, "case": case})


# =====================
# ADD HEARING
# =====================
@login_required
def add_hearing(request, case_id):
    case = get_object_or_404(Case, pk=case_id, created_by=request.user)
    if request.method == "POST":
        form = HearingForm(request.POST)
        if form.is_valid():
            hearing = form.save(commit=False)
            hearing.case = case
            hearing.save()

            Notification.objects.create(
                user=case.created_by,
                message=f"Hearing scheduled for case '{case.title}' on {hearing.hearing_date}"
            )
            return redirect("case_detail", pk=case.id)
    else:
        form = HearingForm()
    return render(request, "core/add_hearing.html", {"form": form, "case": case})


# =====================
# NOTIFICATIONS
# =====================
@login_required
def notifications(request):
    notes = Notification.objects.filter(user=request.user).order_by('-date')
    return render(request, "core/notifications.html", {"notifications": notes})


# =====================
# DOCUMENT LIST
# =====================
@login_required
def document_list(request, case_id):
    case = get_object_or_404(Case, pk=case_id, created_by=request.user)
    documents = Document.objects.filter(case=case)
    return render(request, "core/document_list.html", {"case": case, "documents": documents})


# =====================
# HEARING LIST
# =====================
@login_required
def hearing_list(request, case_id):
    case = get_object_or_404(Case, pk=case_id, created_by=request.user)
    hearings = Hearing.objects.filter(case=case)
    return render(request, "core/hearing_list.html", {"case": case, "hearings": hearings})
