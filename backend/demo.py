"""
Demo/Mock version of the AI Chef Collective
This demonstrates the application flow without requiring Azure credentials
"""
from typing import List, Dict, Any


class MockAIChefCollective:
    """Mock multi-agent system for demonstration purposes"""
    
    def run_chef_show(self, pantry_items: List[str]) -> List[Dict[str, Any]]:
        """
        Simulates the complete chef show pipeline with mock responses
        """
        steps = []
        
        # Step 1: Chef creates initial recipe
        chef_response = f"""
**Vegan Chickpea Curry with Spinach**

Ingredients:
- 2 cups chickpeas (from your pantry)
- 2 cups fresh spinach
- 1 cup coconut milk
- 2 tbsp curry powder
- 1 cup rice
- 1 onion, diced
- 3 cloves garlic, minced
- Salt and pepper to taste

Instructions:
1. Cook rice according to package directions
2. Sauté onion and garlic until fragrant
3. Add curry powder and cook for 1 minute
4. Add chickpeas and coconut milk, simmer for 10 minutes
5. Stir in spinach until wilted
6. Season with salt and pepper
7. Serve over rice

Cooking Time: 30 minutes
Servings: 4
"""
        steps.append({
            'agent': 'Chef',
            'role': 'Recipe Creator',
            'input': f"Pantry items: {', '.join(pantry_items)}",
            'output': chef_response
        })
        
        # Step 2: Nutritionist analyzes the recipe
        nutrition_response = """
**Nutritional Analysis (per serving):**

- Calories: ~420 kcal
- Protein: 15g (excellent plant-based protein from chickpeas)
- Carbohydrates: 58g (complex carbs from rice and chickpeas)
- Fat: 14g (healthy fats from coconut milk)
- Fiber: 12g (great for digestive health)

**Key Nutrients:**
- Iron: High (from spinach and chickpeas)
- Vitamin A: Excellent (from spinach)
- Folate: Good source
- Magnesium: Good source

**Nutritional Improvements:**
1. Consider adding turmeric for anti-inflammatory benefits
2. Include a squeeze of lemon for vitamin C and better iron absorption
3. Add some red bell peppers for extra vitamins and color
4. The protein-to-carb ratio is well balanced for a complete meal
"""
        steps.append({
            'agent': 'Nutritionist',
            'role': 'Nutrition Analyst',
            'input': 'Analyzing recipe nutritional content',
            'output': nutrition_response
        })
        
        # Step 3: Critic provides feedback
        critic_response = """
**Professional Review:**

**Strengths:**
- Excellent flavor profile with the curry-coconut combination
- Good texture contrast between creamy sauce and tender chickpeas
- Spinach adds fresh, earthy notes
- Well-balanced meal with protein, vegetables, and grains

**Areas for Enhancement:**
1. **Flavor Depth**: Toast the curry powder in oil before adding liquid for deeper flavor
2. **Texture**: Add some crispy elements like toasted cashews or coconut flakes on top
3. **Presentation**: Garnish with fresh cilantro and a lime wedge
4. **Technique**: Let the curry simmer a bit longer to develop richer flavors
5. **Complexity**: Consider adding ginger along with the garlic for extra warmth

**Overall Rating: 8.5/10**
A solid, approachable recipe that delivers on flavor and nutrition. With the suggested refinements, this could easily be a 9.5/10!
"""
        steps.append({
            'agent': 'Critic',
            'role': 'Food Critic',
            'input': 'Reviewing recipe and nutrition',
            'output': critic_response
        })
        
        # Step 4: Chef refines based on feedback
        final_response = """
**Refined Vegan Chickpea Curry with Spinach**

Ingredients:
- 2 cups chickpeas
- 2 cups fresh spinach
- 1 cup coconut milk
- 2 tbsp curry powder
- 1 tsp turmeric powder (added for nutrition!)
- 1 cup basmati rice
- 1 onion, diced
- 3 cloves garlic, minced
- 1 inch ginger, grated (enhanced!)
- 1 red bell pepper, diced (added!)
- 1/4 cup toasted cashews (for texture!)
- Fresh cilantro for garnish
- Lime wedges for serving
- 2 tbsp coconut oil
- Salt and pepper to taste

Enhanced Instructions:
1. Cook basmati rice according to package directions
2. Heat coconut oil in a large pan over medium heat
3. **Toast curry powder and turmeric** for 30 seconds until fragrant
4. Add onion, garlic, and ginger - sauté until golden
5. Add bell pepper and cook for 3 minutes
6. Add chickpeas and coconut milk
7. **Simmer for 15 minutes** to develop deep flavors
8. Stir in spinach until wilted
9. Season with salt and pepper
10. Serve over rice, topped with **toasted cashews**, fresh cilantro, and lime wedges

Cooking Time: 35 minutes
Servings: 4

**Chef's Notes:**
- The toasted spices create a deeper, more complex flavor base
- Fresh ginger and garlic bring aromatic warmth
- Bell peppers add sweetness and vibrant color
- Cashews provide delightful crunch contrast
- Lime juice enhances iron absorption from spinach
- This refined version offers restaurant-quality results at home!
"""
        steps.append({
            'agent': 'Chef',
            'role': 'Recipe Refiner',
            'input': 'Incorporating feedback',
            'output': final_response
        })
        
        return steps


if __name__ == "__main__":
    # Demo the mock collective
    print("🧑‍🍳 AI Chef Collective - Demo Mode\n")
    print("=" * 60)
    
    collective = MockAIChefCollective()
    pantry_items = ["chickpeas", "spinach", "coconut milk", "curry powder", "rice"]
    
    print(f"\nPantry Items: {', '.join(pantry_items)}\n")
    print("=" * 60)
    
    steps = collective.run_chef_show(pantry_items)
    
    for i, step in enumerate(steps, 1):
        print(f"\n{'='*60}")
        print(f"Step {i}: {step['agent']} - {step['role']}")
        print(f"{'='*60}")
        print(f"\nInput: {step['input']}\n")
        print("Response:")
        print(step['output'])
    
    print("\n" + "="*60)
    print("✨ Chef Show Complete!")
    print("="*60)
