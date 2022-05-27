class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self, question):
        print(question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print('- ' + response)


question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question(question)
print("Enter 'q' at any yime yo quit. \n")
while True:
    response = input("Languge: ")
    my_survey.store_response(response)
    if response == 'q':
        break

print("\nThank's everyone ")
my_survey.show_results()