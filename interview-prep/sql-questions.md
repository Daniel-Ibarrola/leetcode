# SQL Interview Questions

---

### 1. What is the difference between `WHERE` and `HAVING`?

Both filter rows, but they operate at different stages of the query.

- **`WHERE`** filters rows **before** aggregation. It cannot reference aggregate functions.
- **`HAVING`** filters groups **after** `GROUP BY` and aggregation. It can reference aggregate functions.

```sql
-- Find departments with more than 5 employees earning over 50k
SELECT department, COUNT(*) AS headcount
FROM employees
WHERE salary > 50000          -- filter rows first
GROUP BY department
HAVING COUNT(*) > 5;          -- then filter groups
```

Using `HAVING` without `GROUP BY` applies the filter to the entire result set as one group.

---

### 2. Explain the different types of JOINs.

| JOIN type | Returns |
|---|---|
| `INNER JOIN` | Only rows with a match in **both** tables |
| `LEFT JOIN` | All rows from the left table; NULLs for unmatched right rows |
| `RIGHT JOIN` | All rows from the right table; NULLs for unmatched left rows |
| `FULL OUTER JOIN` | All rows from both tables; NULLs wherever no match |
| `CROSS JOIN` | Cartesian product — every left row paired with every right row |
| `SELF JOIN` | A table joined to itself (use aliases) |

```sql
-- LEFT JOIN: all employees, even those with no department
SELECT e.name, d.name AS department
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- SELF JOIN: find each employee's manager
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**Interview tip:** "Give me all X with no Y" is a LEFT JOIN + `WHERE right_table.id IS NULL` pattern.

```sql
-- Employees with no assigned department
SELECT e.name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id
WHERE d.id IS NULL;
```

---

### 3. What are window functions and how do they differ from `GROUP BY`?

`GROUP BY` collapses rows into one row per group. **Window functions** compute across a set of rows related to the current row **without collapsing** them — each row keeps its identity.

```sql
-- Rank employees by salary within each department
SELECT
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;
```

Common window functions:

| Function | Description |
|---|---|
| `ROW_NUMBER()` | Unique sequential number per partition; no ties |
| `RANK()` | Rank with gaps on ties (1, 1, 3) |
| `DENSE_RANK()` | Rank without gaps on ties (1, 1, 2) |
| `LAG(col, n)` | Value from n rows before the current row |
| `LEAD(col, n)` | Value from n rows after the current row |
| `SUM() OVER (...)` | Running total |
| `NTILE(n)` | Divides rows into n equal buckets |

```sql
-- Running total of sales by date
SELECT
    sale_date,
    amount,
    SUM(amount) OVER (ORDER BY sale_date) AS running_total
FROM sales;

-- Month-over-month change
SELECT
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_revenue,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS change
FROM monthly_revenue;
```

---

### 4. What is the difference between a subquery and a CTE?

Both encapsulate a query, but they differ in readability and reusability.

**Subquery** — inline, anonymous, can be used in `SELECT`, `FROM`, or `WHERE`:

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**CTE (Common Table Expression)** — named, defined with `WITH`, can be referenced multiple times:

```sql
WITH avg_salary AS (
    SELECT AVG(salary) AS avg FROM employees
)
SELECT e.name, e.salary
FROM employees e
JOIN avg_salary a ON e.salary > a.avg;
```

**Recursive CTE** — used for hierarchical data (org charts, trees):

```sql
WITH RECURSIVE org AS (
    -- base case: top-level employees (no manager)
    SELECT id, name, manager_id, 0 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- recursive case: employees whose manager is already in the CTE
    SELECT e.id, e.name, e.manager_id, org.level + 1
    FROM employees e
    JOIN org ON e.manager_id = org.id
)
SELECT * FROM org ORDER BY level;
```

Prefer CTEs for readability. Prefer subqueries in `WHERE` for simple existence checks.

---

### 5. What is the difference between `UNION` and `UNION ALL`?

- **`UNION`** combines result sets and **removes duplicate rows** (sorts and deduplicates — slower).
- **`UNION ALL`** combines result sets and **keeps all rows including duplicates** (faster).

```sql
-- UNION: unique customer IDs from two tables
SELECT customer_id FROM orders_2024
UNION
SELECT customer_id FROM orders_2025;

