# AI Chef Collective - Frontend

React + TypeScript + Tailwind CSS frontend for the AI Chef Collective.

## Features

- **Modern UI**: Glass morphism with gradient backgrounds
- **Responsive Design**: Works on all devices
- **Real-time Updates**: Watch agents collaborate step-by-step
- **Interactive Input**: Easy pantry item management
- **Beautiful Animations**: Smooth transitions and effects

## Setup

1. Install dependencies:
```bash
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

## Tech Stack

- React 18
- TypeScript 5
- Tailwind CSS 3
- Vite 5
- Axios

## Development

The frontend expects the backend to be running on `http://localhost:8000`. The Vite dev server proxies `/api` requests to the backend.

## Environment

No environment variables needed for local development. The API proxy is configured in `vite.config.ts`.
