from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
from django.db import models

POKEMON_TYPES = (
    ('A', 'Agua'),
    ('F', 'Fuego'),
    ('T', 'Tierra'),
    ('P', 'Planta'),
    ('E', 'Eléctrico'),
    ('L', 'Lagartija'),
)

class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=POKEMON_TYPES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to='pokemon_images', null=True, blank=True)

    def __str__(self):
       return self.name
   
       