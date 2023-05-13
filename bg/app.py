from flask import Flask, render_template, request
import openai
openai.api_key = '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'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processes', methods=['POST'])
def process():
    user_input = request.form['user_input']
    # Perform any necessary processing on user input
    # For example, you can pass it to a function and get the output
    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the GPT-3.5 engine
        prompt=user_input,
        max_tokens=4000,  # Adjust the response length as needed
        temperature=0.7,  # Adjust the temperature for response randomness
        n=1,  # Generate a single response
        stop=None,  # Optional stop sequence to end the response
        timeout=10,  # Optional timeout for the API request
        )
    output=response.choices[0].text.strip()
   # output = chat_with_gpt(user_input)
    return render_template('index.html', output=output)

def process_user_input(user_input):
    # Perform processing on user input and return the output
    # This can be any Python code or logic you want
    return user_input.upper()

if __name__ == '__main__':
    app.run(debug=True)

    

# Set up your OpenAI API credentials


# Define a function to send a message to ChatGPT and get a response
def chat_with_gpt(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the GPT-3.5 engine
        prompt=message,
        max_tokens=4000,  # Adjust the response length as needed
        temperature=0.7,  # Adjust the temperature for response randomness
        n=1,  # Generate a single response
        stop=None,  # Optional stop sequence to end the response
        timeout=10,  # Optional timeout for the API request
    )
    return response.choices[0].text.strip()

# Start a conversation with ChatGPT
#print("You: Hello!")
# print("ChatGPT:", chat_with_gpt("Hello!"))
# print("You:", chat_with_gpt("How are you?"))
# print("ChatGPT:", chat_with_gpt("I'm good. How about you?"))
# Continue the conversation...
#print(chat_with_gpt(input("Enter query: ")))

while True:
    try:
       print( chat_with_gpt(input("Enter query: "))) 
    except Exception:
        print('Sorry no result, please be clear')
    user_input = input('To continue press y: ')
    if user_input != 'y':
        break