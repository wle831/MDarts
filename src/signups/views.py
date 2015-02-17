from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

from .forms import SignUpForm

def home(request):

	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()

	return render_to_response("signup.html", locals(), context_instance=RequestContext(request))

def standings(request):

	return render_to_response("standings.html", locals(), context_instance=RequestContext(request))

def about(request):

	return render_to_response("about.html", locals(), context_instance=RequestContext(request))

def contact(request):

	return render_to_response("contact.html", locals(), context_instance=RequestContext(request))

def schedules(request):

	return render_to_response("schedules.html", locals(), context_instance=RequestContext(request))

def statistics(request):

	return render_to_response("statistics.html", locals(), context_instance=RequestContext(request))

def home(request):

	return render_to_response("base.html", locals(), context_instance=RequestContext(request))