module.exports = {
  plugins: {
    'autoprefixer': { browsers: ['last 2 versions', 'iOS >= 8'] },
    'postcss-nesting': {},
    'postcss-preset-env': { stage: 1 }
  }
}