from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Car, Brand, Testimonial, Partner, TeamMember, ContactMessage

def home(request):
    featured_cars = Car.objects.filter(is_featured=True, is_available=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    partners = Partner.objects.filter(is_active=True)

    context = {
        'featured_cars': featured_cars,
        'testimonials': testimonials,
        'partners': partners,
    }
    return render(request, 'home.html', context)

def car_list(request):
    # Get all available cars
    cars = Car.objects.filter(is_available=True)

    # Get filter parameters
    brand_id = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    transmission = request.GET.get('transmission')
    fuel_types = request.GET.getlist('fuel_type')
    seats = request.GET.get('seats')
    sort = request.GET.get('sort', 'newest')

    # Apply filters
    if brand_id:
        cars = cars.filter(brand_id=brand_id)
    
    if min_price:
        cars = cars.filter(price_per_day__gte=min_price)
    
    if max_price:
        cars = cars.filter(price_per_day__lte=max_price)
    
    if transmission:
        cars = cars.filter(transmission=transmission)
    
    if fuel_types:
        cars = cars.filter(fuel_type__in=fuel_types)
    
    if seats:
        cars = cars.filter(seats=seats)

    # Apply sorting
    if sort == 'price_asc':
        cars = cars.order_by('price_per_day')
    elif sort == 'price_desc':
        cars = cars.order_by('-price_per_day')
    elif sort == 'rating':
        cars = cars.order_by('-rating')
    else:  # newest
        cars = cars.order_by('-created_at')

    # Pagination
    paginator = Paginator(cars, 6)  # Show 6 cars per page
    page = request.GET.get('page')
    cars = paginator.get_page(page)

    # Get all brands and unique seat options for filters
    brands = Brand.objects.all()
    seats_options = Car.objects.values_list('seats', flat=True).distinct().order_by('seats')

    context = {
        'cars': cars,
        'brands': brands,
        'seats_options': seats_options,
        'selected_brand': brand_id,
        'min_price': min_price,
        'max_price': max_price,
        'transmission': transmission,
        'selected_fuel_types': fuel_types,
        'selected_seats': seats,
        'sort': sort,
        'fuel_types': Car.FUEL_TYPE_CHOICES,
    }
    return render(request, 'cars/car_list.html', context)

def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    similar_cars = Car.objects.filter(
        Q(brand=car.brand) | Q(transmission=car.transmission),
        is_available=True
    ).exclude(id=car.id)[:3]

    if request.method == 'POST':
        # Handle review submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if name and email and rating and comment:
            Review.objects.create(
                car=car,
                name=name,
                email=email,
                rating=rating,
                comment=comment
            )
            messages.success(request, 'Thank you for your review!')
            return redirect('car_detail', slug=slug)
        else:
            messages.error(request, 'Please fill in all fields.')

    context = {
        'car': car,
        'similar_cars': similar_cars,
    }
    return render(request, 'cars/car_detail.html', context)

def about(request):
    team_members = TeamMember.objects.filter(is_active=True)
    context = {
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and phone and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'contact.html')
