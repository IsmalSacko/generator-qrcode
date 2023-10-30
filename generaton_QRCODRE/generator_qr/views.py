# Dans votre fichier views.py
from django.http import HttpResponse
from django.shortcuts import render
import qrcode

from generator_qr.forms import QRCodeForm

import qrcode
from django.shortcuts import render
from .forms import QRCodeForm
from django.http import HttpResponse
from io import BytesIO


def index(request):
    return render(request, 'generator_qrcode/index.html')


def generate_qrcode(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            # Créez un objet QRCode
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            # Ajoutez les données que vous souhaitez encoder dans le QR code
            qr.add_data(data)
            qr.make(fit=True)

            # Créez une image QR code à partir des données
            img = qr.make_image(fill_color="black", back_color="white")

            # Enregistrez l'image ou envoyez-la directement en réponse HTTP
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)

            response = HttpResponse(buffer, content_type="image/png")
            return response
    else:
        form = QRCodeForm()

    return render(request, 'generator_qrcode/index.html', {'form': form})
