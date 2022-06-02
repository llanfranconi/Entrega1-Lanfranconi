from django import forms


class Usuario_formulario(forms.Form):
    nombre_usuario = forms.CharField()
    email_usuario = forms.EmailField()


class Juego_formulario(forms.Form):
    nombre_juego = forms.CharField()
    genero_juego = forms.CharField()
    desarrollador = forms.CharField()


class Review_formulario(forms.Form):
    nombre_autor = forms.CharField()
    titulo_review = forms.CharField()
    contenido_review = forms.CharField(widget=forms.Textarea)
    puntaje_review = forms.IntegerField()
    juego_review = forms.CharField()

class Buscar_por_juego(forms.Form):
    nombre_juego = forms.CharField()

class Buscar_por_autor(forms.Form):
    nombre_autor = forms.CharField()
