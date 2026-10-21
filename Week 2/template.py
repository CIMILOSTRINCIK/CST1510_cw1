"""
RECORD CHECK  -  my version
===========================

Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  01.10.2026

Run it:   python template.py
"""

count = 0
while True:
    source_ip = input("Source IP: ('quit' for quit) ")
    if source_ip == "quit":
        print(f"OVER LIMIT: {count}")
        break
    failed_logins = float(input("Failed logins: "))
    total_attempts = float(input("Total attempts: "))
    difference = total_attempts - failed_logins
    percent = (failed_logins / total_attempts) * 100
    if percent >= 100:
       status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    if status == "OVER LIMIT":
        count += 1
    print()
    print("=" * 34)
    print(f"  Source IP  -  {source_ip}")
    print("=" * 34)
    print(f"Failed logins: {failed_logins:>19.2f}")
    print(f"Total Attempts: {total_attempts:>18.2f}")
    print(f"Difference: {difference:>+22.2f}")
    print(f"Percent: {percent:>23.2f} %")
    print("=" * 34)
    print(f"  Status      :       {status}")
    print("=" * 34)
    print()
    print()