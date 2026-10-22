"""
RECORD CHECK  -  my version
===========================

Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  22.10.2026

Run it:   python template.py
"""

class Record:
    """Represent one cyber security record."""
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """Store source IP, failed logins and total attempts."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OK, WARNING or OVER LIMIT."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

def load_records(path):
    """Load Record objects from a comma-separated text file."""
    records = []
    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            record = Record(
                label,
                float(value),
                float(limit)
            )
            records.append(record)
    return records

records = load_records("lab5_records.txt")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Source IP:       {record.label}")
    print(f"Failed logins:   {record.value}")
    print(f"Total attempts:  {record.limit}")
    print(f"Status:          {record.status()}")

    if record.status() == "OVER LIMIT":
        Record.over_limit_count += 1
    
    print("=" * 34)

print()
print(f"OVER LIMIT records: {Record.over_limit_count}")