import openai

# openAi API key
openai.api_key = "your API keys"
model_engine = "text-davinci-002"

def generate_response(prompt):
  completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=4000,#tokens limit is 4096
    n=1,
    stop=None,
    temperature=0.85 
    
  )

  message = completions.choices[0].text
  return message.strip()

while True:
  # Get user input
  prompt = input("You: ")

  # Check if the user wants to exit
  if prompt.lower() in ["exit", "quit", "goodbye", "bye"]:
    print("Chatbot: Goodbye! Have a nice day.")
    break

  # Generate a response and print it
  response = generate_response(prompt)
  print("Chatbot: " + response)


