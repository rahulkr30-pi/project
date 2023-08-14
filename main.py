from chatbot import ChatBot
from sample_responses import sample_goodbyes, sample_greetings

def main():
    bot = ChatBot()
    print("ChatBot:", sample_greetings[0])

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "goodbye"]:
            print("ChatBot:", sample_goodbyes[0])
            break

        response = bot.generate_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
