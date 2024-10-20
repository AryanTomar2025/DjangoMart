from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from . models import Product , Customer , Cart
from . forms import CustomerRegistrationForm ,CustomerProfileForm
from django.db.models import Count
from django.contrib import messages 
# Create your views here.
def home(request):
    return render(request,"app/home.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)  
        return render(request, 'app/productdetail.html', locals())
    

class Customer_Registration_View(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registration Successfully")
        else:
            messages.warning(request, "Error! User Registration Failed")  

        return render(request, 'app/customerregistration.html', locals())
    


    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):    
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations !  Profile Updated Successfully")
        else:
            messages.warning(request,"Some error occur")    
        return render(request,'app/profile.html',locals())
            


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateaddress.html',locals())
        
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()  
            messages.success(request, "Address updated successfully!")
            return redirect('address')  
        else:
            messages.warning(request, "Error updating address.")  
            
        return redirect('address')


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)

    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount+value
    totolamount = amount+40    
    return render(request ,'app/addtocart.html',locals())    


def checkout(request):
    pass



def plus_cart(request):
    pass


