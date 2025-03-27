from django.urls import path, include

urlpatterns = [
    path('', include('mi_app.urls')),  # Asegura que incluye las rutas de mi_app
]
