from django.contrib import admin
from .models import Species, SNP, Sample, Annotation

admin.site.register(Species)
admin.site.register(SNP)
admin.site.register(Sample)
admin.site.register(Annotation)
