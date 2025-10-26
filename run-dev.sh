#!/bin/bash

# Start both backend and frontend servers
echo "🚀 Starting AI Chef Collective..."
echo ""

# Check if running in development
if [ ! -f "backend/.env" ]; then
    echo "⚠️  Warning: backend/.env not found. Copy backend/.env.example to backend/.env and configure it."
    echo ""
fi

# Start backend
echo "Starting backend server..."
cd backend
python main.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Start frontend
echo "Starting frontend server..."
cd ../frontend
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ Servers started!"
echo "   - Backend: http://localhost:8000"
echo "   - Frontend: http://localhost:3000"
echo "   - API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
