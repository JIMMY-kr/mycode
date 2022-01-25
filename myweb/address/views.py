from django.shortcuts import render, redirect
from address.models import Address

def home(request):
    #select * from address_address order by name;
    items=Address.objects.order_by('name')
    return render(request, 'address/list.html', \
                  {'items':items, 'address_count':len(items)})

def write(request):
    return render(request, 'address/write.html')

def insert(request): #폼에 입력한 값들이 request에 저장
    # request.POST['변수명'] post 방식으로 전달된 데이터
    # request.GET['변수명'] get 방식으로 전달된 데이터
    addr=Address(name=request.POST['name'], tel=request.POST['tel'], \
                 email=request.POST['email'], address=request.POST['address'])
    addr.save() #insert, 레코드 저장 완료
    return redirect('/address')

def detail(request):
    id = request.GET['idx']
    addr = Address.objects.get(idx=id)
    return render(request, 'address/detail.html', {'addr':addr})

def update(request):
    id=request.POST['idx']
    addr = Address(idx=id, name=request.POST['name'], \
                   tel=request.POST['tel'], email=request.POST['email'], \
                   address=request.POST['address'])
    addr.save()
    return redirect('/address')

def delete(request):
    id=request.POST['idx']
    Address.objects.get(idx=id).delete()
    return redirect('/address')