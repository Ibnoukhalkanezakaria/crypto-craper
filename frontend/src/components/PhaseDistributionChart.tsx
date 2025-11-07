import { useQuery } from '@tanstack/react-query'
import { apiService } from '../services/api'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'react-chartjs-2'

ChartJS.register(ArcElement, Tooltip, Legend)

export default function PhaseDistributionChart() {
  const { data: distribution } = useQuery({
    queryKey: ['phase-distribution'],
    queryFn: apiService.getPhaseDistribution,
  })

  if (!distribution) return null

  // distribution is already an array from the API
  const distributionArray = Array.isArray(distribution) ? distribution : []

  const chartData = {
    labels: distributionArray.map((d) => d.phase.toUpperCase()),
    datasets: [
      {
        data: distributionArray.map((d) => d.count),
        backgroundColor: [
          'rgba(16, 185, 129, 0.8)',  // Green - Accumulation
          'rgba(59, 130, 246, 0.8)',   // Blue - Expansion
          'rgba(245, 158, 11, 0.8)',   // Yellow - Hype
          'rgba(239, 68, 68, 0.8)',    // Red - Crash
          'rgba(107, 114, 128, 0.8)',  // Gray - Unknown
        ],
        borderColor: [
          'rgba(16, 185, 129, 1)',
          'rgba(59, 130, 246, 1)',
          'rgba(245, 158, 11, 1)',
          'rgba(239, 68, 68, 1)',
          'rgba(107, 114, 128, 1)',
        ],
        borderWidth: 2,
      },
    ],
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'right' as const,
        labels: {
          color: 'rgb(156, 163, 175)',
          font: {
            size: 12,
          },
        },
      },
      tooltip: {
        callbacks: {
          label: (context: any) => {
            const label = context.label || ''
            const value = context.parsed || 0
            const total = context.dataset.data.reduce((a: number, b: number) => a + b, 0)
            const percentage = ((value / total) * 100).toFixed(1)
            return `${label}: ${value} (${percentage}%)`
          },
        },
      },
    },
  }

  return (
    <div className="card">
      <h2 className="text-2xl font-bold text-white mb-6">Market Phase Distribution</h2>
      <div className="h-80">
        <Pie data={chartData} options={options} />
      </div>
      <div className="mt-6 grid grid-cols-2 md:grid-cols-5 gap-4">
        {distributionArray.map((item) => (
          <div key={item.phase} className="text-center">
            <div className="text-2xl font-bold text-white">{item.count}</div>
            <div className="text-sm text-gray-400 capitalize">{item.phase}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
