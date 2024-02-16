#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations
from collections import defaultdict


class TinyApriori:
    def __init__(self, transactions, min_support=0.5, min_confidence=0.5):
        """
        Initialize the Apriori algorithm.

        Args:
            transactions (list): A list of sets, where each set represents a transaction.
            min_support (float): Minimum support threshold.
            min_confidence (float): Minimum confidence threshold.
        """
        if not isinstance(transactions, list) or not all(isinstance(t, set) for t in transactions):
            raise ValueError("Transactions must be a list of sets.")
        if not 0 < min_support <= 1:
            raise ValueError("Support must be between 0 and 1.")
        if  not 0 < min_confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1.")
        self.transactions = transactions
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.itemsets = {}
        self.rules = []

    def _generate_candidates(self, itemset, length):
        """
        Generate candidate itemsets of a given length.

        Args:
            itemset (list): List of itemsets.
            length (int): Length of the itemsets to generate.

        Returns:
            set: Candidate itemsets.
        """
        candidates = set()
        for i in range(len(itemset)):
            for j in range(i + 1, len(itemset)):
                if len(itemset[i] | itemset[j]) == length:
                    candidates.add(itemset[i] | itemset[j])
        return candidates

    def _calculate_support(self, itemset):
        """
        Calculate the support of an itemset.

        Args:
            itemset (set): The itemset to calculate support for.

        Returns:
            float: The support value.
        """
        count = 0
        for transaction in self.transactions:
            if itemset.issubset(transaction):
                count += 1
        return count / len(self.transactions)

    def _get_frequent_itemsets(self):
        """
        Generate frequent itemsets.
        """
        itemsets = [frozenset([item]) for item in self.transactions[0]]
        self.itemsets[1] = {itemset: self._calculate_support(itemset) for itemset in itemsets}

        k = 2
        while self.itemsets[k - 1]:
            candidates = self._generate_candidates(list(self.itemsets[k - 1].keys()), k)
            frequent_itemsets = {}
            for candidate in candidates:
                support = self._calculate_support(candidate)
                if support >= self.min_support:
                    frequent_itemsets[candidate] = support
            self.itemsets[k] = frequent_itemsets
            k += 1

    def _generate_rules(self):
        """
        Generate association rules.
        """
        for size in range(2, len(self.itemsets)):
            for itemset in self.itemsets[size]:
                for i in range(1, size):
                    for antecedent in combinations(itemset, i):
                        antecedent = frozenset(antecedent)
                        consequent = itemset - antecedent
                        confidence = self.itemsets[size][itemset] / self.itemsets[len(antecedent)][antecedent]
                        if confidence >= self.min_confidence:
                            self.rules.append((antecedent, consequent, confidence))

    def find_association_rules(self):
        """
        Find association rules based on the transactions.

        Returns:
            list: A list of association rules.
        """
        if not self.transactions:
            raise ValueError("No transactions provided.")
        
        self._get_frequent_itemsets()
        if not self.itemsets:
            raise ValueError("No frequent itemsets found.")
        
        self._generate_rules()
        return self.rules
