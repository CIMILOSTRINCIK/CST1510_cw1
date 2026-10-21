"""
RECORD CHECK  -  my version
===========================
Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  24.09.2026
"""

source_ip = input("Source IP:")
failed_logins = float(input("Failed logins:"))
total_attempts = float(input("Total attempts:"))
difference = (total_attempts - failed_logins)
percent = (failed_logins / total_attempts * 100)
print()
print("=" * 34)
print(f"  Source IP:  -  {source_ip}")
print("=" * 34)
print(f"Failed logins: {failed_logins:>19.2f}")
print(f"Total attempts: {total_attempts:>18.2f}")
print(f"Difference: {difference:>+22.2f}")
print(f"Percent: {percent:>23.2f} %")
print("=" * 34)