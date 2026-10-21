"""
RECORD CHECK  -  my version
===========================
 
Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  08.10.2026

Run it:   python template.py
"""

def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(failed_logins, total_attempts):
    """Returns the difference and percentage."""
    difference = failed_logins - total_attempts
    percent = failed_logins / total_attempts * 100
    return difference, percent

def print_report(source_ip, failed_logins, total_attempts, difference, percent, status):
    """Prints the report."""
    print()
    print("=" * 34)
    print(f"  Source IP  -  {source_ip}")
    print("=" * 34)
    print(f"Failed logins: {failed_logins:19.2f}")
    print(f"Total Attempts: {total_attempts:18.2f}")
    print(f"Difference: {difference:>22.2f}")
    print(f"Percentage: {percent:>21.2f}%")
    print(f"Status: {status}")
    print("=" * 34)

count_ol = 0
while True:
    source_ip = input("Source IP ('quit' to stop): ")
    if source_ip == "quit":
        break
    failed_logins = float(input("Failed logins: "))
    total_attempts = float(input("Total attemtps: "))

    difference, percent = check(failed_logins, total_attempts)
    status = status_of(percent)

    if status == "OVER LIMIT":
        count_ol += 1

    print_report(source_ip, failed_logins, total_attempts, difference, percent, status)

print("OVER LIMIT amount:", count_ol)