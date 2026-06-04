class DiscountCalculator:
    """Калькулятор знижок за типом клієнта та сумою замовлення піци."""

    # Константи, що усувають Magic Numbers за вимогами лінтерів
    RATES = {
        "standard": 0.05,
        "premium": 0.10,
        "vip": 0.15,
    }
    BULK_THRESHOLD = 10
    BULK_DISCOUNT_FACTOR = 0.97

    def __init__(self, customer_type: str) -> None:
        if customer_type not in self.RATES:
            raise ValueError(f"Unknown type: {customer_type}")
        self.customer_type = customer_type

    def calculate(self, amount: float) -> float:
        """Обчислює суму знижки за типом клієнта."""
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount == 0:
            return 0.0
        
        discount_rate = self.RATES[self.customer_type]
        return round(amount * discount_rate, 2)

    def apply_discount(self, amount: float) -> float:
        """Повертає суму після застосування знижки."""
        discount = self.calculate(amount)
        final_price = amount - discount
        return round(final_price, 2)

    def bulk_discount(self, amount: float, qty: int) -> float:
        """Додаткова знижка 3% при кількості піц > 10 одиниць."""
        base_price = self.apply_discount(amount)
        
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        if qty > self.BULK_THRESHOLD:
            return round(base_price * self.BULK_DISCOUNT_FACTOR, 2)
            
        return base_price
