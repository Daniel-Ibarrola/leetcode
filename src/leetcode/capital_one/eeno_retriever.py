"""
Eeno Retriever - Real-time customer data retrieval for fraud detection model.

This module implements a data retrieval system for Capital One's Eeno model,
which makes fast decisions (fraud detection, payment approval, etc.) based on
recent customer activity.

Key concepts:
- Time is measured in minutes since epoch (1970-01-01)
- Multiple data stores (clickstream, transactions) feed into decision model
- Time window is parameterized to support different use cases
"""

from typing import Any, List


class DataStore:
    """
    Abstract interface for a data store.

    In production, this would be backed by a real database or cache (Redis, DynamoDB, etc.)
    """

    def retrieve(self, customer_id: int, minute: int) -> Any:
        """
        Retrieve data for a customer at a specific minute.

        Args:
            customer_id: Unique customer identifier
            minute: Time in minutes since epoch

        Returns:
            Data at this minute, or None if no data exists
        """
        raise NotImplementedError


class RetrieverQ:
    """
    Retrieves recent customer activity within a configurable time window.

    Used by Eeno model to quickly fetch context for real-time decisions.
    """

    def __init__(self, store: DataStore):
        """
        Initialize the retriever with a data store.

        Args:
            store: DataStore instance (clickstream, transactions, etc.)
        """
        self._store = store

    def retrieve_recent(
        self, customer_id: int, curr_time: int, time_window: int
    ) -> List[Any]:
        """
        Retrieve customer data from the last N minutes.

        Args:
            customer_id: Which customer's data to retrieve
            curr_time: Current time in minutes since epoch
            time_window: Number of minutes to look back (must be >= 1)

        Returns:
            List of data points in chronological order for the time window.
            Empty list if no data exists in the window.

        Raises:
            ValueError: If time_window <= 0

        Example:
            >>> retriever = RetrieverQ(store)
            >>> # Retrieve last 5 minutes of activity
            >>> recent = retriever.retrieve_recent(customer_id=1, curr_time=25853655, time_window=5)
            >>> recent
            ["Enter password", "Login", "View recent", "Schedule Payment", "Confirm"]

        Timeline (for time_window=5, curr_time=25853655):
            Include minutes: [25853651, 25853652, 25853653, 25853654, 25853655]
            Exclude minutes: [... 25853650 (too old), 25853656+ (future)]
        """
        if time_window <= 0:
            raise ValueError("time_window must be > 0")

        result = []
        for minute in range(1, time_window + 1):
            data = self._store.retrieve(customer_id, curr_time - time_window + minute)
            if data is not None:
                result.append(data)
        return result

class InMemoryStore(DataStore):
    """
    Simple in-memory implementation of DataStore for testing.

    Maps (customer_id, minute) -> data_value
    """

    def __init__(self):
        """Initialize empty store."""
        self._data: dict[tuple[int, int], Any] = {}

    def add(self, customer_id: int, minute: int, data: Any) -> None:
        """
        Add data to the store.

        Args:
            customer_id: Customer ID
            minute: Time in minutes since epoch
            data: Data value to store
        """
        self._data[(customer_id, minute)] = data

    def retrieve(self, customer_id: int, minute: int) -> Any:
        """
        Retrieve data for a customer at a specific minute.

        Returns None if data doesn't exist.
        """
        return self._data.get((customer_id, minute))
