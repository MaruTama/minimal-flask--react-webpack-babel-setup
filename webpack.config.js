const webpack = require('webpack');

module.exports = {
  entry: './src/jsx/index.js',
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  },
  output: {
    path: __dirname + '/src/python/server/static/js',
    publicPath: '/',
    filename: 'bundle.js'
  }
};
