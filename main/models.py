from django.db import models



class Banner(models.Model):
    title = models.CharField(max_length=200)  # Oynaning sarlavhasi
    description = models.TextField()  # Tavsif
    image = models.ImageField(upload_to='banners/')  # Rasmlar uchun joy
    is_active = models.BooleanField(default=True)  # Oynani ko‘rsatish kerakmi?
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)  # Yangilangan vaqt

    def __str__(self):
        return self.title

class Dimm(models.Model):
    title = models.CharField(max_length=200)  # Dimming sarlavhasi
    description = models.TextField()
    image = models.ImageField(upload_to='dimms/')  # Rasmlar uchun joy


    def __str__(self):
        return self.title



class CourseType(models.Model):
    name = models.CharField(max_length=100)  # Kurs turi nomi (masalan: Dasturlash, Dizayn)
    description = models.TextField(blank=True, null=True)  # Tavsif (ixtiyoriy)

    def __str__(self):
        return self.name


# Kurs modeli
class Course(models.Model):
    title = models.CharField(max_length=200)  # Kursning nomi
    description = models.TextField()  # Kurs haqida qisqacha ma'lumot
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE) # Kurs turi bilan bog'lanish
    start_date = models.DateField()  # Kurs boshlanish sanasi
    end_date = models.DateField()  # Kurs tugash sanasi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Kurs narxi

    def __str__(self):
        return self.title
    
class Module(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=200)
    duration = models.DurationField()  # Vaxtni ko'rsatish uchun
    video_link = models.URLField()
    homework_type = models.CharField(max_length=50, choices=[('description', 'Description'), ('link', 'Link'), ('list', 'List')])
    homework_content = models.TextField()

    def __str__(self):
        return self.name
    
    

class News(models.Model):
    title = models.CharField(max_length=255)  # Yangilik sarlavhasi
    description = models.TextField(blank=True, null=True)  # Yangilik matni
    created_at = models.DateTimeField(auto_now_add=True)  # Qo‘shilgan sana
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Rasm yuklash
    link = models.URLField(blank=True, null=True)  # Har qanday URL (masalan, YouTube, maqola havolasi)

    def __str__(self):
        return self.title



class Subject(models.Model):
    name = models.CharField(max_length=255)  # Fanning nomi
    description = models.TextField(blank=True, null=True)  # Fanni tavsifi (ixtiyoriy)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)  # O'qituvchi ismi
    last_name = models.CharField(max_length=100)  # O'qituvchi familiyasi
    subject = models.ForeignKey(Subject, related_name='teachers', on_delete=models.SET_NULL, null=True, blank=True)  # O'qituvchining fani (bog'lash)
    bio = models.TextField(blank=True, null=True)  # O'qituvchi haqida ma'lumot
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)  # O'qituvchi rasmi

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.subject.name if self.subject else 'No Subject'})"
    

class Message(models.Model):
    first_name = models.CharField(max_length=100)  # Foydalanuvchi ismi
    last_name = models.CharField(max_length=100, blank=True, null=True)  # Foydalanuvchi familiyasi (ixtiyoriy)
    email = models.EmailField()  # Foydalanuvchi emaili
    phone = models.CharField(max_length=15)  # Foydalanuvchi telefon raqami
    message = models.TextField(blank=True, null=True)  # Foydalanuvchi fikri (ixtiyoriy)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"



class Contact(models.Model):
    first_name = models.CharField(max_length=100)  # Foydalanuvchi ismi
    last_name = models.CharField(max_length=100, blank=True, null=True)  # Foydalanuvchi familiyasi (ixtiyoriy)
    email = models.EmailField()  # Foydalanuvchi emaili
    phone = models.CharField(max_length=15)  # Foydalanuvchi telefon raqami
    message = models.TextField(blank=True, null=True)  # Foydalanuvchi fikri (ixtiyoriy)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
