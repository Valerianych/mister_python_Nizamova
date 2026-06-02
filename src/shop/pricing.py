def final_price_cents(base_cents: int, discount_percent: int = 0, tax_percent: int = 20) -> int:
    for value in (base_cents, discount_percent, tax_percent):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("all values must be int")

    if base_cents < 0:
        raise ValueError("base_cents must be greater than or equal to zero")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be from 0 to 100")
    if tax_percent < 0 or tax_percent > 100:
        raise ValueError("tax_percent must be from 0 to 100")

    price_after_discount = base_cents * (100 - discount_percent) / 100
    final_price = price_after_discount * (100 + tax_percent) / 100
    return int(round(final_price))
