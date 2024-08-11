import json
import logging

# LOGGING SETUP
logging.basicConfig(
    filename='task_2.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug('Script started.')


try:
    with open('task_2_and_3.json') as file:
        file_data = json.load(file)
        logging.debug('JSON file loaded successfully.')
except Exception as e:
    logging.error(f'Error loading JSON file: {e}')
    raise


def most_expensive_item(data):
    most_expensive = max(data, key=lambda x: float(x['price']))
    message = f"Most expensive: {most_expensive['description']} - £{most_expensive['price']}"
    logging.debug(f"Most expensive item calculated: {message}")
    return message


def cheapest_item(data):
    cheapest = min(data, key=lambda x: float(x['price']))
    message = f"Cheapest: {cheapest['description']} - £{cheapest['price']}"
    logging.debug(f"Cheapest item calculated: {message}")
    return message


def average_price(data):
    prices = [float(item['price']) for item in data]
    avg = sum(prices) / len(prices)
    message = f"Average price: £{avg:.2f}"
    logging.debug(f"Average price calculated: {message}")
    return message


def average_price_bridgestone(data):
    bridgestone_items = [item for item in data if item['manufacturer'] == 'Bridgestone']
    if not bridgestone_items:
        message = "No Bridgestone products found"
        logging.debug(message)
        return message
    prices = [float(item['price']) for item in bridgestone_items]
    avg = sum(prices) / len(prices)
    message = f"Average price of Bridgestone products: £{avg:.2f}"
    logging.debug(f"Average price of Bridgestone products calculated: {message}")
    return message


def prices_speed_rating_v(data):
    v_rated_items = [item for item in data if item['speed'] == 'V']
    messages = [f"{item['description']} - £{item['price']}" for item in v_rated_items]
    result = "\n".join(messages)
    logging.debug(f"Prices for tyres with speed rating V calculated:\n{result}")
    return result


# Output results and log them
logging.debug("RESULT...")
print(most_expensive_item(file_data))
print(cheapest_item(file_data))
print(average_price(file_data))
print(average_price_bridgestone(file_data))
print("\n\nPrices for tyres with speed rating V:")
print("--------------------------------------\n")
print(prices_speed_rating_v(file_data))

logging.debug('Script completed.')
