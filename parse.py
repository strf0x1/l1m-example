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
    base_url="http://localhost:10337",
    provider=ProviderOptions(
      model="mistral-small-24b-instruct-2501",
      url="http://host.docker.internal:1234/v1/",
      key="not-needed"
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
