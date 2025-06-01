mails = []
confirm = False
while True:
    c = input().strip()
    c = c[:5]
    if not confirm and c.strip() == "end":
        confirm = True
        continue
    if confirm and c == "end":
        print(mails)
        print(*set(mails), sep=", ")
        print(f"count = {len(mails)}, unique count: {len(set(mails))}")
        break
    if confirm:
        confirm = False
    mails.append(c+ "@snu.edu.in")