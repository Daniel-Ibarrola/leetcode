from leetcode.refactoring.property_listing_legacy import handle_property_data

def test_process_valid_condo():
    """Tests if a valid CONDO is processed and formatted correctly."""
    data = [{'id': '1a', 'price': 600000, 'type': 'CONDO', 'bedrooms': 2, 'sqft': 900}]
    expected = ["Property 1a [CONDO] - Score: 240.00 - Price: $600,000"]
    assert handle_property_data(data) == expected

def test_process_valid_single_family():
    """Tests if a valid SINGLE_FAMILY home is processed and formatted correctly."""
    data = [{'id': '2b', 'price': 800000, 'type': 'SINGLE_FAMILY', 'bedrooms': 4, 'sqft': 2500}]
    expected = ["Property 2b [SINGLE_FAMILY] - Score: 1250.00 - Price: $800,000"]
    assert handle_property_data(data) == expected

def test_process_valid_townhouse():
    """Tests if a valid TOWNHOUSE (other type) is processed and formatted correctly."""
    data = [{'id': '3c', 'price': 450000, 'type': 'TOWNHOUSE', 'bedrooms': 3, 'sqft': 1500}]
    expected = ["Property 3c [TOWNHOUSE] - Score: 255.00 - Price: $450,000"]
    assert handle_property_data(data) == expected

def test_filter_out_expensive_property():
    """Tests that properties with a price over 1,000,000 are filtered out."""
    data = [{'id': '4d', 'price': 1200000, 'type': 'SINGLE_FAMILY', 'bedrooms': 5, 'sqft': 3000}]
    assert handle_property_data(data) == []

def test_filter_out_low_score_property():
    """Tests that properties with a final score of 50 or less are filtered out."""
    # This property's score will be 10.0, so it should be excluded.
    data = [{'id': '5e', 'price': 900000, 'type': 'TOWNHOUSE', 'bedrooms': 1, 'sqft': 500}]
    assert handle_property_data(data) == []

def test_handle_empty_list():
    """Tests that the function returns an empty list when given an empty list."""
    assert handle_property_data([]) == []

def test_no_properties_meet_criteria():
    """Tests that an empty list is returned if no properties meet the criteria."""
    data = [
        {'id': '4d', 'price': 1200000, 'type': 'SINGLE_FAMILY', 'bedrooms': 5, 'sqft': 3000},
        {'id': '5e', 'price': 900000, 'type': 'TOWNHOUSE', 'bedrooms': 1, 'sqft': 500}
    ]
    assert handle_property_data(data) == []

def test_mixed_property_list():
    """Tests a list with a mix of properties that should and should not be included."""
    data = [
        # Should be included
        {'id': '1a', 'price': 600000, 'type': 'CONDO', 'bedrooms': 2, 'sqft': 900},
        # Should be excluded (too expensive)
        {'id': '4d', 'price': 1100000, 'type': 'SINGLE_FAMILY', 'bedrooms': 5, 'sqft': 3000},
        # Should be included
        {'id': '3c', 'price': 450000, 'type': 'TOWNHOUSE', 'bedrooms': 3, 'sqft': 1500},
        # Should be excluded (low score)
        {'id': '5e', 'price': 900000, 'type': 'TOWNHOUSE', 'bedrooms': 1, 'sqft': 500},
    ]
    expected = [
        "Property 1a [CONDO] - Score: 240.00 - Price: $600,000",
        "Property 3c [TOWNHOUSE] - Score: 255.00 - Price: $450,000"
    ]
    assert handle_property_data(data) == expected
