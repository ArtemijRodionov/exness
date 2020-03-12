from assignment import percents


def tax(price, percent):
    return price + price * percent


def discount(price, percent):
    return price - price * percent


class PricePolicy:

    def apply(self, price):
        """
        Change the total price of items depending on the policy.
        """


class Tax(PricePolicy):

    state_taxes = dict(percents.TAXES)

    def __init__(self, state: str):
        self.state: str = state

    def apply(self, price):
        return tax(price, self.state_taxes[self.state])


class Discount(PricePolicy):

    bound_percent = sorted(percents.DISCOUNT)

    def apply(self, price):
        if price <= 0:
            return price

        percent = 0
        for bound, p in self.bound_percent:
            if price < bound:
                break
            percent = p

        return discount(price, percent)


def calculate(price, quantity, state):
    total = price * quantity
    discounted = Discount().apply(total)
    with_tax = Tax(state).apply(discounted)
    return {'total': {'discounted': discounted, 'tax': with_tax}}
