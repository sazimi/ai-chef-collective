# AI Chef Collective - Backend

FastAPI backend for the AI Chef Collective multi-agent demo.

## Features

- **Microsoft Agent Framework**: Integration with Azure AI Foundry
- **Multi-Agent Pipeline**: Chef → Nutritionist → Critic → Chef
- **FastAPI**: Modern, fast, async API framework
- **Environment Configuration**: Secure credential management with dotenv

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```env
AZURE_AI_PROJECT_CONNECTION_STRING=your_connection_string_here
AZURE_MODEL_DEPLOYMENT_NAME=gpt-4
```

3. Run the server:
```bash
python main.py
```

## API Documentation

Once running, visit:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Agents

### Chef Agent
Creates and refines vegan recipes from pantry items. Specializes in creative, flavorful plant-based cooking.

### Nutritionist Agent
Analyzes nutritional content and provides health-focused recommendations while maintaining taste.

### Critic Agent
Professional food critic providing constructive feedback on flavor balance, technique, and presentation.

## Environment Variables

- `AZURE_AI_PROJECT_CONNECTION_STRING`: Your Azure AI Foundry project connection string
- `AZURE_MODEL_DEPLOYMENT_NAME`: Model deployment name (default: gpt-4)
