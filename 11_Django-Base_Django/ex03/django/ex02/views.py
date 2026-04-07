from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime
from .forms import MessageForm

def form_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            nuevo_texto = form.cleaned_data['message']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(settings.HISTORY_LOG_FILE, 'a') as f:
                f.write(f"{timestamp} - {nuevo_texto}\n")
            
            return redirect('ex02:form-view')   # Returns a 302 to client and client asks for `form_view` as GET
    else:
        form = MessageForm() # Si es GET, el formulario aparece vacío

    historic = []
    try:
        with open(settings.HISTORY_LOG_FILE, 'r') as f:
            historic = f.readlines()
    except FileNotFoundError: #To avoid problems whem log file no exits
        pass

    return render(request, 'ex02/index.html', {'form': form, 'historic': historic})
