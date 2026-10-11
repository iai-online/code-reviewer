from dotenv import load_dotenv
import sys
import anthropic
import json
from helpers import ROOT, first_text

# Loads variables from .env into system environment variables
load_dotenv() 

client = anthropic.Anthropic()        						# Reads ANTHROPIC_API_KEY
review_response_schema = json.load(open(ROOT / "schemas" / "findings.json"))
rubric = open(ROOT / "prompts" / "system.md").read()

def review_diff(diff_text):
	response = client.messages.create(
		model="claude-sonnet-5",
		max_tokens=1024,										# Max token limit for the response
		system=rubric,
		messages=[
			{
				"role": "user",
				"content": "Review this diff:\n\n" + diff_text
			}
		],
		output_config={
			"format": {
				"type": "json_schema",
				"schema": review_response_schema
			}
		}
	)

	return json.loads(first_text(response))["findings"]


if __name__ == "__main__":
	for finding in review_diff(open(sys.argv[1]).read()):
		print(f"[{finding['severity']}] {finding['file']}:{finding['line']}")
		print(f"    {finding['issue']}")
		print(f"    fix: {finding['suggestion']}")