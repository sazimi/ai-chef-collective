"""
AI Chef Collective - Multi-Agent Demo
Using Microsoft Agent Framework + Azure AI Foundry
"""
import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import Agent, AgentThread, ThreadMessage, MessageRole
from azure.identity import DefaultAzureCredential

# Load environment variables
load_dotenv()


class AIChefCollective:
    """Multi-agent system for recipe creation and refinement"""
    
    def __init__(self):
        """Initialize the AI Chef Collective with Azure AI Foundry"""
        connection_string = os.getenv("AZURE_AI_PROJECT_CONNECTION_STRING")
        if not connection_string:
            raise ValueError("AZURE_AI_PROJECT_CONNECTION_STRING environment variable is required")
        
        # Initialize Azure AI Project Client with Microsoft Agent Framework
        self.client = AIProjectClient.from_connection_string(
            conn_str=connection_string,
            credential=DefaultAzureCredential()
        )
        
        self.model_deployment = os.getenv("AZURE_MODEL_DEPLOYMENT_NAME", "gpt-4")
        self.agents = {}
        self.thread = None
        
    def initialize_agents(self):
        """Create the three specialized agents using Microsoft Agent Framework"""
        
        # Chef Agent - Creates initial recipes
        self.agents['chef'] = self.client.agents.create_agent(
            model=self.model_deployment,
            name="Chef Agent",
            instructions="""You are an expert vegan chef specializing in creative, 
            delicious plant-based recipes. When given pantry items, create a complete 
            recipe with ingredients, instructions, and cooking time. Be creative and 
            focus on flavor, texture, and presentation. Keep recipes practical and 
            achievable for home cooks."""
        )
        
        # Nutritionist Agent - Analyzes nutritional content
        self.agents['nutritionist'] = self.client.agents.create_agent(
            model=self.model_deployment,
            name="Nutritionist Agent",
            instructions="""You are a certified nutritionist specializing in plant-based 
            diets. Analyze recipes for nutritional content, providing estimated calories, 
            protein, carbs, fats, and key vitamins/minerals. Suggest improvements for 
            better nutritional balance while maintaining taste. Be specific with 
            portions and health benefits."""
        )
        
        # Critic Agent - Provides constructive feedback
        self.agents['critic'] = self.client.agents.create_agent(
            model=self.model_deployment,
            name="Critic Agent",
            instructions="""You are a professional food critic with expertise in 
            vegan cuisine. Evaluate recipes for flavor balance, technique, creativity, 
            and presentation. Provide constructive feedback on what works well and 
            what could be improved. Be encouraging but honest. Suggest specific 
            refinements to elevate the dish."""
        )
        
    def create_thread(self):
        """Create a conversation thread for the agents"""
        self.thread = self.client.agents.create_thread()
        
    def run_agent(self, agent_name: str, message: str) -> str:
        """Run a specific agent and get its response"""
        if agent_name not in self.agents:
            raise ValueError(f"Unknown agent: {agent_name}")
        
        # Add user message to thread
        self.client.agents.create_message(
            thread_id=self.thread.id,
            role=MessageRole.USER,
            content=message
        )
        
        # Run the agent
        run = self.client.agents.create_and_process_run(
            thread_id=self.thread.id,
            assistant_id=self.agents[agent_name].id
        )
        
        # Get the response
        messages = self.client.agents.list_messages(thread_id=self.thread.id)
        
        # Return the latest assistant message
        for msg in messages:
            if msg.role == MessageRole.ASSISTANT:
                return msg.content[0].text.value
        
        return "No response received"
    
    def run_chef_show(self, pantry_items: List[str]) -> List[Dict[str, Any]]:
        """
        Run the complete chef show pipeline:
        Chef → Nutritionist → Critic → Chef (refined)
        """
        steps = []
        
        # Initialize agents and thread
        self.initialize_agents()
        self.create_thread()
        
        # Step 1: Chef creates initial recipe
        chef_prompt = f"Create a delicious vegan recipe using these pantry items: {', '.join(pantry_items)}. Include ingredients, instructions, and cooking time."
        chef_response = self.run_agent('chef', chef_prompt)
        steps.append({
            'agent': 'Chef',
            'role': 'Recipe Creator',
            'input': f"Pantry items: {', '.join(pantry_items)}",
            'output': chef_response
        })
        
        # Step 2: Nutritionist analyzes the recipe
        nutrition_prompt = f"Analyze the nutritional content of this recipe and suggest improvements:\n\n{chef_response}"
        nutrition_response = self.run_agent('nutritionist', nutrition_prompt)
        steps.append({
            'agent': 'Nutritionist',
            'role': 'Nutrition Analyst',
            'input': 'Analyzing recipe nutritional content',
            'output': nutrition_response
        })
        
        # Step 3: Critic provides feedback
        critic_prompt = f"Review this recipe and its nutritional analysis. Provide constructive feedback:\n\nRecipe:\n{chef_response}\n\nNutrition:\n{nutrition_response}"
        critic_response = self.run_agent('critic', critic_prompt)
        steps.append({
            'agent': 'Critic',
            'role': 'Food Critic',
            'input': 'Reviewing recipe and nutrition',
            'output': critic_response
        })
        
        # Step 4: Chef refines based on feedback
        refine_prompt = f"Based on the nutritionist's analysis and critic's feedback, refine your recipe:\n\nOriginal Recipe:\n{chef_response}\n\nNutrition Feedback:\n{nutrition_response}\n\nCritic Feedback:\n{critic_response}"
        final_response = self.run_agent('chef', refine_prompt)
        steps.append({
            'agent': 'Chef',
            'role': 'Recipe Refiner',
            'input': 'Incorporating feedback',
            'output': final_response
        })
        
        return steps
    
    def cleanup(self):
        """Clean up agents and thread"""
        if self.thread:
            self.client.agents.delete_thread(self.thread.id)
        for agent in self.agents.values():
            self.client.agents.delete_agent(agent.id)
