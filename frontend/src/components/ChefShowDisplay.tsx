interface AgentStep {
  agent: string
  role: string
  input: string
  output: string
}

interface ChefShowDisplayProps {
  steps: AgentStep[]
  pantryItems: string[]
}

export default function ChefShowDisplay({ steps, pantryItems }: ChefShowDisplayProps) {
  const getAgentIcon = (agent: string) => {
    switch (agent) {
      case 'Chef':
        return '👨‍🍳'
      case 'Nutritionist':
        return '🥗'
      case 'Critic':
        return '⭐'
      default:
        return '🤖'
    }
  }

  const getAgentColor = (agent: string) => {
    switch (agent) {
      case 'Chef':
        return 'from-orange-500/30 to-red-500/30'
      case 'Nutritionist':
        return 'from-green-500/30 to-emerald-500/30'
      case 'Critic':
        return 'from-yellow-500/30 to-amber-500/30'
      default:
        return 'from-blue-500/30 to-purple-500/30'
    }
  }

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Recipe Summary Header */}
      <div className="glass rounded-2xl p-6 border-2 border-white/30">
        <h2 className="text-2xl font-bold text-white mb-3 flex items-center gap-2">
          <span>✨</span> Chef Show Complete!
        </h2>
        <p className="text-white/80 mb-3">
          Based on your pantry items: <strong>{pantryItems.join(', ')}</strong>
        </p>
        <p className="text-white/70 text-sm">
          Our AI agents collaborated through {steps.length} steps to create your perfect recipe
        </p>
      </div>

      {/* Agent Steps */}
      {steps.map((step, index) => (
        <div
          key={index}
          className="glass rounded-2xl p-6 hover:scale-[1.02] transition-transform duration-300"
          style={{ animationDelay: `${index * 100}ms` }}
        >
          {/* Agent Header */}
          <div className="flex items-start gap-4 mb-4">
            <div className={`text-5xl bg-gradient-to-br ${getAgentColor(step.agent)} rounded-2xl p-3 border border-white/20`}>
              {getAgentIcon(step.agent)}
            </div>
            <div className="flex-1">
              <div className="flex items-center gap-3 mb-1">
                <h3 className="text-2xl font-bold text-white">{step.agent}</h3>
                <span className="px-3 py-1 rounded-full bg-white/10 text-white/70 text-sm border border-white/20">
                  Step {index + 1}
                </span>
              </div>
              <p className="text-white/70 text-lg">{step.role}</p>
            </div>
          </div>

          {/* Input */}
          <div className="mb-4 p-4 rounded-xl bg-white/5 border border-white/10">
            <p className="text-white/60 text-sm font-semibold mb-1">Input:</p>
            <p className="text-white/80">{step.input}</p>
          </div>

          {/* Output */}
          <div className="p-4 rounded-xl bg-gradient-to-br from-white/10 to-white/5 border border-white/20">
            <p className="text-white/60 text-sm font-semibold mb-2">Response:</p>
            <div className="text-white/90 whitespace-pre-wrap leading-relaxed">
              {step.output}
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}
