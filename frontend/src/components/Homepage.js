import React, {Component} from 'react';
import JoinGang from './Join Gang';
import CreateGang from './Create Gang';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect
} from "react-router-dom"

export default class Homepage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <Router>
            <Switch>
                <Route exact path= '/'><h1> Hi {this.props.name}, This is the Homepage. </h1></Route>
                <Route exact path= '/join' component= {JoinGang} />
                <Route exact path= '/create' component= {CreateGang} />
            </Switch>
        </Router>
    }
}
