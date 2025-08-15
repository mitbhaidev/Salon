from django.shortcuts import render
from .models import Appointment, Service,Contact
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime
from django.db import IntegrityError

def home(request):
    gallery_images = [f'images/gallery{i}.jpg' for i in range(1, 3)]
    return render(request, 'home.html', {'gallery_images': gallery_images})


def book_appointment(request):
    now = timezone.localtime()
    Appointment.objects.filter(date__lt=now.date()).delete()
    Appointment.objects.filter(date=now.date(), time__lt=now.time()).delete()

    services = Service.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service_id = request.POST.get('service')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            time_obj = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            return render(request, 'book.html', {
                'services': services,
                'error': "Invalid date or time format."
            })

        if date_obj < now.date():
            return render(request, 'book.html', {
                'services': services,
                'error': "You cannot select a past date."
            })
        elif date_obj == now.date() and time_obj <= now.time():
            return render(request, 'book.html', {
                'services': services,
                'error': "You cannot select a past time."
            })

        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            return render(request, 'book.html', {
                'services': services,
                'error': "Invalid service selected."
            })

        if Appointment.objects.filter(service=service, date=date_obj, time=time_obj).exists():
            return render(request, 'book.html', {
                'services': services,
                'error': "This time slot is already booked. Please select another."
            })

        try:
            appointment = Appointment.objects.create(
                name=name,
                email=email,
                phone=phone,
                service=service,
                date=date_obj,
                time=time_obj
            )
        except IntegrityError:
            return render(request, 'book.html', {
                'services': services,
                'error': "This slot just got booked by someone else."
            })

        # Send email to admin
        send_mail(
            subject="New Appointment Booking",
            message=(
                f"Name: {name}\nEmail: {email}\nPhone: {phone}\n"
                f"Service: {service.name}\nDate: {date_obj}\nTime: {time_obj}"
            ),
            from_email="mitbhai989@gmail.com",
            recipient_list=["mitbhai989@gmail.com"],
        )


        return render(request, 'success.html', {'appointment': appointment})

    return render(request, 'book.html', {'services': services})


def contact(request):
    success = False
    error = None

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            error = "Please fill in all required fields."
        else:
            # Save to DB
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            # Send email
            try:
                send_mail(
                    subject="We Received Your Message",
                    message=f"Hi {name},\n\nThank you for contacting us. We received your message:\n\n\"{message}\"\n\nWe will get back to you shortly.",
                    from_email="mitbhai989@gmail.com",
                    recipient_list=[email],
                )
                success = True
            except Exception as e:
                error = f"Error sending email: {str(e)}"

    return render(request, "contact.html", {"success": success, "error": error})