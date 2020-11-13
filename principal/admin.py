from django.contrib import admin
from principal.models import (
    Cliente, Lanche, Almoço, Janta, Vinho, Sobremesa, ItemDoEstoque, Bebida, Reserva
)

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Lanche)
admin.site.register(Almoço)
admin.site.register(Janta)
admin.site.register(Vinho)
admin.site.register(Sobremesa)
admin.site.register(ItemDoEstoque)
admin.site.register(Bebida)
admin.site.register(Reserva)
