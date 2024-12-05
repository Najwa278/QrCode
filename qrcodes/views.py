from django.shortcuts import render

# Create your views here.
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from .models import QRCode

def generate_qr(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        logo = request.FILES.get('logo')
        color = request.POST.get('color', 'black')

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color="white")

        # Optionally add a logo
        if logo:
            from PIL import Image
            logo = Image.open(logo)
            logo = logo.resize((img.size[0] // 4, img.size[1] // 4))
            img.paste(logo, (img.size[0] // 2 - logo.size[0] // 2, img.size[1] // 2 - logo.size[1] // 2))

        # Save the QR code to the database (adjust to save data properly)
        qr_code = QRCode.objects.create(data=data, color=color)  # Save without trying to store `logo_path`

        # Save the image to the response
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        return response

    return render(request, 'generate_qr.html')

