import discord
import openai
import json

# Read configuration from settings.json
with open("settings.json", "r") as config_file:
    config = json.load(config_file)

# Extract the OpenAI API key and Discord bot token from the configuration
OPENAI_API_KEY = config["openai_api_key"]
DISCORD_BOT_TOKEN = config["discord_bot_token"]

# ... Rest of the code remains unchanged ...

# Initialize the Discord client
client = discord.Client()

# Function to interact with the OpenAI API
def get_openai_response(message):
    openai.api_key = OPENAI_API_KEY
    # Fine-tune the response using the Andrew Tate-like examples
    examples_prompt = "\n".join(andrew_tate_examples)
    prompt = f"{examples_prompt}\nUser: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
    )
    return response.choices[0].text.strip()

# Event listener for when the bot is ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# Event listener for when a message is received
@client.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    # Check if the message starts with a specific trigger command
    if message.content.startswith("!tate"):
        # Extract the user input (excluding the trigger command)
        user_input = message.content[len("!tate"):].strip()

        # Call the OpenAI API to get the response
        response = get_openai_response(user_input)

        # Send the response back to the Discord channel
        await message.channel.send(response)

# Run the bot
client.run(DISCORD_BOT_TOKEN)
