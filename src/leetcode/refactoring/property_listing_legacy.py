# data is a list of dictionaries, for example:
# [
#     {'id': '1a', 'price': 600000, 'type': 'CONDO', 'bedrooms': 2, 'sqft': 900},
#     {'id': '2b', 'price': 1200000, 'type': 'SINGLE_FAMILY', 'bedrooms': 4, 'sqft': 2500},
#     {'id': '3c', 'price': 450000, 'type': 'TOWNHOUSE', 'bedrooms': 3, 'sqft': 1500}
# ]

def handle_property_data(data):
    """
    This function processes property data. It takes a list of properties,
    filters them, calculates a score, and returns a formatted list of strings.
    """
    results = []
    for p in data:
        # Don't show properties over 1,000,000
        if p['price'] > 1000000:
            continue

        score = 0
        # Calculate score based on type
        if p['type'] == 'CONDO':
            # condos are popular in urban areas
            score += p['sqft'] * 0.3 + (5 - p['bedrooms']) * 10
        elif p['type'] == 'SINGLE_FAMILY':
            # single family homes are valued for space
            score += p['sqft'] * 0.5 + p['bedrooms'] * 20
        else:
            # Other types
            score += p['sqft'] * 0.2

        # Adjust score based on price, lower is better
        score -= p['price'] / 10000

        # Only include properties with a final score > 50
        if score > 50:
            # Format the final string for display
            display_str = f"Property {p['id']} [{p['type']}] - Score: {score:.2f} - Price: ${p['price']:,}"
            results.append(display_str)

    return results