-- UNION ALL: all rows including dupes (e.g., for aggregation later)
SELECT customer_id FROM orders_2024
UNION ALL
SELECT customer_id FROM orders_2025;
```

Use `UNION ALL` by default unless you explicitly need deduplication — it avoids the sort cost.

---

### 6. What is the difference between `EXISTS` and `IN`?

Both check set membership but behave differently on NULLs and large data sets.

```sql
-- IN: executes the subquery once, then checks membership
SELECT name FROM customers
WHERE id IN (SELECT customer_id FROM orders);

-- EXISTS: short-circuits — stops as soon as one match is found
SELECT name FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.id
);
```

- `IN` with a subquery that can return NULLs produces unexpected results — `x IN (1, NULL)` is NULL (not TRUE/FALSE) for non-matching x, so rows are silently excluded.
- `EXISTS` is often faster for large subqueries because it short-circuits.
- `IN` is clearer for small, static value lists: `WHERE status IN ('active', 'pending')`.

**Rule of thumb:** Use `EXISTS` for correlated subqueries, `IN` for small literal lists.

---

### 7. How do indexes work and when should you add one?

An index is a separate data structure (typically a B-tree) that the database maintains alongside a table to speed up lookups. It trades write overhead and storage for read speed.

**When to add an index:**
- Columns frequently used in `WHERE`, `JOIN ON`, or `ORDER BY`
- Foreign key columns
- Columns used in range queries (`BETWEEN`, `>`, `<`)

**When NOT to index:**
- Small tables (a full scan is faster than index overhead)
- Columns with very low cardinality (e.g., a boolean) — the optimizer may ignore the index
- Tables with very high write volume relative to reads

**Index types:**

| Type | Use case |
|---|---|
| B-tree (default) | Equality, range, ORDER BY |
| Hash | Equality only |
| Composite | Multi-column lookups — column order matters |
| Partial | Only indexes rows matching a condition |
| Covering | Includes all columns a query needs; avoids table lookup |

```sql
-- Composite index: useful for WHERE status = 'active' AND created_at > ...
CREATE INDEX idx_orders_status_date ON orders(status, created_at);

-- Partial index: index only active orders
CREATE INDEX idx_active_orders ON orders(customer_id)
WHERE status = 'active';
```

A **composite index on (A, B)** satisfies queries on A alone or (A, B) together, but **not B alone** — the leftmost prefix rule.

---

### 8. What are transactions and what are ACID properties?

A **transaction** is a sequence of SQL statements that execute as a single unit. All statements either commit together or roll back together.

**ACID:**

| Property | Meaning |
|---|---|
| **Atomicity** | All operations succeed or all are rolled back — no partial writes |
| **Consistency** | The database moves from one valid state to another; constraints are enforced |
| **Isolation** | Concurrent transactions don't interfere with each other |
| **Durability** | Committed data survives crashes (written to disk/WAL) |

```sql
BEGIN;
    UPDATE accounts SET balance = balance - 500 WHERE id = 1;
    UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;
-- If either UPDATE fails, ROLLBACK is implicit (or explicit with ROLLBACK;)
```

**Isolation levels** (weakest → strongest):

| Level | Dirty Read | Non-repeatable Read | Phantom Read |
|---|---|---|---|
| Read Uncommitted | Yes | Yes | Yes |
| Read Committed | No | Yes | Yes |
| Repeatable Read | No | No | Yes |
| Serializable | No | No | No |

Most databases default to **Read Committed**. PostgreSQL's default is Read Committed; MySQL InnoDB defaults to Repeatable Read.

---

### 9. What is normalization? Explain 1NF, 2NF, 3NF.

Normalization organizes tables to reduce data redundancy and improve integrity.

**1NF — First Normal Form:**
- Every column contains atomic (indivisible) values.
- No repeating groups or arrays in columns.

```sql
-- Violates 1NF: multiple values in one column
-- | id | name  | phones          |
-- | 1  | Alice | 555-1234, 555-9999 |

