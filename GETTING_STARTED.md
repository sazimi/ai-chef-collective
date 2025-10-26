# Getting Started with AI Chef Collective

## Quick Start Guide

### Prerequisites

Before you begin, ensure you have:

1. **Python 3.9+** installed on your system
2. **Node.js 18+** installed on your system
3. **Azure AI Foundry Account** with a project created
4. **Azure OpenAI deployment** (GPT-4 recommended)

### Azure AI Foundry Setup

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Create or select a project
3. Deploy a model (GPT-4 recommended for best results)
4. Navigate to **Settings → Project properties**
5. Copy your **connection string**

### Installation Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/sazimi/ai-chef-collective.git
cd ai-chef-collective
```

#### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Edit .env and add your credentials
# AZURE_AI_PROJECT_CONNECTION_STRING=your_connection_string_here
# AZURE_MODEL_DEPLOYMENT_NAME=gpt-4
```

#### 3. Frontend Setup

```bash
# Navigate to frontend (from root)
cd ../frontend

# Install dependencies
npm install
```

### Running the Application

#### Option 1: Run Both Servers (Recommended)

From the root directory:

```bash
./run-dev.sh
```

This will start:
- Backend at http://localhost:8000
- Frontend at http://localhost:3000

#### Option 2: Run Separately

**Terminal 1 - Backend:**
```bash
cd backend
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

#### Option 3: Demo Mode (No Azure Required)

To see how the application works without Azure credentials:

```bash
cd backend
python demo.py
```

### Using the Application

1. Open http://localhost:3000 in your browser
2. Enter pantry items or click suggestions
3. Click "🚀 Start AI Chef Show"
4. Watch the agents collaborate:
   - **Chef** creates initial recipe
   - **Nutritionist** analyzes nutritional content
   - **Critic** provides feedback
   - **Chef** refines the recipe

### API Documentation

Once the backend is running, visit:
- Interactive API docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

### Troubleshooting

#### "Configuration error" when running the app

Make sure your `.env` file exists and contains valid Azure credentials:
```env
AZURE_AI_PROJECT_CONNECTION_STRING=your_actual_connection_string
AZURE_MODEL_DEPLOYMENT_NAME=gpt-4
```

#### Frontend can't connect to backend

Ensure the backend is running on port 8000. Check for:
- Port conflicts (another app using port 8000)
- Firewall blocking local connections

#### Build errors in frontend

Try:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Production Deployment

#### Backend

1. Set environment variables in your hosting platform
2. Install dependencies: `pip install -r requirements.txt`
3. Run with production server: `uvicorn main:app --host 0.0.0.0 --port 8000`

#### Frontend

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. Serve the `dist` folder with a web server (nginx, Apache, etc.)
3. Configure the API proxy or update the API endpoint

### Learn More

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)

### Support

For issues or questions:
1. Check the [README.md](README.md) for detailed information
2. Review the code in `backend/demo.py` for implementation examples
3. Check Azure AI Foundry status and quotas

### Next Steps

- Customize agent prompts in `backend/agents.py`
- Modify the UI design in `frontend/src/components/`
- Add more agents to the pipeline
- Implement user authentication
- Add recipe history and favorites
