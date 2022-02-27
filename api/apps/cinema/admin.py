from django.contrib import admin



from .models import Cinema, Hall, Event


admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Event)
