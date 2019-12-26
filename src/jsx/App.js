import React from 'react';
import axios from 'axios';

class App extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      a  : 3,
      b  : 1,
      num: null,
    };

    // サーバーにリクエスト
    axios.get('/add',{
      params: {
        'a': this.state.a,
        'b': this.state.b
      }
    })
    .then((response) => {
      // 成功時の処理
      this.setState({ ...this.state, num: response.data });
      console.log(response.data);
    })
    .catch((error) => {
      // 失敗時の処理
      console.error(error);
    });
  }

  render() {
    const { title } = this.props;
    console.log(title);
    return (
      <div>
        <div>{title}</div>
        <div>{this.state.a}+{this.state.b}={this.state.num}</div>
      </div>
    );
  }
}

export default App;
