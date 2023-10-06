class EducationalChatbot:
    def __init__(self):
        self.math_questions = {
            "1": "What is 2 + 2?",
            "2": "What is the square root of 16?",
            "3": "What is 10 divided by 2?"
        }

        self.math_answers = {
            "1": "The sum of 2 and 2 is 4.",
            "2": "The square root of 16 is 4.",
            "3": "10 divided by 2 is 5."
        }

    def get_response(self, user_input):
        if user_input in self.math_questions:
            question_id = user_input
            return self.math_answers.get(question_id, "Sorry, I don't know the answer to that question.")
        else:
            return "I'm sorry, I don't understand that question."

    def start_conversation(self):
        print("Welcome to the Educational Chatbot!")
        print("You can ask me questions about mathematics.")
        print("To exit, type 'exit'.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            response = self.get_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    chatbot = EducationalChatbot()
    chatbot.start_conversation()
