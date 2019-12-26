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
- [【Trainer's Recipe】Pythonのフレームワークのflaskを触ってみた。](https://qiita.com/gsacademy_tokyo/items/16cba215a0cd921df87f)
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
