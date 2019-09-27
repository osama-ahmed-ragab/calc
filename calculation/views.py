from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import operat

def calc_op(request):
    if request.method == 'POST':
        form = operat(request.POST)
        result = 0
        if form.is_valid():
            n1 = form.cleaned_data['num1']
            op = form.cleaned_data['operation']
            n2 = form.cleaned_data['num2']
            if op == '+' :
                result = n1 + n2 
                return render(request,'body/base.html',{'result':result})
            elif op == '-' :
                result = n1 - n2
                return render(request,'body/base.html',{'result':result})
            elif op == '*' :
                result = n1 * n2
                return render(request,'body/base.html',{'result':result})
            elif op == '/' :
                result = n1 / n2
                return render(request,'body/base.html',{'result':result})
            else :
                result= 'put the right foken operation'
                return render(request,'body/base.html',{'result':result})
        else :
            form = operat()
            result= 'all fields is required'
            return render(request,'body/base.html',{'form': form, 'result':result})
    else :
        return render(request,'body/base.html', {'result':result})
