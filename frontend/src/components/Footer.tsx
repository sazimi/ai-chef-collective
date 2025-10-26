export default function Footer() {
  return (
    <footer className="glass border-t border-white/20 mt-12 py-6">
      <div className="container mx-auto max-w-6xl px-4">
        <div className="text-center space-y-2">
          <p className="text-white/80 text-sm">
            Built with{' '}
            <strong className="text-white">Microsoft Agent Framework</strong>
            {' '}+{' '}
            <strong className="text-white">Azure AI Foundry</strong>
          </p>
          <p className="text-white/60 text-xs">
            Multi-agent collaborative AI demo showcasing Chef → Nutritionist → Critic → Chef pipeline
          </p>
          <div className="flex justify-center gap-4 mt-3 text-xs text-white/50">
            <span>🐍 Python FastAPI</span>
            <span>⚛️ React + TypeScript</span>
            <span>🎨 Tailwind CSS</span>
          </div>
        </div>
      </div>
    </footer>
  )
}
