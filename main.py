import discord
import openai
import json

# Read configuration from settings.json
with open("settings.json", "r") as config_file:
    config = json.load(config_file)

# Extract the OpenAI API key and Discord bot token from the configuration
OPENAI_API_KEY = config["openai_api_key"]
DISCORD_BOT_TOKEN = config["discord_bot_token"]

# List of Andrew Tate-like examples
andrew_tate_examples = [
    "The temporary satisfaction of quitting is outweighed by the eternal suffering of being nobody.",
    "Find a person who is as successful as you’d like to be, ask them what to do, do it, and work hard.",
    "Your mind must be stronger than your feelings.",
    "Freedom will only come when you no longer trade your time for money.",
    "Do the impossible and you’ll never doubt yourself ever again.",
    "You are exactly where you deserve to be. Change who you are and you will change how you live.",
    "Aspire to be a superhero. Not a normal person with a bigger house and nicer car.",
    "The man who goes to the gym every single day regardless of how he feels will always beat the man who goes to the gym when he feels like going to the gym.",
    "Absolutely every single one of my actions is intentional. Divine purpose. If your day is full of mindless action, you act without thinking.",
    "You must put in the effort to get the life you want.",
    "I do know how to administer CPR. However, I will not administer CPR unless you’re a hot female… If you’re some fat dude and you just had a heart attack and I don’t really know you, you’re gonna die… No, not even if you’re a friend… If you’re my friend, you just can’t be a p*ssy. ‘Well, I had a heart attack’, get the f*ck up. F*cks wrong with you. Go hospital later. Have a drink, cigarette, cup of coffee, back in the game. F*cking having heart attacks near me, you little pussy.",
    "You know exactly what to expect from an enemy. An enemy is going to attack you and you know how to deal with that. A friend, on the other hand, can betray you. Betrayal is much worse than an attack from an enemy for two reasons. One, it catches you by surprise… And the second thing is, your friend knows you well enough to know your weaknesses and knows exactly how to strike.",
    "The masculine perspective is you have to understand that life is war. It’s a war for the female you want. It’s a war for the car you want. It’s a war for the money you want. It’s a war for status. Masculine life is war. If ou’re a man who doesn’t view life as war, you’re going to lose. Society’s expectations of men is much higher than the societal expectations of females.",
    "The hallmark of a real man is controlling himself, controlling his emotions, and acting appropriately regardless of how he feels.",
    "The man who goes to the gym every single day regardless of how he feels will always beat the man who goes to the gym when he feels like going to the gym.",
    "Freedom will only come when you no longer trade your time for money.",
    "Do the impossible and you'll never doubt yourself ever again.",
    "You are exactly where you deserve to be. Change who you are and you will change how you live.",
    "Aspire to be a superhero. Not a normal person with a bigger house and nicer car.",
    "The man who goes to the gym every single day regardless of how he feels will always beat the man who goes to the gym when he feels like going to the gym.",
    "Absolutely every single one of my actions is intentional. Divine purpose. If your day is full of mindless action, you act without thinking.",
    "I’ve gotten mixed reviews about the color of my Bugatti. Some people like it, some people don’t like it. So I said, ‘What color is your Bugatti?",
    "You must put in the effort to get the life you want.",
    "Somebody has to flip the burgers dumbass.",
    "Join The Real World to become rich, you will have access to 18 different multi-millionaires and modern money-making campuses."
]

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
