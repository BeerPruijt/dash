def get_valid_indices(column_data):
    """Returns a list of valid indices as dropdown options."""
    return [{'label': str(i), 'value': i} for i in column_data.index]

def get_disabled_indices(column_data, comparator, condition):
    """Returns a list of indices with a 'disabled' key based on the condition."""
    return [{'label': str(i), 'value': i, 'disabled': condition(i, comparator)} for i in column_data.index]
