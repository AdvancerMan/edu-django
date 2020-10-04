from django.db import models


class Spider(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    power = models.FloatField()
    defense = models.FloatField()
    health = models.FloatField()
    is_attacker = models.BooleanField()

    def attack(self, near_spiders):
        for spider in near_spiders:
            if spider.is_attacker != self.is_attacker:
                spider.health -= max(0, self.power - spider.defense)

    def check_alive(self):
        return self.health <= 0
