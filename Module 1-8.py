"""Session - 1"""

import random
def generate_persona():
  occupations = ["Student", "Software Engineer", "Business Owner", "Teacher", "Home Maker"]
  interests = ["Technology", "Shopping", "Education", "Finance", "Healthcare"]
  persona = {
      "name" : f"User_{random.randint(100, 999)}",
      "age" : random.randint(18,60),
      "occupation" : random.choice(occupations),
      "interest" : random.choice(interests),
      "budget" : random.choice(["Low", "Medium", "High"])
  }
  return persona
user = generate_persona()
print(user)



"""Session - 2"""

def generate_behavior(persona):
  if persona["occupation"] == "Student":
    behavior = "Price conscious"
  elif persona["occupation"] == "Software Engineer":
    behavior = "Technology focused"
  elif persona["occupation"] == "Business Owner":
    behavior = "Value focused"
  elif persona["occupation"] == "Teacher":
    behavior = "Education focused"
  elif persona["occupation"] == "Home Maker":
    behavior = "Home improvement focused"
  elif persona["occupation"] == "Senior citizen":
    behavior = "Simplicity/ Accessibility/ Reliability focused"
  else:
    behavior = "Convenience focused"
  persona["behavior"] = behavior
  return persona
user = generate_behavior(user)
print(user)



"""Session - 3"""

class UserMemory:
    def __init__(self):
        self.memory = []

    def add_memory(self, question, answer):
        self.memory.append({
            "question": question,
            "answer": answer
        })

    def show_memory(self):
        return self.memory

user_memory = UserMemory()

user_memory.add_memory(
    "Shopping budget",
    "2000"
)

user_memory.add_memory(
    "Preferred category",
    "Electronics"
)

print(user_memory.show_memory())



"""Session - 4"""

def generate_psychology():
  profile = {
      "risk_taking" : random.choice(
          ["Low", "Medium", "High"]
      ),
      "price_sensitivity" : random.choice(
          ["Low", "Medium", "High"]
      ),
      "brand_loyalty" : random.choice(
          ["Low", "Medium", "High"]
      ),
      "technology_adoption" : random.choice(
          ["Low", "Medium", "High"]
      )
  }
  return profile
print(generate_psychology())



"""Session - 5"""

def generate_answer(question, persona):
  if persona['behavior'] == 'Price Conscious' :
    answer={
        'I would prefer affordable pricing'
        'and attractive discounts.'
    }
  elif persona['behavior'] == 'Technology Focused':
    answer={
        'I would prefer advanced features'
        'and a smooth digital experience.'
    }
  else:
    answer={
        'I would prefer a simple and convenient'
        'application.'
    }
  return answer
user = generate_persona()
user = generate_behavior(user)
question = 'what do you expect for this product?'
print(generate_answer(question, user))



"""Session - 6"""

features = [
    'free delivery',
    'cash on delivery',
    'AI recommendations'
]
def test_features():
  results = []
  for feature in features:
    rating = random.randint(1,5)
    results.append({
        'feature' : feature,
        'rating' : rating
    })
  return results
print(test_features())



"""Session - 7"""

def simulate_journey(persona):
  journey = [
      "Open Application",
      "Search Product",
      "Compare Prices",
      "Add to cart",
      "Checkout",
      "Payment"
  ]
  if persona["budget"] == "Low":
    journey.insert(
        2,
        "Check Discounts"
    )
  return journey
user = generate_persona()
print(simulate_journey(user))



"""Session - 8"""

def persona_agent():
  return generate_persona()
def interview_agent(user):
  user = generate_behavior(user)
  return generate_answer(
      "What do you expect?",
      user
  )
def product_testing_agent():
  return test_features()
def journey_agent(user):
  return simulate_journey(user)
def main_orchestrator():
  user = persona_agent()
  interview = interview_agent(user)
  testing = product_testing_agent()
  journey = journey_agent(user)
  return {
      "persona" : user,
      "interview" : interview,
      "testing" : testing,
      "journey" : journey
  }
print(main_orchestrator())