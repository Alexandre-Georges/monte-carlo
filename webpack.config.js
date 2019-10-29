const path = require('path');

module.exports = {
  mode: 'development',
  entry: './js/index.js',
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'static')
  },
  resolve: {
    alias: {
      svelte: path.resolve('node_modules', 'svelte')
    },
    extensions: ['.mjs', '.js', '.svelte'],
    mainFields: ['svelte', 'browser', 'module', 'main']
  },
  module: {
    rules: [
      {
        test: /\.(html|svelte)$/,
        exclude: /node_modules/,
        use: 'svelte-loader',
      },
    ],
  },
};