"""
Tests for Eeno Retriever - Capital One interview exercise.

Tests cover:
1. Basic functionality - retrieving data within time windows
2. Edge cases - empty windows, sparse data, boundary conditions
3. Data ordering - chronological order of results
4. Error handling - invalid inputs
"""

import pytest

from leetcode.capital_one.eeno_retriever import InMemoryStore, RetrieverQ


class TestInMemoryStore:
    """Tests for InMemoryStore implementation."""

    def test_store_and_retrieve_single_entry(self):
        """Should store and retrieve a single data entry."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="Login")

        result = store.retrieve(customer_id=1, minute=100)
        assert result == "Login"

    def test_retrieve_nonexistent_entry_returns_none(self):
        """Should return None when data doesn't exist."""
        store = InMemoryStore()
        result = store.retrieve(customer_id=1, minute=100)
        assert result is None

    def test_store_multiple_entries_different_customers(self):
        """Should handle multiple customers independently."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="Login")
        store.add(customer_id=2, minute=100, data="Logout")

        assert store.retrieve(customer_id=1, minute=100) == "Login"
        assert store.retrieve(customer_id=2, minute=100) == "Logout"

    def test_store_multiple_entries_same_customer_different_minutes(self):
        """Should handle multiple time points for same customer."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="Enter password")
        store.add(customer_id=1, minute=101, data="Login")
        store.add(customer_id=1, minute=102, data="View account")

        assert store.retrieve(customer_id=1, minute=100) == "Enter password"
        assert store.retrieve(customer_id=1, minute=101) == "Login"
        assert store.retrieve(customer_id=1, minute=102) == "View account"

    def test_overwrite_existing_entry(self):
        """Should overwrite data at same (customer_id, minute)."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="First value")
        store.add(customer_id=1, minute=100, data="Second value")

        result = store.retrieve(customer_id=1, minute=100)
        assert result == "Second value"


class TestRetrieverQ:
    """Tests for RetrieverQ data retrieval."""

    def test_retrieve_recent_basic_window(self):
        """Should retrieve data within time window in chronological order."""
        store = InMemoryStore()
        # Add 5 consecutive minutes of data
        store.add(customer_id=1, minute=100, data="Enter password")
        store.add(customer_id=1, minute=101, data="Login")
        store.add(customer_id=1, minute=102, data="View recent")
        store.add(customer_id=1, minute=103, data="Schedule Payment")
        store.add(customer_id=1, minute=104, data="Confirm")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=104, time_window=5
        )

        expected = [
            "Enter password",
            "Login",
            "View recent",
            "Schedule Payment",
            "Confirm",
        ]
        assert result == expected

    def test_retrieve_recent_sparse_data(self):
        """Should skip missing minutes and only return non-null values."""
        store = InMemoryStore()
        # Add data only at minutes 100, 102, 104 (sparse)
        store.add(customer_id=1, minute=100, data="Event A")
        store.add(customer_id=1, minute=102, data="Event B")
        store.add(customer_id=1, minute=104, data="Event C")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=104, time_window=5
        )

        # Should return only existing data, in order
        expected = ["Event A", "Event B", "Event C"]
        assert result == expected

    def test_retrieve_recent_empty_window(self):
        """Should return empty list when no data in window."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=50, data="Old event")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=100, time_window=5
        )

        # Window is [96, 97, 98, 99, 100], doesn't include minute 50
        assert result == []

    def test_retrieve_recent_window_size_one(self):
        """Should handle window size of 1 (only current minute)."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="Current event")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=100, time_window=1
        )

        assert result == ["Current event"]

    def test_retrieve_recent_large_window(self):
        """Should handle large time windows."""
        store = InMemoryStore()
        # Add data at 5 different points within a large window
        store.add(customer_id=1, minute=1000, data="Event 1")
        store.add(customer_id=1, minute=1500, data="Event 2")
        store.add(customer_id=1, minute=2000, data="Event 3")
        store.add(customer_id=1, minute=2500, data="Event 4")
        store.add(customer_id=1, minute=2999, data="Event 5")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=2999, time_window=2000
        )

        # Window should be [1000, 1001, ..., 2999]
        expected = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"]
        assert result == expected

    def test_retrieve_recent_multiple_events_same_minute(self):
        """Should handle multiple events at the same minute (if store supports it)."""
        store = InMemoryStore()
        # Note: Basic implementation stores one value per (customer, minute)
        # This test documents the current behavior
        store.add(customer_id=1, minute=100, data="First event")
        store.add(customer_id=1, minute=100, data="Second event")  # Overwrites

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=100, time_window=1
        )

        # Only one event per minute in basic implementation
        assert result == ["Second event"]

    def test_retrieve_recent_different_customers(self):
        """Should retrieve only specified customer's data."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="Customer 1 event")
        store.add(customer_id=2, minute=100, data="Customer 2 event")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=100, time_window=1
        )

        assert result == ["Customer 1 event"]
        assert store.retrieve(customer_id=2, minute=100) == "Customer 2 event"

    def test_retrieve_recent_chronological_order(self):
        """Results should be in chronological order (oldest to newest)."""
        store = InMemoryStore()
        # Add in non-chronological order
        store.add(customer_id=1, minute=103, data="Third")
        store.add(customer_id=1, minute=101, data="First")
        store.add(customer_id=1, minute=102, data="Second")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=103, time_window=3
        )

        # Should return in chronological order
        assert result == ["First", "Second", "Third"]


