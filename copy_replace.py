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
