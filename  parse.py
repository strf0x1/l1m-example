from pydantic import BaseModel
from l1m import L1M, ClientOptions, ProviderOptions

class ContactDetails(BaseModel):
  email: str
  phone: str

class UserProfile(BaseModel):
  name: str
  company: str
  contactInfo: ContactDetails


client = L1M(
  options=ClientOptions(
    base_url="http://localhost:10377",
    provider=ProviderOptions(
      model="mistral-small-24b-instruct-2501",
      url="http://localhost:1234/v1/chat/completions",
      key="your-api-key-here"
    )
  )
)

# Generate a structured response
user_profile = client.structured(
  input="John Smith was born on January 15, 1980. He works at Acme Inc. as a Senior Engineer and can be reached at john.smith@example.com or by phone at (555) 123-4567.",
  # OR   input="<BASE64_ENCODED_IMAGE>",
  schema=UserProfile,
  instruction="Extract details from the provided text.", # Optional
  options=RequestOptions(cache_ttl=100) # Optional
)