class TestRetrieverQEdgeCases:
    """Edge case and error handling tests."""

    def test_retrieve_recent_zero_window_raises_error(self):
        """Should raise ValueError for time_window <= 0."""
        store = InMemoryStore()
        retriever = RetrieverQ(store)

        with pytest.raises(ValueError):
            retriever.retrieve_recent(
                customer_id=1, curr_time=100, time_window=0
            )

    def test_retrieve_recent_negative_window_raises_error(self):
        """Should raise ValueError for negative time_window."""
        store = InMemoryStore()
        retriever = RetrieverQ(store)

        with pytest.raises(ValueError):
            retriever.retrieve_recent(
                customer_id=1, curr_time=100, time_window=-5
            )

    def test_retrieve_recent_window_boundary_excludes_before_window(self):
        """Data before window start should not be included."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=95, data="Too old")
        store.add(customer_id=1, minute=96, data="In window")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=100, time_window=5
        )

        # Window is [96, 97, 98, 99, 100]
        # Minute 95 is before window, should be excluded
        assert "Too old" not in result
        assert "In window" in result

    def test_retrieve_recent_includes_current_minute(self):
        """Current minute should be included in results."""
        store = InMemoryStore()
        store.add(customer_id=1, minute=100, data="Current event")

        retriever = RetrieverQ(store)
        result = retriever.retrieve_recent(
            customer_id=1, curr_time=100, time_window=1
        )

        assert result == ["Current event"]

    def test_retrieve_recent_capital_one_example(self):
        """Recreate the Capital One interview example."""
        # Clickstream data from the exercise
        clk_store = InMemoryStore()
        clk_store.add(customer_id=1, minute=25853654, data="Confirm")
        clk_store.add(customer_id=1, minute=25853653, data="Schedule Payment")
        clk_store.add(customer_id=1, minute=25853652, data="View recent")
        clk_store.add(customer_id=1, minute=25853651, data="Login")
        clk_store.add(customer_id=1, minute=25853650, data="Enter password")
        clk_store.add(customer_id=1, minute=25853649, data="Enter username")

        # Transaction data
        trx_store = InMemoryStore()
        trx_store.add(customer_id=1, minute=25853652, data="Krogers 243.00")
        trx_store.add(customer_id=1, minute=25853651, data="Ren's Ice Cream 5.00")
        trx_store.add(customer_id=1, minute=25853648, data="Starbucks 8.00")

        # Retrieve with curr_time = 25853655, window = 5
        clk_retriever = RetrieverQ(clk_store)
        trx_retriever = RetrieverQ(trx_store)

        clk_recent = clk_retriever.retrieve_recent(
            customer_id=1, curr_time=25853655, time_window=5
        )
        trx_recent = trx_retriever.retrieve_recent(
            customer_id=1, curr_time=25853655, time_window=5
        )

        # Window is [25853651, 25853652, 25853653, 25853654, 25853655]
        # This excludes minute 25853650 (too old) and 25853649 (too old)
        # and 25853648 (way too old)
        assert "Enter password" not in clk_recent
        assert "Enter username" not in clk_recent
        assert "Starbucks 8.00" not in trx_recent

        # Should include events within window
        assert "Login" in clk_recent
        assert "View recent" in clk_recent
        assert "Krogers 243.00" in trx_recent
