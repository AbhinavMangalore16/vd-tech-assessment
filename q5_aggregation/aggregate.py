from collections import defaultdict
from typing import List, Dict, Callable
import logging

# Configure logging
logging.basicConfig(
    filename='aggregation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def aggregation(data: List[Dict], key: str, aggregator: Callable):
    try:
        logging.info(f"Aggregating data by key: {key}")
        grouped_data = defaultdict(list)
        for item in data:
            grouped_data[item[key]].append(item)
        result = {}
        for k, v in grouped_data.items():
            result[k] = aggregator(v)
            logging.info(f"Aggregated result for {k}: {result[k]}")
        return result
    except Exception as e:
        logging.error(f"Error during aggregation: {e}")

data = [{'category': 'fruit', 'price': 10}, {'category': 'fruit', 'price': 20}, {'category': 'vegetable', 'price': 15}]
result = aggregation(data, 'category', lambda x: sum(item['price'] for item in x))
print(result)
