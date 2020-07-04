from django.contrib.auth import login, authenticate, logout
from . forms import OrganiserSignUpForm, LocalResidentSignUpForm
from . models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
# pages
from django.core.paginator import Paginator
# search 
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def welcome(request):
    context = {}
    return render(request, "super/landing_page.html", context)

def news(request):
	article = models.Article.objects.all()

	paginator = Paginator(article, 8)
	page_number = request.GET.get("page")
	article = paginator.get_page(page_number)




	context = {"article":article}

	return render(request, "super/news.html", context)


# about page
def about(request):
	context = {}
	return render(request, "super/about.html", context)
# Search everything
def searchEverything(request):
	try:
		query = request.GET.get("all")
		article = models.Article.objects.filter(Q(title__icontains = query))
		sport = models.Sport.objects.filter(Q( sport_name__icontains = query))
		# results = models.Schedule.objects.filter(Q( course_name__icontains = query))
		venue = models.Venue.objects.filter(Q( venue_name__icontains = query))
		event = models.Event.objects.filter(Q( event_name__icontains = query))
	except:
		query = None
	if query:
		context = {"article":article,"sport":sport, "venue":venue, "event":event, "query":query}
		return render(request, 'super/everything_search.html', context)
	else:
		return render(request, 'super/everything_search.html')

# Venues
def venue(request):
	venue = models.Venue.objects.all().order_by("capacity")
	paginator = Paginator(venue, 3)
	page_number = request.GET.get("page")
	venue = paginator.get_page(page_number)
	
	context={"venue":venue}
	return render(request, "super/venue.html", context)


# main shedule page
def schedule(request):
	schedule = models.Schedule.objects.all()
	context = {"schedule":schedule}
	return render(request, "super/schedule.html", context)

# event page
def events(request):
	event = models.Event.objects.all()
	context = {"event":event}
	return render(request, "super/events.html", context)


# sports page
def sports(request):
	sport = models.Sport.objects.all().order_by("sport_name")
	context={"sport":sport}
	return render(request, "super/sports.html", context)

# where users will choose what type of users they are
def register(request):
	return render(request, "super/register.html")



def localResidentRegister(request):
	model = User
	form = LocalResidentSignUpForm()
	if request.method == 'POST':
		form = LocalResidentSignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/login')
			messages.info(request, "Successful registration")
		else:
			messages.info(request,"Something went wrong")

	context = {"form":form}
	return render(request, 'super/local_register.html', context)
#----------------------------------------------------------------

# after the user logs in they are reditected here
@login_required(login_url='/local_login/')
def localResidentHome(request):
	course = models.Course.objects.all()
	lecturer = models.Lecturer.objects.all()

	# search
	try:
		query = request.GET.get("q")
		results = models.Course.objects.filter(Q( course_name__icontains = query))
	except:
		query = None
	if query:
		context = {"results":results, "query":query}
		return render(request, 'super/local_residents_home.html', context)
	else:
		context = {"course":course, "lecturer":lecturer}
		return render(request, 'super/local_residents_home.html', context)


@login_required(login_url="/login_login")
def CourseDetails(request):
	mycourse = models.Enrollment.objects.all()
	context = {"mycourse":mycourse}
	return render(request, "super/Enrolled.html", context)

#------------------------------------------------------------------------


def organiserRegister(request):
	model = User
	form  = OrganiserSignUpForm()
	if request.method == "POST":
		form = OrganiserSignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/login')

	context = {"form":form}
	return render(request, 'super/organiser_register.html', context)



# where users will choose what type of users they are
def loginChoose(request):
	return render(request, "super/login.html")




def localResidentLogin(request):
	form = AuthenticationForm()

	if request.method=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None :
				login(request,user)
				return redirect('/home')
			else:
				messages.error(request,"Invalid username or password")
		else:
			messages.error(request,"Invalid username or password")

	context = {"form":form}

	return render(request, 'super/local_login.html',context)



