import React, {Component} from 'react';

export default class CreateGang extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <h1> Hi {this.props.name}, This is the Create Gang Page. </h1>;
    }
}