-- 1NF: separate table
CREATE TABLE phone_numbers (
    customer_id INT,
    phone VARCHAR(20)
);
```

**2NF — Second Normal Form:**
- Must be in 1NF.
- Every non-key column depends on the **whole** primary key (no partial dependencies).
- Relevant only when there is a composite primary key.

```sql
-- Violates 2NF: order_items(order_id, product_id, product_name)
-- product_name depends only on product_id, not on (order_id, product_id)

-- 2NF: move product_name to a products table
```

**3NF — Third Normal Form:**
- Must be in 2NF.
- No transitive dependencies — non-key columns must depend only on the primary key, not on other non-key columns.

```sql
-- Violates 3NF: employees(id, department_id, department_name)
-- department_name depends on department_id, not on employee id

-- 3NF: separate departments table
CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE employees (id INT PRIMARY KEY, department_id INT REFERENCES departments(id));
```

**Denormalization** is intentional — accept redundancy for query performance (e.g., storing `department_name` in the `employees` table to avoid a JOIN in every report query).

---

### 10. How do you handle NULLs in SQL?

NULL is not a value — it means "unknown." This causes counterintuitive behavior.

```sql
-- NULL comparisons always evaluate to NULL (not TRUE or FALSE)
SELECT 1 = NULL;    -- NULL
SELECT NULL = NULL; -- NULL (not TRUE!)

-- Correct NULL checks
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;

-- COALESCE: return the first non-NULL argument
SELECT COALESCE(phone, email, 'no contact') AS contact FROM users;

-- NULLIF: return NULL if two values are equal (avoids division by zero)
SELECT revenue / NULLIF(units_sold, 0) AS price_per_unit FROM sales;

-- NULL in aggregates: aggregate functions ignore NULLs
SELECT AVG(salary) FROM employees; -- NULLs excluded from average