# account settings
@login_required(login_url='/local_login/')
def accountSettings(request):
	user = request.user
	form_pic = forms.LocalResidentProfileForm(instance=user)
	if request.method == "POST":
		form_pic = forms.LocalResidentProfileForm(request.POST, request.FILES, instance=user)
		if form_pic.is_valid():
			form_pic.save()
	context = {"form_pic":form_pic}
	return render(request, "super/local_residents_settings.html", context)



# pay for course
@login_required(login_url='/local_login/')
def payment(request):
	context = {}
	return render(request, "super/pay_for_course.html")



# =============+================++++++==============++==================+=======++=====
# organiser workspace

# organiser login 
def organiserLogin(request):
	form = AuthenticationForm()

	if request.method=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None :
				login(request,user)
				return redirect('/organiser_home')
			else:
				messages.error(request,"Invalid username or password")
		else:
			messages.error(request,"Invalid username or password")

	context = {"form":form}

	return render(request, 'super/organiser_login.html',context)



# logged in organiser home
@login_required(login_url='/organiser_login/')
def organiserHome(request):
	course = models.Course.objects.all()
	students = models.LocalResident.objects.all()

	total_courses = course.count()
	total_students = students.count()
	context = {"total_courses":total_courses, "total_students":total_students}
	return render(request, "super/organiser_home.html", context)



@login_required(login_url='/organiser_login/')
def addCourse(request):
	# course
	courseForm = forms.CourseForm()
	if request.method == "POST":
		courseForm = forms.CourseForm(request.POST, request.FILES)
		if courseForm.is_valid():
			try:
				courseForm.save()
				messages.success(request,"Successfully added Course")
				print("course added {-_-}")
				return redirect("/organiser_home")
			except:
				print("course not added ")
				messages.warning(request, "did not add course")
		else:
			courseForm = forms.CourseForm()
	context = {"courseForm":courseForm}
	return render(request, "super/organiser/course.html", context)

@login_required(login_url='/organiser_login/')
def addLecturer(request):
	# lecturer
	lecturerForm = forms.LecturerForm()
	if request.method == "POST":
		lecturerForm = forms.LecturerForm(request.POST, request.FILES)
		if lecturerForm.is_valid():
			try:
				lecturerForm.save()
				messages.success(request,"Successfully added lecturer")
				return redirect("/organiser_home")
			except:
				messages.warning(request, "did not add lecturer")
		else:
			lecturerForm = forms.LecturerForm()
	context = {"lecturerForm":lecturerForm}
	return render(request, "super/organiser/lecturer.html", context)

@login_required(login_url='/organiser_login/')
def addSchedule(request):
	# Schedule
	scheduleForm = forms.ScheduleForm()
	if request.method == "POST":
		scheduleForm = forms.ScheduleForm(request.POST, request.FILES)
		if scheduleForm.is_valid():
			try:
				scheduleForm.save()
				messages.success(request,"Successfully added Schedule")
				print("course added {-_-}")
				return redirect("/organiser_home")
			except:
				print("course not added ")
				messages.warning(request, "did not add Schedule")
		else:
			scheduleForm = forms.ScheduleForm()

	context = {"scheduleForm":scheduleForm}
	return render(request, "super/organiser/schedule.html", context)

@login_required(login_url='/organiser_login/')
def addSport(request):
# sport
	sportForm = forms.SportForm()
	if request.method == "POST":
		sportForm = forms.SportForm(request.POST, request.FILES)
		if sportForm.is_valid():
			try:
				sportForm.save()
				messages.success(request,"Successfully added Sport")
				print("course added {-_-}")
				return redirect("/organiser_home")
			except:
				print("course not added ")
				messages.warning(request, "did not add Sport")
		else:
			sportForm = forms.SportForm()
			messages.warning(request, "Invalid method")
	context = {"sportForm":sportForm}
	return render(request, "super/organiser/sports.html", context)

