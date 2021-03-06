const path = require('path'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin'),
    BrowserSyncPlugin = require('browser-sync-webpack-plugin'),
    CSSNanoPlugin = require('cssnano-webpack-plugin'),
    TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        index: ['@js_modules/index.js', '@js_modules/header.js', '@js_modules/messages.js'],
        news: ['@js_modules/news.js', '@js_modules/header.js'],
        delivery_order: ['@js_modules/header.js', '@js_modules/order-delivery.js'],
        news_single: ['@js_modules/header.js', '@js_modules/news-single.js', '@js_modules/messages.js'],
        vehisles: ['@js_modules/vehisles.js', '@js_modules/header.js'],
        vehisle_single: '@js_modules/header.js',
        login: '@js_modules/header.js',
        control_panel: ['@js_modules/header.js', '@js_modules/control-panel.js'],
        create_news: '@js_modules/header.js',
        model_info: '@js_modules/header.js',
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
            proxy: 'http://localhost:8000',
        },
        {
            injectCss: true
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
};