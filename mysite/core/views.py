from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm, TestimonialForm
from .models import MenuItem, Testimonial, GalleryImage


def index(request):
    menu_items = MenuItem.objects.all()
    testimonials = Testimonial.objects.filter(is_approved=True)
    gallery_images = GalleryImage.objects.all()
    return render(request, 'core/index.html', {
        'menu_items': menu_items,
        'testimonials': testimonials,
        'gallery_images': gallery_images
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Check if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your message has been sent successfully.'
                })
            else:
                messages.success(request, 'Thank you! Your message has been sent successfully.')
                return redirect('index')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': 'Please correct the errors in the form.'
                })

    return render(request, 'core/contact.html', {'form': ContactForm()})


def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your testimonial has been submitted and is pending approval.')
            return redirect('index')
    else:
        form = TestimonialForm()

    return render(request, 'core/submit_testimonial.html', {'form': form})