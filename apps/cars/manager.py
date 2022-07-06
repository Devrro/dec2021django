from django.db.models import Manager


class CarManager(Manager):
    def car_car_by_price_filter(self, price=7000):
        return self.filter(price__gt=price)
