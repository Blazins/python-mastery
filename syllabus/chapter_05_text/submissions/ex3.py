#Ex3 - Deduplicating messy signups

signups = (
    "  Ada Lovelace <ADA@shop.co>  ",
    "Grace Hopper <grace@shop.co>",
    "ada lovelace <ada@shop.co>",
    "Alan Turing <alan@SHOP.co>",
    "Grace Hopper <GRACE@shop.co>",
    "Katherine Johnson <katherine@shop.co>",
)

email_start = 0
identities = []
first_signups = []
duplicate_signups = []
actual_emails = []
actual_names = []
problems = []
rejected = []


for line, signup in enumerate(signups):
    entry = signup.strip().split("<")

    if len(entry) < 2:
        reason = '— malformed'
        names = entry[0].strip()
        rejected.append((names,line, reason))
        continue
    else:
        names = entry[0].strip()
        emails = entry[1].strip().split('>')
        actual_email = emails[0].lower()
        #print(actual_email)



        if actual_email not in first_signups:
            first_signups.append(actual_email)
        else:
            duplicate_signups.append((line,actual_email, names))



for email in first_signups:
    for signup in signups:
        entry = signup.strip().split("<")
        if len(entry) < 2:
            continue
        emails = entry[1].strip().split('>')
        actual_email = emails[0].lower()
        names = entry[0].strip()
        if actual_email == email:
            identities.append((email, names))

print(f"KEPT ({len(first_signups)})")
for index, actual_email in enumerate(first_signups, start = 1):
    for email, name in identities:
        if email == actual_email:
            print(f"{index}. {name:<20}{actual_email}")
            break

print("REJECTED")
if duplicate_signups:
    for line, email,name in duplicate_signups:
        print(f"  line {line}: {name} already signed up as {email}")


if rejected:
    for name, line, reason in rejected:
        print(f"  line {line}: {name} {reason}")
        break



print("-" * 46)
print(f"{len(signups)} signups   {len(first_signups)} unique   {len(duplicate_signups)} duplicate   {len(rejected)} malformed")





