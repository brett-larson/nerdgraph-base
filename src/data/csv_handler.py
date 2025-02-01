import csv
from typing import List, Dict


def write_csv(filename: str, data: List[Dict]):
    """Write data to CSV file"""
    if not data:
        return

    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv(filename: str) -> List[Dict]:
    """Read data from CSV file"""
    with open(filename, 'r') as f:
        return list(csv.DictReader(f))