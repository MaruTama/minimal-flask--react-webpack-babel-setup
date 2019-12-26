# minimal-flask + react-webpack-babel-setup
自分で使う用のテンプレート。  
サーバーサイドは flask, フロントサイドが React の開発ができる。

## Features

* Flask 1.0.2
* React 16
* Webpack 4
* Babel 7

## Installation

```
$ git clone git@github.com:MaruTama/minimal-flask--react-webpack-babel-setup.git
$ cd minimal-flask--react-webpack-babel-setup
$ npm install
$ npm run start:react

# 別コンソールにて開く
$ pyenv global 3.7.2 2.7.14
$ pip install -r requirements.txt
$ npm run start:flask

Goto http://localhost:3000
```


Flask は以下のようにファイルを配置する必要がある
```
/myproject  
  ├─ server.py  
  ├─ templates  
  │    └── index.html
  └─ static
       ├── css
       │    └── style.css
       └── js
            └── bundle.js
```

## 不明なエラー
```
VM3930 index.js:14 Uncaught TypeError: Cannot read property 'accept' of undefined
    at Module.eval (VM3930 index.js:14)
    at eval (VM3930 index.js:15)
    at Module../src/jsx/index.js (VM3929 bundle.js:584)
    at __webpack_require__ (VM3929 bundle.js:20)
    at VM3929 bundle.js:84
    at VM3929 bundle.js:87
```
