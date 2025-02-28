from pydantic import BaseModel
from l1m import L1M, ClientOptions, ProviderOptions
import os

class ContactDetails(BaseModel):
  email: str
  phone: str

class UserProfile(BaseModel):
  name: str
  company: str
  contactInfo: ContactDetails

# Get API key from environment variable
openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
if not openrouter_api_key:
  raise ValueError("OPENROUTER_API_KEY environment variable is not set")

client = L1M(
  options=ClientOptions(
    base_url="http://localhost:10337",
    provider=ProviderOptions(
      model="google/gemini-2.0-flash-lite-001",
      url="https://openrouter.ai/api/v1/",
      key=openrouter_api_key
    )
  )
)

# Generate a structured response
try:
  user_profile = client.structured(
    input="John Smith was born on January 15, 1980. He works at Acme Inc. as a Senior Engineer and can be reached at john.smith@example.com or by phone at (555) 123-4567.",
    # OR   input="<BASE64_ENCODED_IMAGE>",
    schema=UserProfile,
    instruction="Extract details from the provided text."
  )
  print("User profile:", user_profile)
except Exception as e:
  print("Error type:", type(e))
