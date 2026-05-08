# Dynamic Programming

```cpp
int Knapsack::maxProfit() const
{
    // Returns the optimal profit for the knapsack

    // Create a table of zeros with shape (num items, knapsack weight + 1)
    int numItems {static_cast<int>(m_weights.size())};
    std::vector<int> row (m_weight, 0);
    std::vector<std::vector<int>> table (numItems, row);

    // Fill the table
    for (auto item {1}; item < numItems + 1; ++item)
    {
        for (auto wt {1}; wt < m_weight + 1; ++wt)
        {
            // If the item weight is greater than the current weight skip it
            if (m_weights[item - 1] > wt)
                table[item][wt] = table[item - 1][wt];
            // Take the max of including vs excluding the item
            else
                table[item][wt] = std::max(table[item - 1][wt],
                                            m_profits[item - 1] + table[item - 1][wt - m_weights[item - 1]]);
        }
    }

    return table[numItems][m_weight];
}
```
