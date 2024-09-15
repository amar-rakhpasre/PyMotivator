import requests
from twilio_conn import send_whatsapp_text,client
'''
get a qud from REST API BY catagory

'''


def get_quote_of_the_day(category):
    # API URL and key setup
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    headers = {'X-Api-Key': 'AeYuoHnmjCVoC5q2OMuqQg==6zhoFbiW7MdT9Y8n'}

    try:
        # Sending the GET request
        response = requests.get(api_url, headers=headers, timeout=10)

        # Debugging: Print the request URL and response content
        #print(f"Request URL: {api_url}")
        #print(f"Response Content: {response.text}")

        # Checking for a successful response
        if response.status_code == requests.codes.ok:
            quote_data = response.json()
            if len(quote_data) > 0:
                quote = quote_data[0]
                return f"Quote: {quote['quote']}\nAuthor: {quote['author']}"
            else:
                return "No quotes found for the selected category."
        else:
            return f"Error {response.status_code}: Unable to fetch quotes. Response: {response.text}"

    except requests.exceptions.Timeout:
        return "Error: The request timed out. Please try again later."
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the server. Please check your internet connection."
    except requests.exceptions.RequestException as e:
        return f"Error: An unexpected error occurred. {str(e)}"

# Call the function to get a quote in the "happiness" category
quote = get_quote_of_the_day(category="failure")

send_whatsapp_text(client,quote)
