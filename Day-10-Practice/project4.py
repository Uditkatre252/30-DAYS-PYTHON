import re
import datetime
import random
from urllib import response


def chatbot():
    user_name = None

    patterns = [
        (r'\b(hi|hello|hey)\b', ["Hello!", "Hey there!", "Hi 👋"]),

        (r'\b(your name|who are you)\b',
         ["I am a chatbot.", "You can call me your assistant 🤖"]),

        (r'\b(how are you|how r u)\b',
         ["I'm doing great!", "All good here 😄 What about you?"]),

        (r'\b(know udit)\b',
         ["My boss is a handsome man 😎"]),

        (r'\b(my name is (\w+))\b', None),  # special handling

        (r'\b(date)\b', None),  # dynamic

        (r'\b(time)\b', None),  # dynamic

        (r'\b(bye|exit|quit)\b',
         ["Goodbye! 👋", "See you soon!", "Take care!"]),
    ]

    while True:
        user_input = input("You: ").lower()
        matched = False

        for pattern, response in patterns:
            match = re.search(pattern, user_input)

            if match:
                matched = True

                # 👉 Special case: user name
                if "my name is" in pattern:
                    user_name = match.group(2)
                    print(f"Bot: Nice to meet you, {user_name}!")
                    break

                # 👉 Date
                elif pattern == r'\b(date)\b':
                    now = datetime.datetime.now()
                    print(f"Bot: Today's date is {now.day}/{now.month}/{now.year}")
                    break

                # 👉 Time
                elif pattern == r'\b(time)\b':
                    now = datetime.datetime.now()
                    print(f"Bot: Current time is {now.strftime('%H:%M:%S')}")
                    break

                # 👉 Normal responses
                else:
                    print("Bot:", random.choice(response))

                    # Exit condition
                    if re.search(r'\b(bye|exit|quit)\b', user_input):
                        return
                    break

        if not matched:
            if user_name:
                print(f"Bot: Sorry {user_name}, I didn't understand that.")
            else:
                print("Bot: I didn't understand that. Try saying hi, ask time, or tell me your name!")


chatbot()



