from car_rental_system import user, customer, employee


class Rental:
    def __init__(self, date, price, pending_payment, attendant):
        self.date = date
        self.price = price
        self.pending_payment = pending_payment
        self.attendant = attendant

