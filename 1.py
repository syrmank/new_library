from dataclasses import dataclass
import random
import logging

import my_logger  # настраивает логирование (файл app.log + консоль)

logger = logging.getLogger(__name__)


# ============================================================
#  БИЗНЕС-ПРАВИЛА
#  - Цена позиции = price × quantity
#  - VIP-клиент: скидка 10%
#  - Промокод: скидка 20%
#  - Скидки складываются, но итоговая скидка ≤ 25%
# ============================================================


@dataclass
class Order:
    order_id: int
    price: float
    quantity: int
    vip: bool  # True — VIP-клиент
    promo: bool  # True — есть промокод


VIP_DISCOUNT = 0.10
PROMO_DISCOUNT = 0.20
MAX_DISCOUNT = 0.25


class Store:
    def __init__(self, orders: list[Order]):
        self.orders = orders
        # ЗАДАНИЕ 1: создать debug-лог, в котором указано,
        #            сколько заказов создаётся

    def compute_subtotal(self, order: Order) -> float:
        subtotal = order.price  # ← возможная проблема
        # ЗАДАНИЕ 2: создать debug-лог, в котором по каждому заказу
        #            выводится order_id, price, quantity и полученный subtotal
        return subtotal

    def compute_discount(self, order: Order) -> float:
        disc = 0.0
        if order.vip:
            disc = VIP_DISCOUNT
        disc = min(disc, MAX_DISCOUNT)  # ← возможная проблема
        if order.promo:
            disc += PROMO_DISCOUNT
        # ЗАДАНИЕ 3: создать debug-лог, в котором по каждому заказу
        #            выводится order_id, vip, promo и итоговая скидка в %
        # ЗАДАНИЕ 4: создать warning-лог, если итоговая скидка
        #            превышает MAX_DISCOUNT
        return disc

    def process(self) -> float:
        # ЗАДАНИЕ 5: создать info-лог о начале обработки
        #            с количеством заказов
        total = 0.0
        for order in self.orders:
            subtotal = self.compute_subtotal(order)
            disc = self.compute_discount(order)
            final = round(subtotal * (1 - disc), 2)
            # ЗАДАНИЕ 6: создать debug-лог — сводную строку по заказу
            #            (order_id, price, quantity, vip, promo,
            #             subtotal, discount, final)
            total += final
        total = round(total, 2)
        # ЗАДАНИЕ 7: создать info-лог с итоговой выручкой
        return total


def generate_orders(n: int = 40, seed: int = 42) -> list[Order]:
    rnd = random.Random(seed)
    orders = []
    for i in range(1, n + 1):
        orders.append(
            Order(
                order_id=i,
                price=round(rnd.uniform(100, 3000), 2),
                quantity=rnd.randint(1, 5),
                vip=rnd.random() < 0.3,
                promo=rnd.random() < 0.15,
            )
        )
    # гарантируем заказы с VIP+промо (для проверки скидки)
    orders[4] = Order(order_id=5, price=2000.0, quantity=3, vip=True, promo=True)
    orders[19] = Order(order_id=20, price=1500.0, quantity=2, vip=True, promo=True)
    orders[34] = Order(order_id=35, price=800.0, quantity=5, vip=True, promo=True)
    return orders


EXPECTED_REVENUE = 160483.72

if __name__ == "__main__":
    print(f"Эталон (бухгалтерия): {EXPECTED_REVENUE:.2f}")
    store = Store(generate_orders())
    total = store.process()
    print(f"ИТОГО (программа):    {total}")
    print(f"Расхождение:          {EXPECTED_REVENUE - total:+.2f}")
    print("Подробности — в app.log")
