const path = require('path');
const process = require('process');
const { VueLoaderPlugin } = require('vue-loader')
const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')

module.exports = {
  entry: "./app/assets/js",
  mode: process.env.NODE_ENV,
  output: {
    path: path.resolve(__dirname, "app/static"),
    filename: "bundle.js"
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
    }
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: ['to-string-loader', 'css-loader'],
      },
      {
        test: /\.styl$/,
        loader: ['style-loader', 'css-loader', 'stylus-loader']
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new VuetifyLoaderPlugin()
  ]
}
