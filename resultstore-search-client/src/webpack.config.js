const webpack = require('webpack');

module.exports = {
  // ... your webpack configuration ...
  plugins: [
    new webpack.ContextReplacementPlugin(
      /\/package-name\//,
      (data) => {
        delete data.dependencies[0].critical;
        return data;
      },
    ),
  ]
}