-- NULL in ORDER BY: NULLs sort first or last depending on the DB
-- PostgreSQL: NULLS LAST / NULLS FIRST
SELECT * FROM employees ORDER BY salary DESC NULLS LAST;
```

**Interview tip:** When a `LEFT JOIN` produces unexpected missing rows, check for NULLs propagating through `WHERE` clauses.

---

### 11. Common coding problems

#### Nth highest salary

```sql
-- Second highest salary (generalizes to Nth with OFFSET N-1)
SELECT salary
FROM (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS sub;

-- With DENSE_RANK (handles ties correctly)
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk = 2;
```

#### Find duplicate rows

```sql
-- Find emails that appear more than once
SELECT email, COUNT(*) AS cnt
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Return the full duplicate rows
SELECT *
FROM users
WHERE email IN (
    SELECT email FROM users GROUP BY email HAVING COUNT(*) > 1
);
```

#### Delete duplicate rows, keep one

```sql
-- Keep the row with the lowest id for each email
DELETE FROM users
WHERE id NOT IN (
    SELECT MIN(id) FROM users GROUP BY email
);

-- PostgreSQL: using ctid for efficiency
DELETE FROM users
WHERE ctid NOT IN (
    SELECT MIN(ctid) FROM users GROUP BY email
);
```

#### Employees who earn more than their manager

```sql
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

#### Running total

```sql
SELECT
    sale_date,
    amount,
    SUM(amount) OVER (ORDER BY sale_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM sales;
```

#### Find users active in consecutive days

```sql
WITH daily AS (
    SELECT DISTINCT user_id, DATE(created_at) AS day FROM events
),
with_lag AS (
    SELECT
        user_id,
        day,
        LAG(day) OVER (PARTITION BY user_id ORDER BY day) AS prev_day
    FROM daily
)
SELECT DISTINCT user_id
FROM with_lag
WHERE day - prev_day = 1;  -- consecutive days
```

---

### 12. How do you diagnose a slow query?

Use `EXPLAIN` / `EXPLAIN ANALYZE` to see the query plan.

```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 42;
```

**Key things to look for:**

| Indicator | Meaning |
|---|---|
| `Seq Scan` | Full table scan — no index used |
| `Index Scan` | Index used, then fetches row from heap |
| `Index Only Scan` | Covering index — no heap access |
| `Hash Join` / `Nested Loop` | Join strategy — Nested Loop is slow on large tables without indexes |
| High `rows` estimate vs actual | Stale statistics — run `ANALYZE` |
| High `cost` | Relative query cost estimate |

**Common fixes:**
- Add an index on the filtered/joined column
- Rewrite a correlated subquery as a JOIN or CTE
- Use `LIMIT` to avoid full scans when only a few rows are needed
- Run `ANALYZE` to refresh statistics if estimates are far off
- Avoid `SELECT *` — fetch only needed columns (enables covering indexes)
- Avoid functions on indexed columns in `WHERE` — `WHERE YEAR(created_at) = 2024` prevents index use; use `WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'` instead

---

### 13. Query optimization techniques (15 rules)

A checklist of actionable techniques, roughly ordered from highest to lowest impact.

#### 1. Index the right columns
Create indexes on columns used in `WHERE`, `JOIN ON`, and `ORDER BY`. Prefer composite indexes for multi-column filters and remember the leftmost prefix rule. Avoid over-indexing — every index slows down `INSERT`, `UPDATE`, and `DELETE`.

```sql
CREATE INDEX idx_customer_id ON orders (customer_id);
```

#### 2. Never use `SELECT *`
Fetch only the columns you need. This reduces I/O, enables covering index scans, and prevents surprising behavior when schema changes.

```sql
-- Bad
SELECT * FROM products;
-- Good
SELECT product_id, product_name, price FROM products;
```

#### 3. Use `LIMIT` to cap row counts during development
While testing or validating a transformation, add `LIMIT` to avoid scanning the full table. Remove it (or make it configurable) for production pipelines that need complete data.

```sql
SELECT name FROM customers ORDER BY customer_group DESC LIMIT 100;
```

#### 4. Join efficiently
- Index the join columns on both sides.
- Start with the table that produces the fewest rows.
- Use CTEs to pre-filter before joining, rather than joining first and filtering after.

```sql
WITH recent_orders AS (
    SELECT customer_id, order_id
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT c.customer_name, ro.order_id
FROM customers c
INNER JOIN recent_orders ro ON c.customer_id = ro.customer_id;
```

#### 5. Read query execution plans
`EXPLAIN` (or `EXPLAIN ANALYZE` to see actual row counts) reveals what the optimizer chose. Watch for:
- `Seq Scan` on large tables — missing index.
- Nested Loop join on large tables — missing index on the inner table.
- High estimated vs. actual row counts — stale statistics, run `ANALYZE`.

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 42;
```

#### 6. Keep `WHERE` clauses sargable
A condition is **sargable** (Search ARGument ABLE) when the optimizer can use an index for it. Functions applied to indexed columns break sargability.

```sql
-- Non-sargable: wrapping the column in a function prevents index use
SELECT * FROM employees WHERE YEAR(hire_date) = 2020;

-- Sargable: range condition lets the index work
SELECT * FROM employees
WHERE hire_date >= '2020-01-01' AND hire_date < '2021-01-01';
```

#### 7. Replace correlated subqueries with JOINs or CTEs
A correlated subquery re-executes for every row of the outer query. Rewriting as a JOIN or a CTE typically turns it into a single pass.

```sql
-- Correlated subquery: runs once per salesperson row
SELECT salesperson_id
FROM sales s
WHERE sales_amount > (SELECT AVG(sales_amount) FROM sales WHERE salesperson_id = s.salesperson_id);

-- CTE: aggregation computed once
WITH avg_by_rep AS (
    SELECT salesperson_id, AVG(sales_amount) AS avg_sales
    FROM sales GROUP BY salesperson_id
)
SELECT s.salesperson_id
FROM sales s
JOIN avg_by_rep a ON s.salesperson_id = a.salesperson_id
WHERE s.sales_amount > a.avg_sales;
```

#### 8. Use `EXISTS` instead of `IN` for existence checks
`EXISTS` short-circuits on the first match; `IN` with a subquery reads the full result set. `IN` also has surprising NULL behavior (see Q6).

```sql
SELECT * FROM orders o
WHERE EXISTS (
    SELECT 1 FROM customers c
    WHERE c.customer_id = o.customer_id AND c.country = 'USA'
);
```

#### 9. Avoid `DISTINCT` on large result sets
`DISTINCT` forces a sort/deduplication pass. Alternatives:
- Fix upstream data quality so duplicates don't exist.
- Use `GROUP BY` — communicates intent more clearly.
- Use `ROW_NUMBER()` when you need one row per group with control over which one to keep.

```sql
-- Prefer GROUP BY over DISTINCT for simple deduplication
SELECT city FROM customers GROUP BY city;
```

#### 10. Use `UNION ALL` instead of `UNION`
`UNION` deduplicates — it sorts the full combined result set. `UNION ALL` skips that step. Use `UNION` only when you actually need to remove duplicates.

```sql
SELECT product_id FROM products WHERE category = 'Electronics'
UNION ALL
SELECT product_id FROM products WHERE category = 'Books';
```

#### 11. Keep statistics up to date
The query planner estimates costs using table statistics. Stale statistics lead to bad plan choices (e.g., choosing a Seq Scan when an index exists).

```sql
ANALYZE;           -- update statistics for all tables (PostgreSQL)
ANALYZE my_table;  -- update for one table
```

Most databases auto-analyze, but after large bulk loads it's worth running manually.

#### 12. Use stored procedures for repeated logic
Stored procedures are precompiled and cached. They reduce network round-trips (the SQL is already on the server) and avoid re-parsing the same statement on every call.

```sql
CREATE OR REPLACE PROCEDURE insert_employee(
    emp_id INT, emp_first_name VARCHAR, emp_last_name VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO employees (employee_id, first_name, last_name)
    VALUES (emp_id, emp_first_name, emp_last_name);
END;
$$;
```

#### 13. Minimize unnecessary `ORDER BY` and `GROUP BY`
Sorting is O(n log n). Only sort when the output order actually matters — avoid it inside subqueries and CTEs that will be filtered further. Index `ORDER BY` columns when sorting is unavoidable.

#### 14. Use database-specific features for scale
- **Partitioning** — split a large table into smaller physical segments by a partition key (e.g., date range). Queries that filter on the partition key scan only the relevant partition.
- **Sharding** — distribute rows across multiple servers using a sharding key. Needed when a single node cannot hold or serve the data.
- **Query hints** — database-specific instructions that override the optimizer's choice (use sparingly, as they can mask root causes).

```sql
-- MySQL: force a specific index
SELECT * FROM employees USE INDEX (idx_salary) WHERE salary > 50000;
```

#### 15. Break down complex queries with materialized views
A **materialized view** stores the precomputed result of a query on disk. Subsequent queries read the snapshot instead of recomputing. Refresh manually or on a schedule when the underlying data changes.

```sql
CREATE MATERIALIZED VIEW daily_sales AS
SELECT product_id, SUM(quantity) AS total_quantity
FROM order_items
GROUP BY product_id;

-- Query the snapshot (fast)
SELECT * FROM daily_sales WHERE total_quantity > 100;

-- Refresh when data changes
REFRESH MATERIALIZED VIEW daily_sales;
```

Materialized views trade freshness for speed — ideal for dashboards and reports that tolerate slightly stale data.
