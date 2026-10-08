"""
RECORD CHECK  -  my version
===========================
 
Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  08.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(value, limit):
    """Returns the difference and percentage."""
    difference = value - limit
    percent = value / limit * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Prints the report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value: {value:>27.2f}")
    print(f"Limit: {limit:>27.2f}")
    print(f"Difference: {difference:>22.2f}")
    print(f"Percentage: {percent:>21.2f}%")
    print(f"Status: {status}")
    print("=" * 34)

count_ol = 0
while True:
    label = input("Enter label ('quit' to stop): ")
    if label == "quit":
        break
    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        count_ol += 1

    print_report(label, value, limit, difference, percent, status)

print("OVER LIMIT amount:", count_ol)