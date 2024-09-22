from collections import defaultdict
from typing import List, Dict, Callable
def aggregation(data: List[Dict], key:str, aggregator: Callable):
    grouped_data = defaultdict(list)
    for item in data:
        grouped_data[item[key]].append(item)
    d = {}
    for k, v in grouped_data.items():
        d[k] = aggregator(v)
    return d

data = [{'category': 'fruit', 'price': 10}, {'category': 'fruit', 'price': 20}, {'category': 'vegetable', 'price': 15}]
result = aggregation(data, 'category', lambda x: sum(item['price'] for item in x))
print(result)