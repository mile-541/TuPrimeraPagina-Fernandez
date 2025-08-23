from django.db import models
from django.utils import timezone

# Create your models here

class Dueño(models.Model):
    """Datos del dueño de la/s mascota/s."""
    nombre = models.CharField("Nombre del dueño", max_length=50)
    apellido = models.CharField("Apellido del dueño", max_length=50)
    telefono = models.IntegerField("Teléfono del dueño")
    email = models.EmailField("Correo electrónico del dueño", max_length=50)

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nTeléfono: {self.telefono}\nEmail: {self.email}"
    
    def listar_mascotas(self):
        """Lista las mascotas del dueño indicado."""
        nombres_mascotas = []
        for mascota in self.mascota_set.all():
            nombres_mascotas.append(mascota.nombre)
        return f"Mascotas de {self}: {nombres_mascotas}"

class Mascota(models.Model):
    """Datos de la mascota."""
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    nombre = models.CharField("Nombre de la mascota", max_length=50)
    especie = models.CharField("Especie del animal", max_length=50)
    sexo = models.CharField("Sexo del animal", max_length=1)
    edad = models.IntegerField("Edad del animal", default=0)

    def __str__(self):
        return f"***Datos de {self.nombre}***\nDueño: {self.dueño}\nEspecie: {self.especie}\nSexo: {self.sexo}\nEdad: {self.edad}"
    
    def turnos_pendientes(self):
        """Lista los turnos pendientes de la mascota indicada."""
        lista_turnos_pendientes = []
        for turno in self.turno_set.all():
            if turno.fecha > timezone.now():
                lista_turnos_pendientes.append(f"{turno.fecha} - {turno.motivo}")
        return f"Turnos pendientes de {self}: {lista_turnos_pendientes}"

    def turnos_historicos(self):
        """Lista los turnos históricos de la mascota indicada."""
        lista_turnos_historicos = []
        for turno in self.turno_set.all():
            if turno.fecha < timezone.now():
                lista_turnos_historicos.append(f"{turno.fecha} - {turno.motivo}")
        return f"Turnos históricos de {self}: {lista_turnos_historicos}"
        

class Turno(models.Model):
    """Datos del turno agendado."""
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha  = models.DateTimeField("Fecha del turno")
    motivo = models.CharField("Motivo de la consulta", max_length=200)

    def __str__(self):
        return f"***Información del turno agendado***\nDueño: {self.dueño}\nMascota: {self.mascota}\nFecha: {self.fecha}\nMotivo: {self.motivo}"
    
    @property
    def es_pendiente(self):
        """Devuelve True si el turno indicado está pendiente."""
        return self.fecha > timezone.now()