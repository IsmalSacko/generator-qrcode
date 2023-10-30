from django import forms


class QRCodeForm(forms.Form):
    data = forms.CharField(label='Données pour le QR Code', max_length=255)

