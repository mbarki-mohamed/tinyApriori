# TinyApriori
A tiny python implementation of the Apriori algorithm to find frequent itemsets.

## Usage
After installing the package, startby importing the TinyApriori class;

Next, create a list of python sets containing the current itemsets combinations
and choose the minimum_support and minimum_confidence values (Note: they should be between 0 and 1)
```python
from TinyApriori import TinyApriori

transactions = [
    {'California', 'Texas', 'New York'},
    {'California', 'Texas', 'Florida'},
    {'California', 'Texas', 'New York', 'Florida'},
    {'California', 'Texas'},
    {'Texas', 'New York'},
    {'California', 'Texas'}
]

apriori = TinyApriori(transactions, min_support=0.4, min_confidence=0.7)

# This line converts the result into a list of tuples;
# each tuple has 3 values: antecedent as a frozenset, consequent as a frozenset and confidence as a float)
rules = apriori.find_association_rules()

for antecedent, consequent, confidence in rules:
    print(f"{antecedent} => {consequent} (Confidence: {confidence})")
```

The code above prints for each itemset (antecedent), the confidence of percentage of getting a consequent

A confidence of 1.0 meaning that in 100% of the cases; whenever we have the antecedent, we also have the consequent, explaining maximum association rule.
```python
frozenset({'New York'}) => frozenset({'Texas'}) (Confidence: 1.0)
frozenset({'California'}) => frozenset({'Texas'}) (Confidence: 1.0)
frozenset({'Texas'}) => frozenset({'California'}) (Confidence: 0.8333333333333334)
```
