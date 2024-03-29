module.exports = {
	entry: 'assets/js/index.js',
	output: {
		filename: 'bundle.js'
	},
	module: {
			loaders: [
			{
				test: /\.js$/,
				loader: 'babel-loader',
				query: {
					presets: ['es2015', 'react']
				}
			}
			]
		}
};
