"""Tests for the property_listing module."""

import pytest

from leetcode.refactoring import property_listing


def create_property(
    id_: str,
    price: int,
    type_: property_listing.PropertyType,
    bedrooms: int,
    sqft: int,
):
    return property_listing.Property(
        id=id_, price=price, type=type_, bedrooms=bedrooms, sqft=sqft
    )


class TestProperty:
    """Tests for the Property class."""

    @pytest.mark.parametrize(
        "prop, expected_score",
        [
            (
                create_property(
                    "1a", 600000, property_listing.PropertyType.CONDO, 2, 900
                ),
                240,
            ),
            (
                create_property(
                    "1a", 600000, property_listing.PropertyType.SINGLE_FAMILY, 2, 900
                ),
                430,
            ),
            (
                create_property(
                    "1a", 600000, property_listing.PropertyType.OTHER, 2, 900
                ),
                120,
            ),
        ],
    )
    def test_property_score(
        self, prop: property_listing.Property, expected_score: float
    ):
        """Tests that the score is calculated correctly fore different property types."""
        score = prop.score
        assert score == expected_score

    def test_format_property(self):
        prop = create_property(
            "1a", 600000, property_listing.PropertyType.CONDO, 2, 900
        )
        assert prop.format() == "Property 1a [CONDO] - Score: 240.00 - Price: $600,000"


class TestProcessProperties:
    def test_process_valid_condo(self):
        """Tests if a valid CONDO is processed and formatted correctly."""
        properties = [
            create_property("1a", 600000, property_listing.PropertyType.CONDO, 2, 900)
        ]
        expected = ["Property 1a [CONDO] - Score: 240.00 - Price: $600,000"]
        assert property_listing.process_properties(properties) == expected

    def test_process_valid_single_family(self):
        """Tests if a valid SINGLE_FAMILY home is processed and formatted correctly."""
        properties = [
            create_property(
                "2b", 800000, property_listing.PropertyType.SINGLE_FAMILY, 4, 2500
            )
        ]
        expected = ["Property 2b [SINGLE_FAMILY] - Score: 1250.00 - Price: $800,000"]
        assert property_listing.process_properties(properties) == expected

    def test_process_valid_townhouse(self):
        """Tests if a valid TOWNHOUSE (other type) is processed and formatted correctly."""
        properties = [
            create_property(
                "3c", 450000, property_listing.PropertyType.TOWNHOUSE, 3, 1500
            )
        ]
        expected = ["Property 3c [TOWNHOUSE] - Score: 255.00 - Price: $450,000"]
        assert property_listing.process_properties(properties) == expected

    def test_filter_out_expensive_property(self):
        """Tests that properties with a price over 1,000,000 are filtered out."""
        properties = [
            create_property(
                "4d", 1200000, property_listing.PropertyType.SINGLE_FAMILY, 5, 3000
            )
        ]
        assert property_listing.process_properties(properties) == []

    def test_filter_out_low_score_property(self):
        """Tests that properties with a final score of 50 or less are filtered out."""
        # This property's score will be 10.0, so it should be excluded.
        properties = [
            create_property(
                "5e", 900000, property_listing.PropertyType.TOWNHOUSE, 1, 500
            )
        ]
        assert property_listing.process_properties(properties) == []

    def test_handle_empty_list(self):
        """Tests that the function returns an empty list when given an empty list."""
        assert property_listing.process_properties([]) == []

    def test_no_properties_meet_criteria(self):
        """Tests that an empty list is returned if no properties meet the criteria."""
        properties = [
            create_property(
                "4d", 1200000, property_listing.PropertyType.SINGLE_FAMILY, 5, 3000
            ),
            create_property(
                "5e", 900000, property_listing.PropertyType.TOWNHOUSE, 1, 500
            ),
        ]
        assert property_listing.process_properties(properties) == []

    def test_mixed_property_list(self):
        """Tests a list with a mix of properties that should and should not be included."""
        properties = [
            # Should be included
            create_property("1a", 600000, property_listing.PropertyType.CONDO, 2, 900),
            # Should be excluded (too expensive)
            create_property(
                "4d", 1100000, property_listing.PropertyType.SINGLE_FAMILY, 5, 3000
            ),
            # Should be included
            create_property(
                "3c", 450000, property_listing.PropertyType.TOWNHOUSE, 3, 1500
            ),
            # Should be excluded (low score)
            create_property(
                "5e", 900000, property_listing.PropertyType.TOWNHOUSE, 1, 500
            ),
        ]
        expected = [
            "Property 1a [CONDO] - Score: 240.00 - Price: $600,000",
            "Property 3c [TOWNHOUSE] - Score: 255.00 - Price: $450,000",
        ]
        assert property_listing.process_properties(properties) == expected
