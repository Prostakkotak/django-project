const path = require('path'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin'),
    BrowserSyncPlugin = require('browser-sync-webpack-plugin'),
    CSSNanoPlugin = require('cssnano-webpack-plugin'),
    TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    mode: 'production',
    entry: {
        index: '@js_modules/index-scripts.js',
        defaultHeader: '@js_modules/header-script.js'
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, '../static')
    },
    resolve: {
        extensions: ['.js', '.scss', '.css'],
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
            new CSSNanoPlugin(),
            new TerserPlugin()
        ]
    }
}