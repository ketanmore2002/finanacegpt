from django.contrib import admin

from .models import *

admin.site.register(messages)
admin.site.register(NoteBook)
admin.site.register(stocks)
admin.site.register(Transactions)


