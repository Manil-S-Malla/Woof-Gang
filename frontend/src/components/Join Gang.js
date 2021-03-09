import React, {Component} from 'react';

export default class JoinGang extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <h1> Hi {this.props.name}, This is the Join Gang Page. </h1>;
    }
}
