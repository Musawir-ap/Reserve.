/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.html',
    './**/*.js',
    './**/*.css',
  ],
  theme: {
    extend: {
      spacing: {
        '1': '0.25rem',
        '2': '0.5rem',
        '3': '0.75rem',
        '4': '1rem',
        '5': '1.25rem',
        '6': '1.5rem',
        '7': '1.75rem',
        '8': '2rem',
        '9': '2.25rem',
        '10': '2.5rem',

        '1/2': '50%',
        '1/3': '33.333333%',
        '2/3': '66.666667%',
        '1/4': '25%',
        '2/4': '50%',
        '3/4': '75%',
        '1/5': '20%',
        '2/5': '40%',
        '3/5': '60%',
        '4/5': '80%',
        '1/6': '16.666667%',
        '2/6': '33.333333%',
        '3/6': '50%',
        '4/6': '66.666667%',
        '5/6': '83.333333%',
        '1/7': '14.285714%',
        '2/7': '28.571429%',
        '3/7': '42.857143%',
        '4/7': '57.142857%',
        '5/7': '71.428571%',
        '6/7': '85.714286%',
        '1/8': '12.5%',
        '2/8': '25%',
        '3/8': '37.5%',
        '4/8': '50%',
        '5/8': '62.5%',
        '6/8': '75%',
        '7/8': '87.5%',
        '1/9': '11.111111%',
        '2/9': '22.222222%',
        '3/9': '33.333333%',
        '4/9': '44.444444%',
        '5/9': '55.555556%',
        '6/9': '66.666667%',
        '7/9': '77.777778%',
        '8/9': '88.888889%',
        '1/10': '10%',
        '1/11': '9.090909%',
        '1/12': '8.333333%',
        '1/13': '7.692308%',
        '1/14': '7.142857%',
        '1/15': '6.666667%',
        '1/16': '6.25%',
        '1/17': '5.882353%',
        '1/18': '5.555556%',
        '1/19': '5.263158%',
        '1/20': '5%',
      },
      colors:{
        booked: {
          bg: 'rgba(16, 132, 239, 0.15)',
          text: 'rgba(16, 132, 239, 1)',
        },
        pending: {
          bg: 'rgba(231, 231, 233, 1)',
          text: 'rgba(75, 79, 94, 1)',
        },
        rejected: {
          bg: 'rgba(240, 68, 56, 0.15)',
          text: 'rgba(240, 68, 56, 1)',
        },
        cancelled: {
          bg: 'rgba(240, 68, 56, 0.15)',
          text: 'rgba(240, 68, 56, 1)',
        },
        completed: {
          bg: 'rgba(39, 174, 96, 0.15)',
          text: 'rgba(39, 174, 96)',
        },
        paid: {
          bg: 'rgba(141, 16, 239, 0.15)',
          text: 'rgba(141, 16, 239)',
        },
      }
    },
    fontFamily: {
      // 'sans': ['ui-sans-serif', 'system-ui'],
      // 'serif': ['ui-serif', 'Georgia'],
      'mono': ['ui-monospace', 'SFMono-Regular'],
      'display': ['Gilroy'],
      'body': ['"Gilroy"'],
    },
    
  },
  plugins: [
    // require('@tailwindcss/forms'),
  ],
}

