from django.db import models

# Modello Corso 

class Corso(models.Model):
    """Il modello generico di un corso"""
    titolo = models.CharField(max_length=35)
    descrizione = models.CharField(max_length=20)
    data_inizio = models.DateField(blank=True)
    data_fine = models.DateField(blank=True)
    posti_disponibili = models.IntegerField(default=0,blank=True)

    
    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Corso"
        verbose_name_plural = "Corsi" 
