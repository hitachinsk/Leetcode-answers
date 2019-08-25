# Description
A transaction is possibly invalid if:
- the amount exceeds $1000, or;
- if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

Each transaction string `transactions[i]` consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.
Given a list of `transactions`, return a list of transactions that are possibly invalid.  You may return the answer in any order.

**Example1:**
```
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
```
**Example2:**
```
Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
```
**Example3:**
```
Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
```
**Constraints:**
- `transactions.length <= 1000`
- Each `transactions[i]` takes the form `"{name},{time},{amount},{city}"`
- Each `{name}` and `{city}` consist of lowercase English letters, and have lengths between `1` and `10`.
- Each `{time}` consist of digits, and represent an integer between `0` and `1000`.
- Each `{amount}` consist of digits, and represent an integer between `0` and `2000`.

# Code
```python3
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ret = []
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(',')
            time, amount = int(time), int(amount)
            if amount > 1000:
                ret.append(transactions[i])
            for j in range(i+1, len(transactions)):
                namej, timej, amountj, cityj = transactions[j].split(',')
                timej, amountj = int(timej), int(amountj)
                if name == namej and city != cityj and abs(timej - time) <= 60:
                    ret.append(transactions[j])
                    ret.append(transactions[i])
        return set(ret)
```
