/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'crypto-dark': '#0F172A',
        'crypto-darker': '#0B1120',
        'crypto-blue': '#3B82F6',
        'crypto-green': '#10B981',
        'crypto-red': '#EF4444',
        'crypto-yellow': '#F59E0B',
      },
    },
  },
  plugins: [],
}
