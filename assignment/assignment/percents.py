from decimal import Decimal

DISCOUNT = [
    (0, Decimal('0')),
    (1000, Decimal('0.03')),
    (5000, Decimal('0.05')),
    (7000, Decimal('0.07')),
    (10000, Decimal('0.1')),
    (50000, Decimal('0.15')),
]

TAXES = [
    ('AL', Decimal('0.04')),
    ('TX', Decimal('0.0625')),
    ('UT', Decimal('0.0685')),
    ('NV', Decimal('0.08')),
    ('CA', Decimal('0.0825')),
]
