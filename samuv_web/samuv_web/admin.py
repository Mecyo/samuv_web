from django.contrib import admin
from .models import Usuario
from .models import Profissional
from .models import Paciente
from .models import Doenca
from .models import Ferida
from .models import Caracteristica_da_ferida
from .models import Tecnica
from .models import Atendimento
from .models import Imagem

#para tornar models visível no site
admin.site.register(Usuario)
admin.site.register(Profissional)
admin.site.register(Paciente)
admin.site.register(Doenca)
admin.site.register(Ferida)
admin.site.register(Caracteristica_da_ferida)
admin.site.register(Tecnica)
admin.site.register(Atendimento)
admin.site.register(Imagem)
