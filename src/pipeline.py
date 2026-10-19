import json

def process_batch(records: list) -> dict:
    """Process incoming data records"""
    valid = [r for r in records if r.get('active', True)]
    return {
        'processor': 'rileycove',
        'total_received': len(records),
        'valid_count': len(valid)
    }