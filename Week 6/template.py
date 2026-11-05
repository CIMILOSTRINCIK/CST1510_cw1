"""
RECORD CHECK  -  my version
===========================

Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  05.11.2026

Run it:   python template.py
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_attempts.csv")
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

print("FULL DATA:")
print(df)

filtered_df = df[df["status"] != "OK"]
print("\nROWS THAT ARE NOT OK:")
print(filtered_df)

status_counts = df.groupby("status").size()
print("\nCOUNT PER STATUS:")
print(status_counts)

df.to_csv("survey_results.csv", index=False)
status_counts.plot(kind="bar")

plt.title("Login Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of Sources")
plt.tight_layout()
plt.savefig("login_status_counts.png")