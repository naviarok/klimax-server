from django.shortcuts import render, redirect
from .forms import ConsultationForm, MessageForm


def landing(request):
    return_message = 0
    if request.method == 'POST':
        print('asdf')
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return_message = 1
        else:
            return redirect('fail')
            
    else:
        form = MessageForm()
    if return_message:
        context = {'form': form, 'message':'Your message has been sent successfully!'}
    else:
        context = {'form': form, 'message':''}
    return render(request, 'index.html', context)
 
def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            return redirect('fail')
    else:
        form = ConsultationForm()

    context = {'form': form}
    return render(request, 'form.html', context)
 
def success(request):
    return render(request, 'success.html')

def fail(request):
    return render(request, 'fail.html')