@login_required(login_url='/organiser_login/')
def updateSport(request, id):
	update = models.Sport.objects.get(id=id)
	updateForm  = forms.SportForm(instance=update)
	if request.method == "POST":

		updateForm  = forms.SportForm(request.POST, request.FILES)
		if updateForm.is_valid():
			updateForm.save()
			messages.success(request,"Successfully updated Sport")
			return redirect("/organiser_home")

	context = {"updateForm":updateForm, "update":update}
	return render(request, "super/organiser/updateSport.html", context)

@login_required(login_url='/organiser_login/')
def deleteSport(request, id):
	sport = models.Sport.objects.get(id=id)
	sport.delete()
	return redirect("/sports")
	

@login_required(login_url='/organiser_login/')
def deleteNews(request, id):
	article = models.Article.objects.get(id=id)
	article.delete()
	return redirect("/news")

@login_required(login_url='/organiser_login/')
def deleteEvents(request, id):
	event = models.Event.objects.get(id=id)
	event.delete()
	return redirect("/events")

@login_required(login_url='/organiser_login/')
def deleteVenue(request, id):
	delete_venue = models.Venue.objects.get(id=id)
	delete_venue.delete()
	return redirect("/venue")

@login_required(login_url='/organiser_login/')
def deleteSchedule(request, id):
	delete_schedule = models.Schedule.objects.get(id=id)
	delete_schedule.delete()
	return redirect("/schedule")


@login_required(login_url='/organiser_login/')
def add_news(request):
	# Articles insert
	articleForm = forms.ArticleForm()
	if request.method == "POST":
		articleForm = forms.ArticleForm(request.POST, request.FILES)
		if articleForm.is_valid():
			try:
				articleForm.save()
				messages.success(request,"added artile {-_-}")
				return redirect("/organiser_home")
			except:
				messages.warning(request, "did not add article")
		else:
			articleForm = forms.ArticleForm()
	context = {"articleForm":articleForm}
	return render(request, "super/organiser/article.html", context)

@login_required(login_url='/organiser_login/')
def addEvent(request):
	# Event
	eventForm = forms.EventForm()
	if request.method == "POST":
		eventForm = forms.EventForm(request.POST, request.FILES)
		if eventForm.is_valid():
			try:
				eventForm.save()
				messages.success(request,"Successfully added Venue")
				print("course added {-_-}")
				return redirect("/organiser_home")
			except:
				print("course not added ")
				messages.warning(request, "did not add Venue")
		else:
			eventForm = forms.EventForm()

	context = { "eventForm":eventForm}
	return render(request, "super/organiser/event.html", context)

@login_required(login_url='/organiser_login/')
def addVenue(request):
	# Venue
	venueForm = forms.VenueForm()
	if request.method == "POST":
		venueForm = forms.VenueForm(request.POST, request.FILES)
		if venueForm.is_valid():
			try:
				venueForm.save()
				messages.success(request,"Successfully added Venue")
				print("course added {-_-}")
				return redirect("/organiser_home")
			except:
				print("course not added ")
				messages.warning(request, "did not add Venue")
		else:
			venueForm = forms.VenueForm()

	context = {
	 "venueForm":venueForm,
	 }
	return render(request, "super/organiser/venue.html", context)

@login_required(login_url='/organiser_login/')
def edit_news(request, pk):
	edit = forms.ArticleForm()
	context = {"edit":edit}
	return render(request, "super/organiser/article.html", context)

def show_articles_all(request):
	showAll = models.Article.objects.all()
	context = {"showAll":showAll}
	return render(request, "super/organiser/show_articles.html", context)

@login_required(login_url='/organiser_login/')
def editCourse(request, pk):
	edit = forms.CourseForm()
	context = {"edit":edit}
	return render(request, "super/organiser/editCourse.html", context)

# logout the user
@login_required
def logout_view(request):
	logout(request)
	return redirect("/")



