# 🧑‍🍳 AI Chef Collective

Multi-agent demo using **Microsoft Agent Framework** and **Azure AI Foundry**: Chef, Nutritionist, and Critic agents collaborate in sequence to turn your pantry items into a refined, healthy vegan recipe.

## 🌟 Features

- **Multi-Agent Pipeline**: Chef → Nutritionist → Critic → Chef (refined)
- **Microsoft Agent Framework**: Leverages Azure AI Foundry's agent capabilities
- **Modern Stack**: Python FastAPI backend + React TypeScript frontend
- **Beautiful UI**: Futuristic design with glass morphism and gradients
- **Real-time Collaboration**: Watch agents work together step-by-step

## 🏗️ Architecture

### Backend (Python + FastAPI)
- **FastAPI**: High-performance async API framework
- **Microsoft Agent Framework**: Multi-agent orchestration via Azure AI Foundry
- **Environment Variables**: Secure configuration with python-dotenv
- **Agent Pipeline**:
  1. **Chef Agent**: Creates initial vegan recipe from pantry items
  2. **Nutritionist Agent**: Analyzes nutritional content and suggests improvements
  3. **Critic Agent**: Provides constructive feedback on flavor and technique
  4. **Chef Agent**: Refines recipe based on feedback

### Frontend (React + TypeScript + Tailwind)
- **React 18**: Modern component-based UI
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling with custom glass effects
- **Vite**: Lightning-fast build tool
- **Responsive Design**: Works on desktop and mobile

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Azure AI Foundry account with project setup
- Azure OpenAI deployment (GPT-4 recommended)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

4. Configure your Azure AI Foundry credentials in `.env`:
```env
AZURE_AI_PROJECT_CONNECTION_STRING=your_connection_string_here
AZURE_MODEL_DEPLOYMENT_NAME=gpt-4
```

5. Run the backend server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📡 API Endpoints

### `POST /api/runChefShow`

Runs the complete multi-agent pipeline.

**Request Body:**
```json
{
  "pantry_items": ["chickpeas", "spinach", "coconut milk", "curry powder", "rice"]
}
```

**Response:**
```json
{
  "success": true,
  "steps": [
    {
      "agent": "Chef",
      "role": "Recipe Creator",
      "input": "Pantry items: chickpeas, spinach, coconut milk, curry powder, rice",
      "output": "Recipe details..."
    },
    // ... more steps
  ],
  "message": "Chef show completed successfully!"
}
```

### `GET /health`

Health check endpoint.

## 🎨 UI Features

- **Glass Morphism**: Modern frosted glass effect on cards
- **Gradient Backgrounds**: Beautiful purple-to-pink gradients
- **Animated Steps**: Smooth fade-in animations for each agent step
- **Responsive Layout**: Adapts to all screen sizes
- **Agent Icons**: Visual representation of each agent (👨‍🍳, 🥗, ⭐)
- **Color-Coded Cards**: Different gradients for each agent type

## 🔧 Tech Stack

### Backend
- FastAPI 0.104+
- Azure AI Projects SDK
- Azure Identity
- Python-dotenv
- Pydantic
- Uvicorn

### Frontend
- React 18
- TypeScript 5
- Tailwind CSS 3
- Vite 5
- Axios

## 📝 Environment Variables

Create a `.env` file in the `backend` directory:

```env
# Azure AI Foundry Configuration
AZURE_AI_PROJECT_CONNECTION_STRING=your_connection_string_here
AZURE_MODEL_DEPLOYMENT_NAME=gpt-4
```

**Getting Your Connection String:**
1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Select your project
3. Navigate to Settings → Project properties
4. Copy the connection string

## 🧪 Development

### Backend Development
```bash
cd backend
python main.py
# API available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Frontend Development
```bash
cd frontend
npm run dev
# App available at http://localhost:3000
```

### Building for Production

**Frontend:**
```bash
cd frontend
npm run build
```

The built files will be in `frontend/dist`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Microsoft Agent Framework**: For powerful multi-agent orchestration
- **Azure AI Foundry**: For enterprise-grade AI infrastructure
- Built with ❤️ for the AI community
