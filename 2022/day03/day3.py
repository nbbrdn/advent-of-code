from collections.abc import Iterable
from functools import reduce

def find_duplicates(comp1: str, comp2: str) -> set:
    return set(comp1) & set(comp2)

def sum_priorities(items: Iterable) -> int:
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = small_letters + small_letters.upper()
    
    priorities = 0

    for item in items:
        priorities += (letters.index(item) + 1)

    return priorities


def split_rucksack(rucksack: str) -> tuple:
    mid = len(rucksack) // 2
    return rucksack[:mid], rucksack[mid:]


def compare(first_rucksack: str, second_rucksack: str) -> str:
    common_things = set(first_rucksack.strip()) & set(second_rucksack.strip())
    return ''.join(common_things)


def count_group_priority(group: list):
    common = reduce(compare, group)
    return sum_priorities(common)


def main():
    total_priority = 0
    
    with open('input.txt') as f:
        group = []
        for rucksack in f:
            # compartment_one, compartment_two = split_rucksack(rucksack)
            # duplicate_items = find_duplicates(compartment_one, compartment_two)
            # rucksack_priority = sum_priorities(duplicate_items)
            # total_priority += rucksack_priority
            group.append(rucksack)
            if len(group) == 3:
                total_priority += count_group_priority(group)
                group.clear()

    
    print(total_priority)

if __name__ == '__main__':
    main()
