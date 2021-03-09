import React, {Component} from 'react';
import {render} from 'react-dom';
import Homepage from './Homepage';
import JoinGang from './Join Gang';
import CreateGang from './Create Gang';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        //return <h1> Hi {this.props.name} </h1>;
        return <Homepage name= {this.props.name} />
    }
}

const appDiv = document.getElementById("app");

render(<App name= "Manil" />, appDiv);            //  Put the 'App' component in the 'appDiv'.