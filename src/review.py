from dotenv import load_dotenv
import sys
import anthropic

# Loads variables from .env into system environment variables
load_dotenv() 

client = anthropic.Anthropic()        						# Reads ANTHROPIC_API_KEY
diff_text = open(sys.argv[1]).read()

response = client.messages.create(
	model="claude-sonnet-5",
  	max_tokens=1024,										# Max token limit for the response
  	system="You are a careful code reviewer. Be specific.",
  	messages=[
    	{
        	"role": "user",
			"content": "Review this diff:\n\n" + diff_text
		}
    ]
)

for block in response.content:      						# The response is a list of blocks
	if block.type == "text":
		print(block.text)

print(f"{response.stop_reason}")
print(f"{response.usage.input_tokens}")
print(f"{response.usage.output_tokens}")