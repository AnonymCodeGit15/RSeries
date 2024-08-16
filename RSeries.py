"""Evaluating conditionally convergent series and checking the validity of the Riemann Series Theorem numerically"""
from decimal import *
from tqdm import tqdm
import time
import sys
import os


def generate_positive_term_s1(n) -> Decimal:
    """Generates positive term of series S1: 1 -1/3 + 1/5 +....
       :type n: int
       """
    # print(f" + 1/{4 * n + 1}", end=" ")
    return Decimal(1) / Decimal(4 * n + 1)


def generate_negative_term_s1(n) -> Decimal:
    """Generates negative term of series S1: 1 -1/3 + 1/5 +....
       :type n: int
       """
    n += 1
    # print(f" - 1/{4 * n - 1}", end=" ")
    return (Decimal(1) / Decimal(4 * n - 1)) * Decimal(-1)


getcontext().prec = 28


def normal_sum_to_100_million_terms() -> Decimal:
    """Sum up the infinite series S1: 1 -1/3 + 1/5 - 1/7 ... up to 40000000 terms in the order specified"""
    print("Calculating the sum of series S1 : ")
    s_arr = ["1 ", "- 1/3 ", "+ 1/5 ", "- 1/7 ", "+ 1/9 ", "... "]
    for i in s_arr:
        time.sleep(0.5)
        print(i, end="",flush=True)
    print("")
    s1_sum = Decimal(0)
    for i in tqdm(range(20000000), desc="Calculating Series S1"):
        s1_sum += generate_positive_term_s1(i)
        s1_sum += generate_negative_term_s1(i)
    return s1_sum


def alternative_sum_to_100_million_terms() -> Decimal:
    """Sum up the infinite series S2: 1 + 1/5 - 1/3 + 1/9 ...  up to 40000000 terms in the alternative order"""
    print("Calculating the sum of series S2 : ")
    s_arr = ["1 ", "+ 1/5 ", "- 1/3 ", "+ 1/9 ", "... "]
    for i in s_arr:
        time.sleep(0.5)
        print(i, end="",flush=True)
    print("")
    s2_sum = Decimal(0)
    sc = 0
    for i in tqdm(range(int(40000000 / 3)), desc="Calculating Series S2"):
        s2_sum += generate_positive_term_s1(sc)
        s2_sum += generate_positive_term_s1(sc + 1)
        sc += 2
        s2_sum += generate_negative_term_s1(i)

    return s2_sum


sumS1 = normal_sum_to_100_million_terms()
sumS2 = alternative_sum_to_100_million_terms()
print(f"Sum of series S1 is {sumS1}")
print(f"Sum of series S2 is {sumS2}")
print("")
os.system("pause")
sys.exit(0)
