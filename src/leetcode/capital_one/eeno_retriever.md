# Eeno Retriever - Interview Exercise

## Problem Overview

Capital One's **Eeno model** is a real-time decision system that must make fast decisions on customer requests (fraud detection, payment approval, etc.). To make intelligent decisions, it needs quick access to recent customer activity data.

This exercise involves building a **data retrieval system** that can fetch recent customer activity from different data stores within a configurable time window.

### Real-World Context

**Why this matters:**
- Customer initiates a $50,000 transfer → System has ~200ms to decide: approve or flag
- To decide, it needs: Recent login activity? Recent transactions? Unusual behavior patterns?
- Data sources: Clickstream (UI interactions), Transaction history (money movements)
- Decision: Is this consistent with the customer's normal behavior?

---

## The Data Model

### Time Representation
- **Minute**: Sequential number of minutes since Epoch (January 1, 1970)
- Example: `25853655` = some date/time in minutes
- Why minutes? Fast bucketing without sub-minute precision

### Data Stores

#### Clickstream Store
Tracks user interface interactions:
```
Customer 1's recent clicks:
Minute 25853654: "Confirm"
Minute 25853653: "Schedule Payment"
Minute 25853652: "View recent"
Minute 25853651: "Login"
Minute 25853650: "Enter password"
Minute 25853649: "Enter username"
```

**What it tells you**: User behavior, intent, panic (rapid clicks), normal workflow

#### Transaction Store
Tracks money movements:
```
Customer 1's recent transactions:
Minute 25853652: "Krogers $243.00"
Minute 25853651: "Ren's Ice Cream $5.00"
Minute 25853648: "Starbucks $8.00"

Customer 2's recent transactions:
Minute 25853598: "OSU Bookstore $222"
Minute 25851002: "Neil's Drums $1340"
```

**What it tells you**: Spending patterns, merchant categories, transaction amounts

---

## The Exercise

### Part 1: Understand the Original Code

```python
class RetrieverQ:
    def __init__(self, store):
        self.store = store
    
    def retrieve_recent(self, customer_id, curr_time):
        result = []
        # Retrieve data for the last 5 minutes (hardcoded!)
        for index in range(0, 5):
            val = self.store.retrieve(customer_id, curr_time - 5 + index)
            if val is not None:
                result.append(val)
        return result
```

**What it does:**
- Takes a `customer_id` and `curr_time` (in minutes since epoch)
- Retrieves data from minutes: `[curr_time-5, curr_time-4, curr_time-3, curr_time-2, curr_time-1]`
- Returns all non-null values in order
- **Problem**: Time window is hardcoded to 5 minutes

### Part 2: The Requirement

**Make the time window flexible** so it can be parameterized.

Different use cases need different windows:
- Quick login check: 10 minutes of clickstream
- Payment approval: 1 hour of transactions
- Fraud investigation: 24 hours of both
- Model training: 30 days of history

**Requirement**: Modify `retrieve_recent()` to accept a `time_window` parameter instead of hardcoding 5.

### Part 3: Edge Cases to Consider

1. **Empty results**: What if no data exists in the window?
2. **Window size variations**: time_window = 1, 10, 100, 1000
3. **Order of results**: Should they be chronological? Reverse?
4. **Sparse data**: Data might not exist for every minute in the window
5. **Large time windows**: Performance implications?

---

## Solution Strategy

### Key Decision: What Does "Last N Minutes" Mean?

**Option A: Exclude Current Minute**
```
Window = [curr_time - N, ..., curr_time - 1]
Example (N=5, curr_time=100): [95, 96, 97, 98, 99]
```

**Option B: Include Current Minute**
```
Window = [curr_time - N + 1, ..., curr_time]
Example (N=5, curr_time=100): [96, 97, 98, 99, 100]
```

**Common choice**: Include current minute (more intuitive: "last 5 minutes" = most recent 5 data points)

### Pseudocode

```python
def retrieve_recent(self, customer_id, curr_time, time_window):
    result = []
    # Determine the start of the time window
    start_minute = curr_time - time_window + 1
    
    # Retrieve data for each minute in the window
    for minute in range(start_minute, curr_time + 1):
        val = self.store.retrieve(customer_id, minute)
        if val is not None:
            result.append(val)
    
    return result
```

---

## Interview Tips

### What They're Evaluating

1. **Problem understanding** - Do you see this as a real system, not just code?
2. **API design** - Is your parameter choice sensible?
3. **Edge case thinking** - What breaks with your solution?
4. **Communication** - Can you explain your choices?

### Good Follow-up Questions to Ask

- "Should the window include the current minute or exclude it?"
- "What if `time_window` is 0 or negative?"
- "Should we validate inputs?"
- "If we scaled to millions of customers, how would we optimize this?"
- "Should results be in chronological order?"

### Possible Extensions

- **Caching**: Store frequently accessed windows?
- **Sharding**: How to distribute customer data across servers?
- **Concurrency**: Safely handle concurrent reads/writes?
- **TTL**: How long to keep data before deletion?
- **Filtering**: Return only specific event types?

