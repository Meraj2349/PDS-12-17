import json
import csv
from datetime import datetime
from utils import match_query_advanced, detect_sentiment


# Load categories and responses
def load_responses(file_path="data/responses.json"):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)  # Parse the JSON file
            return data  # Return as a Python dictionary
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {"categories": {}, "responses": {}}  # Return an empty structure
    


# Log user queries and responses
def log_query(query, category, response, sentiment, log_file="logs/query_logs.csv"):
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, query, category, response, sentiment])


# Start chat session
def start_chat(responses):
    
    print(" Customer Support Chatbot!")
   
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Thank you for chatting. Goodbye!")
            break

        # Match query to a category
        category = match_query_advanced(user_query, responses["categories"])

        # Generate the response
        response = responses["responses"].get(
            category, "Sorry, I couldn't understand that."
        )

        # Detect sentiment
        sentiment = detect_sentiment(user_query)

        # Display the response and sentiment
        print(f"Bot: {response} (Sentiment: {sentiment})")

        # Log the query
        log_query(user_query, category, response, sentiment)


# View logs
def view_logs(log_file="logs/query_logs.csv"):
    
    try:
        with open(log_file, "r") as file:
            print("\n--- Query Logs ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No logs found.")


# Main menu
def main_menu():
    responses = load_responses()
    while True:
        print("\n--- Customer Support Chatbot ---")
        print("1. Start Chat")
        print("2. View Logs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_chat(responses)
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
