from django.contrib import admin
from .models import cliente, Atencion
@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'tipo_mascota', 'email')
    search_fields = ('nombre', 'telefono', 'tipo_mascota', 'email')

    
    
@admin.register(Atencion)
class atencionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'monto', 'observacion')
    search_fields = ('fecha', 'hora', 'monto', 'observacion')

    @admin.display(description='monto')
    def precio_formateado(self, obj):
        return f"$ {obj.monto:,}".replace(",", ".")