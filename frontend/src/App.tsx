import { useState } from 'react'
import axios from 'axios'
import ChefShowDisplay from './components/ChefShowDisplay'
import PantryInput from './components/PantryInput'
import Footer from './components/Footer'

interface AgentStep {
  agent: string
  role: string
  input: string
  output: string
}

function App() {
  const [pantryItems, setPantryItems] = useState<string[]>([])
  const [steps, setSteps] = useState<AgentStep[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleRunChefShow = async (items: string[]) => {
    setLoading(true)
    setError(null)
    setSteps([])
    setPantryItems(items)

    try {
      const response = await axios.post('/api/runChefShow', {
        pantry_items: items
      })

      if (response.data.success) {
        setSteps(response.data.steps)
      } else {
        setError(response.data.message || 'An error occurred')
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to connect to the server')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="glass border-b border-white/20 p-6 mb-8">
        <div className="container mx-auto max-w-6xl">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-2 text-center">
            🧑‍🍳 AI Chef Collective
          </h1>
          <p className="text-white/80 text-center text-lg">
            Multi-Agent Demo using Microsoft Agent Framework + Azure AI Foundry
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto max-w-6xl px-4 pb-8 flex-grow">
        {/* Pantry Input */}
        <PantryInput onSubmit={handleRunChefShow} loading={loading} />

        {/* Error Display */}
        {error && (
          <div className="glass-dark border-red-500/50 rounded-2xl p-6 mb-8 animate-fade-in">
            <div className="flex items-start gap-3">
              <span className="text-2xl">⚠️</span>
              <div>
                <h3 className="text-red-400 font-semibold text-lg mb-1">Error</h3>
                <p className="text-white/80">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="glass rounded-2xl p-12 text-center animate-pulse-glow">
            <div className="text-6xl mb-4">👨‍🍳</div>
            <h3 className="text-2xl font-semibold text-white mb-2">
              The AI Chef Collective is working...
            </h3>
            <p className="text-white/70">
              Our agents are collaborating to create your perfect recipe
            </p>
            <div className="mt-6 flex justify-center gap-2">
              <div className="w-3 h-3 bg-white/80 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
              <div className="w-3 h-3 bg-white/80 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
              <div className="w-3 h-3 bg-white/80 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
            </div>
          </div>
        )}

        {/* Chef Show Display */}
        {!loading && steps.length > 0 && (
          <ChefShowDisplay steps={steps} pantryItems={pantryItems} />
        )}
      </main>

      {/* Footer */}
      <Footer />
    </div>
  )
}

export default App
