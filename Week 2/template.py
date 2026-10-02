"""
RECORD CHECK  -  my version
===========================

Name  :  Amal Iliasov
Lane  :  Cyber      (delete two)
Date  :  01.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

count = 0
while True:
    label = input("Text: ")
    if label == "quit":
        print(f"OVER LIMIT: {count}")
        break
    value = float(input("Value: "))
    limit = float(input("Limit: "))
    difference = limit - value
    percent = (value / limit) * 100
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
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Used        : {value:19.2f}")
    print(f"Total       : {limit:19.2f}")
    print(f"Difference  : {difference:19.2f}")
    print(f"Percent     : {percent:18.2f} %")
    print("=" * 34)
    print(f"  Status      :       {status}")
    print("=" * 34)
    print()
    print()