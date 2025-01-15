from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

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
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL,null= True )
    picture = models.ImageField(upload_to='pokemon_images')

    def __str__(self):
       return self.name
   
       