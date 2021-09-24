from django.db import models

# Create your models here.

class Buku(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    judul = models.CharField(max_length=100, null=False)
    pengarang = models.CharField(max_length=100, null=False)
    penerbit = models.CharField(max_length=100, null=False)
    tahun = models.IntegerField(null=False)

    def __str__(self):
        return self.judul

    class Meta:
        db_table = 'buku'