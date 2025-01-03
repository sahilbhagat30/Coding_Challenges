# Node Classification in Binary Search Tree

## Problem Statement
You are given a table `BST` that represents a Binary Search Tree (BST). The table has the following structure:

| Column Name | Type    | Description                                                |
|-------------|---------|------------------------------------------------------------|
| `N`         | INTEGER | The value of the node in the BST.                          |
| `P`         | INTEGER | The value of the parent node. `NULL` if the node is the root.|

Write a query to classify each node in the BST as one of the following:
1. **Root**: If the node has no parent (`P IS NULL`).
2. **Inner**: If the node is a parent of at least one other node.
3. **Leaf**: If the node has a parent but is not a parent to any other node.

The output should include the node value `N` and its classification (`NodeType`) in ascending order of `N`.

---

## Input Table Example

### `BST` Table

| N | P    |
|---|------|
| 1 | 2    |
| 2 | 5    |
| 3 | 2    |
| 5 | NULL |
| 6 | 8    |
| 8 | 5    |
| 9 | 8    |

---

## Expected Output

| N | NodeType |
|---|----------|
| 1 | Leaf     |
| 2 | Inner    |
| 3 | Leaf     |
| 5 | Root     |
| 6 | Leaf     |
| 8 | Inner    |
| 9 | Leaf     |

---

```sql
SELECT
    N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (SELECT P FROM BST) THEN 'Inner'
        ELSE 'Leaf'
    END AS NodeType
FROM
    BST
ORDER BY
    N;
```

## Explanation

1. **Node 5**: As `P` is `NULL`, this node is classified as `Root`.
2. **Nodes 2 and 8**: These nodes appear as parents for other nodes (`1, 3` and `6, 9` respectively), so they are classified as `Inner`.
3. **Nodes 1, 3, 6, 9**: These nodes have parents but are not parents themselves, so they are classified as `Leaf`.

---

## Additional Notes

- The query uses a subquery to determine whether a node appears as a parent in the `BST` table.
- Ordering the results by `N` ensures the output is presented in ascending order of the node values.

---
