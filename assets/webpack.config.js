const path = require('path'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin'),
    BrowserSyncPlugin = require('browser-sync-webpack-plugin'),
    CSSNanoPlugin = require('cssnano-webpack-plugin'),
    TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        index: ['@js_modules/index.js', '@js_modules/header.js'],
        news: ['@js_modules/news.js', '@js_modules/header.js'],
        vehisles: ['@js_modules/vehisles.js', '@js_modules/header.js'],
        styles: '@styles/styles.scss',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, '../static')
    },
    resolve: {
        alias: {
            '@js_modules': path.resolve(__dirname, 'js_modules'),
            '@styles': path.resolve(__dirname, 'styles')
        }
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: { sourceMap: true }
                    }, {
                        loader: 'sass-loader',
                        options: { sourceMap: true }
                    }
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'styles.css'
        }),
        new BrowserSyncPlugin({
            host: 'localhost',
            port: 3000,
            proxy: 'http://localhost:8000'
        })
    ],
    optimization: {
        minimizer: [
            new TerserPlugin(),
            new CSSNanoPlugin({
                cssProcessorOptions: {
                    "preset": "advanced",
                    "safe": true,
                    "map": { "inline": false },
                },
            })
        ]
    }
}