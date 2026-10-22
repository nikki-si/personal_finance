-- Список всех транзакций с категориями (JOIN)
SELECT t.id, t.amount, c.name AS category, t.description
FROM transactions t
JOIN categories c ON t.category_id = c.id
ORDER BY t.id;

-- Транзакции по категории "Продукты" (WHERE)
SELECT t.id, t.amount, t.description
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE c.name = 'Продукты'
ORDER BY t.amount DESC;

-- Транзакции с суммой больше 1000 (WHERE)
SELECT id, amount, description
FROM transactions
WHERE amount > 1000
ORDER BY amount DESC;

-- Транзакция по id (JOIN)
SELECT t.id, t.amount, c.name AS category, t.description
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.id = 1;

-- Количество транзакций (COUNT)
SELECT COUNT(*) AS total_count FROM transactions;

-- Общая сумма (SUM)
SELECT SUM(amount) AS total_amount FROM transactions;

-- Средняя сумма (AVG)
SELECT AVG(amount) AS avg_amount FROM transactions;

-- Количество по категориям (GROUP BY)
SELECT c.name AS category, COUNT(t.id) AS count
FROM categories c
LEFT JOIN transactions t ON t.category_id = c.id
GROUP BY c.id, c.name
ORDER BY count DESC;

-- Сумма по категориям (GROUP BY)
SELECT c.name AS category, SUM(t.amount) AS total
FROM categories c
LEFT JOIN transactions t ON t.category_id = c.id
GROUP BY c.id, c.name
ORDER BY total DESC;

-- Категории с суммой > 500 (HAVING)
SELECT c.name AS category, SUM(t.amount) AS total
FROM categories c
JOIN transactions t ON t.category_id = c.id
GROUP BY c.id, c.name
HAVING SUM(t.amount) > 500
ORDER BY total DESC;

-- Самая дорогая транзакция (MAX)
SELECT id, amount, description
FROM transactions
ORDER BY amount DESC
LIMIT 1;

-- Все, кроме "Транспорт" (WHERE + NOT)
SELECT t.id, t.amount, c.name AS category
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE c.name != 'Транспорт';