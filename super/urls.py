from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
	# logins and registration
	path('', views.welcome, name = "welcome"),
	path('register/', views.register, name = "register"),
	path('local_register/', views.localResidentRegister, name = "local_register"),
	path('organiser_register/', views.organiserRegister, name = "organiser_register"),
	path('login/', views.loginChoose, name="login"),
	path('local_login/', views.localResidentLogin, name="local_login"),
	path('organiser_login/', views.organiserLogin, name="organiser_login"),
	path('logout/', views.logout_view, name="logout"),

	# organiser pages
	path("organiser_home/", views.organiserHome, name="organiser_home"),
	path("add_course/", views.addCourse, name="add_course"),
	path("add_lecturer/", views.addLecturer, name="add_lecturer"),
	path("add_news/", views.add_news, name="add_news"),
	path("add_schedule/", views.addSchedule, name="add_schedule"),
	path("add_sport/", views.addSport, name="add_sport"),
	path("add_venue/", views.addVenue, name="add_venue"),
	path("add_event/", views.addEvent, name="add_event"),

	path("update_sport/<int:id>/", views.updateSport, name="update_sport"),
	path("delete_sport/<int:id>/", views.deleteSport, name="delete_sport"),
	path("delete_news/<int:id>/", views.deleteNews, name="delete_news"),
	path("delete_event/<int:id>/", views.deleteEvents, name="delete_event"),
	path("delete_venue/<int:id>/", views.deleteVenue, name="delete_venue"),
	path("delete_schedule/<int:id>/", views.deleteSchedule, name="delete_schedule"),

	path("update_news/<str:pk>/", views.edit_news, name="update_news"),
	path("show_news/", views.show_articles_all, name="show_news"),
	path("editCourse/<str:pk>/", views.editCourse, name="editCourse"),



	# local resident pages
	path('home/', views.localResidentHome, name='home'),
	path("settings/", views.accountSettings, name = "settings"),
	path("checkout/", views.payment, name = "checkout"),
	path("course_details/", views.CourseDetails, name = "course_details"),


	# pages 
	path("news/", views.news, name="news"),
	path("events/", views.events, name="events"),
	path("sports/", views.sports, name="sports"),
	path("venue/", views.venue, name="venue"),
	path("schedule/", views.schedule, name="schedule"),
	path("about/", views.about, name="about"),
	path("search/", views.searchEverything, name="search"),


	# password resets
	path("reset_password/", auth_views.PasswordResetView.as_view(template_name="super/password_reset.html"), name="reset_password"),
	path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="super/password_reset_sent.html"), name="password_reset_done"),
	path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="super/password_reset_form.html"), name="password_reset_confirm"),
	path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="super/password_reset_done.html"), name="password_reset_complete"),


]
