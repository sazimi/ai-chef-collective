import { useState } from 'react'

interface PantryInputProps {
  onSubmit: (items: string[]) => void
  loading: boolean
}

export default function PantryInput({ onSubmit, loading }: PantryInputProps) {
  const [inputValue, setInputValue] = useState('')
  const [items, setItems] = useState<string[]>([])

  const handleAddItem = () => {
    const trimmed = inputValue.trim()
    if (trimmed && !items.includes(trimmed)) {
      setItems([...items, trimmed])
      setInputValue('')
    }
  }

  const handleRemoveItem = (index: number) => {
    setItems(items.filter((_, i) => i !== index))
  }

  const handleSubmit = () => {
    if (items.length > 0) {
      onSubmit(items)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleAddItem()
    }
  }

  const suggestedItems = [
    'chickpeas', 'spinach', 'coconut milk', 'curry powder', 'rice',
    'tomatoes', 'garlic', 'onions', 'bell peppers', 'quinoa',
    'black beans', 'avocado', 'lemon', 'tahini', 'sweet potato'
  ]

  return (
    <div className="glass rounded-2xl p-8 mb-8 animate-fade-in">
      <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
        <span>🥗</span> Your Pantry Items
      </h2>
      
      <div className="flex gap-3 mb-4">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Enter an ingredient..."
          className="flex-1 px-4 py-3 rounded-xl bg-white/10 border border-white/20 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-white/50"
          disabled={loading}
        />
        <button
          onClick={handleAddItem}
          disabled={!inputValue.trim() || loading}
          className="px-6 py-3 rounded-xl bg-white/20 hover:bg-white/30 text-white font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed border border-white/20"
        >
          Add
        </button>
      </div>

      {/* Suggested Items */}
      <div className="mb-4">
        <p className="text-white/70 text-sm mb-2">Suggestions:</p>
        <div className="flex flex-wrap gap-2">
          {suggestedItems.map((item) => (
            <button
              key={item}
              onClick={() => {
                if (!items.includes(item)) {
                  setItems([...items, item])
                }
              }}
              disabled={items.includes(item) || loading}
              className="px-3 py-1 rounded-lg bg-white/10 hover:bg-white/20 text-white/80 text-sm transition-all disabled:opacity-30 disabled:cursor-not-allowed border border-white/10"
            >
              {item}
            </button>
          ))}
        </div>
      </div>

      {/* Selected Items */}
      {items.length > 0 && (
        <div className="mb-4">
          <p className="text-white/70 text-sm mb-2">Selected Items:</p>
          <div className="flex flex-wrap gap-2">
            {items.map((item, index) => (
              <div
                key={index}
                className="px-4 py-2 rounded-xl bg-gradient-to-r from-purple-500/30 to-pink-500/30 text-white flex items-center gap-2 border border-white/20"
              >
                <span>{item}</span>
                <button
                  onClick={() => handleRemoveItem(index)}
                  disabled={loading}
                  className="text-white/70 hover:text-white transition-colors"
                >
                  ✕
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Submit Button */}
      <button
        onClick={handleSubmit}
        disabled={items.length === 0 || loading}
        className="w-full px-6 py-4 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-bold text-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl"
      >
        {loading ? 'Running Chef Show...' : '🚀 Start AI Chef Show'}
      </button>
    </div>
  )
}
