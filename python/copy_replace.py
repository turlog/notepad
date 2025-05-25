from collections import namedtuple
from dataclasses import dataclass
from datetime import date
from copy import replace

# a bunch of immutable stuff

Amount = namedtuple("Amount", ["value", "currency"])


@dataclass(frozen=True)
class Order:
    date: date
    total: Amount


print(order := Order(total=Amount(100, "USD"), date=date.today()))

# let's create new one based on the old one

print(
    order := replace(
        order,
        total=replace(order.total, value=200),
        date=replace(order.date, year=2024),
    )
)


class Invoice:
    def __init__(self, order):
        self.total = order.total

    def __replace__(self, order=None, total=None):
        if order is not None:
            return Invoice(order)
        if total is not None:
            invoice = Invoice.__new__(Invoice)
            invoice.total = total
            return invoice

    def __repr__(self):
        return f"Invoice(id={id(self)}, total={self.total})"


print(invoice := Invoice(order))
invoice.total = Amount(100, "PLN")
print(invoice)
print(replace(invoice, order=order))
