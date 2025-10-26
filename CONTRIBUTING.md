# Contributing to AI Chef Collective

Thank you for your interest in contributing to AI Chef Collective! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project welcomes contributions and suggestions. Be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

If you find a bug:

1. Check if it's already reported in Issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python/Node version)

### Suggesting Features

For feature requests:

1. Check existing issues for similar suggestions
2. Create a new issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Any alternatives considered

### Contributing Code

#### Setup Development Environment

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/ai-chef-collective.git
cd ai-chef-collective
```

3. Set up backend:
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Configure your .env file
```

4. Set up frontend:
```bash
cd ../frontend
npm install
```

#### Making Changes

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following our coding standards:

**Python (Backend):**
- Follow PEP 8 style guide
- Use type hints where applicable
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

**TypeScript/React (Frontend):**
- Use functional components with hooks
- Follow existing component structure
- Use TypeScript types/interfaces
- Keep components small and reusable

3. Test your changes:

**Backend:**
```bash
cd backend
python -m pytest  # If tests exist
python demo.py    # Run demo to verify functionality
```

**Frontend:**
```bash
cd frontend
npm run build     # Ensure it builds
npm run lint      # Check for linting errors
```

4. Commit your changes:
```bash
git add .
git commit -m "Description of your changes"
```

5. Push to your fork:
```bash
git push origin feature/your-feature-name
```

6. Create a Pull Request

### Pull Request Guidelines

- **Title**: Clear, concise description of changes
- **Description**: Explain what, why, and how
- **Link Issues**: Reference related issues
- **Screenshots**: Include for UI changes
- **Testing**: Describe how you tested

## Project Structure

```
ai-chef-collective/
├── backend/
│   ├── agents.py       # Multi-agent system logic
│   ├── main.py         # FastAPI application
│   ├── demo.py         # Demo without Azure
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/ # React components
│   │   ├── App.tsx     # Main app component
│   │   └── main.tsx    # Entry point
│   └── package.json
└── README.md
```

## Development Tips

### Backend Development

- Use `uvicorn main:app --reload` for auto-reload during development
- Check API docs at http://localhost:8000/docs
- Use the demo.py as reference for agent behavior

### Frontend Development

- Use `npm run dev` for hot-reload
- Components are in `src/components/`
- Tailwind classes are available for styling

### Adding New Agents

To add a new agent to the pipeline:

1. Update `backend/agents.py`:
   - Add agent creation in `initialize_agents()`
   - Update pipeline in `run_chef_show()`

2. Update `frontend/src/components/ChefShowDisplay.tsx`:
   - Add agent icon in `getAgentIcon()`
   - Add agent color in `getAgentColor()`

## Questions?

Feel free to:
- Open an issue for questions
- Check existing documentation
- Review demo.py for examples

Thank you for contributing! 🎉
