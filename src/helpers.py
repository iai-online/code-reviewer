import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def first_text(response):
  """Returns the text of the first text block in the Messages API response."""
  for block in response.content:
    if block.type == "text":
      return block.text
  return ""