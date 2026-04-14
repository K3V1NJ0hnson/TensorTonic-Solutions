SELECT product, revenue, sale_date
FROM sales
ORDER BY revenue DESC, sale_date asc
LIMIT 3 OFFSET 1;