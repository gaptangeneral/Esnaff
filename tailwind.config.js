// tailwind.config.js
const withMT = require("@material-tailwind/react/utils/withMT");

/** @type {import('tailwindcss').Config} */
module.exports = withMT({
  content: [
    "./node_modules/@material-tailwind/react/components/**/*.{js,ts,jsx,tsx}",
    "./node_modules/@material-tailwind/react/theme/components/**/*.{js,ts,jsx,tsx}",
    './employee/templates/**/*.html',
    './finance/templates/**/*.html',
    './static/src/**/*.js', // Eğer JavaScript dosyalarınız varsa
  ],
  theme: {
    extend: {},
  },
  plugins: [],
});
