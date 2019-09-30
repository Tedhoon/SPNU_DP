from django.db import models

class MenuList(models.Model):
    title = models.CharField(max_length=10)
    dorm_menu = models.ImageField(upload_to='menu/')
    hall_menu = models.ImageField(upload_to='menu/')    
    hits =  models.PositiveIntegerField(default = 0) #사용자 계산용(실제 렌더링 수)

    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits += 1
        self.save()
