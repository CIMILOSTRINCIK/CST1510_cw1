"""
RECORD CHECK  -  my version
===========================

Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  15.10.2026

Run it:   python template.py
"""

def check_record(failed_logins, total_attempts):
    """Returns the difference, percentage and status."""
    difference = failed_logins - total_attempts
    percent = failed_logins / total_attempts * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(source_ip, failed_logins=None, total_attempts=None, difference=None, percent=None, status=None):
    """Prints the report."""
    if failed_logins is None:
        print(source_ip)
        return
    else:
        print()
        print("=" * 34)
        print(f"  Source IP  -  {source_ip}")
        print("=" * 34)
        print(f"Failed logins: {failed_logins:>19.2f}")
        print(f"Total attempts: {total_attempts:>18.2f}")
        print(f"Difference: {difference:>22.2f}")
        print(f"Percentage: {percent:>21.2f}%")
        print(f"Status: {status}")
        print("=" * 34)

def load_records(path):
    """Loads records from a file into a list of dictionaries."""
    records = []

    with open(path, "r") as file:
        for line in file:
            source_ip, failed_logins, total_attempts = line.strip().split(",")

            records.append({
                "source_ip": source_ip,
                "failed_logins": float(failed_logins),
                "total_attempts": float(total_attempts)
            })

    return records

def save_results(path, results):
    """Writes source_ip and status results to a file."""
    with open(path, "w") as file:
        for source_ip, status in results:
            file.write(f"{source_ip},{status}\n")

try:
    records = load_records("lab4_records.txt")
except FileNotFoundError:
    print_report("lab4_records.txt not found")
    records = []

results = []
count_ol = 0

for record in records:
    difference, percent, status = check_record(
        record["failed_logins"],
        record["total_attempts"]
    )

    if status == "OVER LIMIT":
        count_ol += 1

    results.append((record["source_ip"], status))

    print_report(
        record["source_ip"],
        record["failed_logins"],
        record["total_attempts"],
        difference,
        percent,
        status
    )

save_results("lab4_results.txt", results)
print_report(f"OVER LIMIT amount: {count_ol}")