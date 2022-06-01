bids = {}
ans = "Yes"
while ans == "Yes" or ans == "yes" or ans == "YES":
    n = input("Name : ")
    amt = int(input("Bid Amount : "))
    bids[n] = amt
    ans = input("Anymore bidders ?")

a = max(bids.values())
for keys in bids:
    if bids[keys] == a:
        print("Higest bidder is ", keys)