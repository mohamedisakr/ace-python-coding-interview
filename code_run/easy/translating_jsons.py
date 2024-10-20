# https://coderun.yandex.ru/problem/merge-jsons-2
import sys
import json


def main():
    """
    merge all feeds of one store into a single feed. 
    Since the feed can be quite large, you only need to leave m first in 
    the order of succession in the input data of product offers.
    """
    n, m = map(int, input().split())
    print(f'n : {n}')
    print(f'm : {m}')


if __name__ == '__main__':
    main()

store_feed_1 = {"offers":
                [
                    {"offer_id": "offer1", "market_sku": 10846332, "price": 1490},
                    {"offer_id": "offer2", "market_sku": 682644, "price": 499}
                ]
                }


store_feed_2 = {"offers":
                [
                    {"offer_id": "offer3", "market_sku": 832784, "price": 14000},
                    {"offer_id": "offer4", "market_sku": 3234, "price": 100}
                ]
                }

product_feed = {"offers":
                [
                    {"market_sku": 10846332, "offer_id": "offer1", "price": 1490},
                    {"market_sku": 682644, "offer_id": "offer2", "price": 499},
                    {"market_sku": 832784, "offer_id": "offer3", "price": 14000}
                ]
                }

# print(store_feed_1["offers"])
# print(store_feed_1["offers"][0])

# store_feed_combined = store_feed_1 | store_feed_2
# print(store_feed_combined)

# Serialize the dictionary into a JSON formatted string
# json_data = json.dumps(store_feed_combined, indent=4, separators=(
#     ",", ": "))


# Output the JSON string
# print(json_data)


def construct_jsons(jsons):
    combined_offers = []

    # Collect all offers
    for json_str in jsons:
        data = json.loads(json_str)
        combined_offers.extend(data["offers"])

    # Sort combined offers by 'market_sku'
    combined_offers = sorted(combined_offers, key=lambda x: x['market_sku'])

    # Create the final merged JSON object
    result = {"offers": combined_offers}
    return json.dumps(result)


# Example usage
jsons = [
    '{"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 1490}, {"offer_id": "offer2", "market_sku": 682644, "price": 499}]}',
    '{"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}, {"offer_id": "offer4", "market_sku": 3234, "price": 100}]}'
]

output = construct_jsons(jsons)
print(output)
