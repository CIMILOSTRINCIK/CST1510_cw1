"""
RECORD CHECK  -  my version
===========================
Name  : Amal Iliasov
Lane  :  IT      (delete two)
Date  : 24.09.2026
"""

label = input("Text:")
first = float(input("First:"))
second = float(input("Second:"))
difference = (second - first)
percent = (first / second * 100)
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"First: {first:>27.2f}")
print(f"Second: {second:>26.2f}")
print(f"Difference: {difference:>+22.2f}")
print(f"Percent: {percent:>23.2f} %")
print("=" * 34)