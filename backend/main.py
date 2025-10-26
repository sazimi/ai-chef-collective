"""
FastAPI Backend for AI Chef Collective
Multi-agent demo using Microsoft Agent Framework + Azure AI Foundry
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import logging

from agents import AIChefCollective

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Chef Collective",
    description="Multi-agent demo using Microsoft Agent Framework + Azure AI Foundry",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChefShowRequest(BaseModel):
    """Request model for the chef show"""
    pantry_items: List[str]
    
    class Config:
        json_schema_extra = {
            "example": {
                "pantry_items": ["chickpeas", "spinach", "coconut milk", "curry powder", "rice"]
            }
        }


class ChefShowResponse(BaseModel):
    """Response model for the chef show"""
    success: bool
    steps: List[dict]
    message: str = ""


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "AI Chef Collective",
        "description": "Multi-agent demo using Microsoft Agent Framework + Azure AI Foundry",
        "version": "1.0.0",
        "endpoints": {
            "/api/runChefShow": "POST - Run the multi-agent chef show pipeline"
        }
    }


@app.post("/api/runChefShow", response_model=ChefShowResponse)
async def run_chef_show(request: ChefShowRequest):
    """
    Run the AI Chef Show multi-agent pipeline
    
    Pipeline: Chef → Nutritionist → Critic → Chef (refined)
    
    - **pantry_items**: List of ingredients available in the pantry
    
    Returns the complete conversation flow with all agent responses
    """
    try:
        if not request.pantry_items:
            raise HTTPException(status_code=400, detail="Pantry items cannot be empty")
        
        logger.info(f"Starting chef show with items: {request.pantry_items}")
        
        # Initialize the AI Chef Collective
        collective = AIChefCollective()
        
        # Run the multi-agent pipeline
        steps = collective.run_chef_show(request.pantry_items)
        
        # Cleanup
        collective.cleanup()
        
        logger.info("Chef show completed successfully")
        
        return ChefShowResponse(
            success=True,
            steps=steps,
            message="Chef show completed successfully!"
        )
        
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Configuration error: {str(e)}. Please check your environment variables."
        )
    except Exception as e:
        logger.error(f"Error running chef show: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI Chef Collective"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
