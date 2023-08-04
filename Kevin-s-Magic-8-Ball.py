import random

def magic_8_ball():
    responses = [
        "Yes",
        "No",
        "Maybe",
        "Try Again Later",
        "Absolutely Not!",
        "Absolutely!",
		"Possibly",
		"You are a terrible person to ask that!",
		"What an incredible question! I will have to take my time to ... NO!"
    ]

    while True:
        print("Ask Kevin's Magic 8 Ball a question...")
  

        question = input()
        if not question.strip():
            print("Kevin's Magic 8-Ball cannot answer if you do not ask! Ask your question!")
        else:
            answer = random.choice(responses)
            print("Kevin's Magic 8 Ball says:", answer)

        choice = input("Do you want to ask another question? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    magic_8_ball()
