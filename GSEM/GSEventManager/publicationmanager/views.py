from django.shortcuts import render
from django.core.mail import send_mail


def request_email(request):
	return render(request, 'request_email.html')
	
def confirm_email(request):
	data = request.POST.get('textbox1') 
	send_mail('You Have Been Invited To A Georgia Southern Event', 'Please follow the link to see more information: ' + request.META.get('HTTP_REFERER', ''), 'chanukyabadrifofo@gmail.com', [data], fail_silently=False)
	return render(request, 'confirm_email.html')
