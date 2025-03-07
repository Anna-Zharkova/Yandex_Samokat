# Анна Жаркова, 27-я когорта — Финальный проект. Инженер по тестированию плюс

# 1. Выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true)

SELECT c.login, COUNT(o.id) AS "order_amount"
       FROM "Couriers" AS c
       LEFT JOIN "Orders" AS o ON c.id = o."courierId"
       WHERE o."inDelivery" = true
       GROUP BY c.login;

# 2. Выведи все трекеры заказов и их статусы

SELECT track,
          CASE
            WHEN finished = true THEN 2
            WHEN cancelled = true THEN -1
            WHEN "inDelivery" = true THEN 1
            ELSE 0 
        END AS status
FROM "Orders";