import React from "react";
import "./App.scss";
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom";
import { Helmet } from "react-helmet";

import Navbar from "./components/Navbar/Navbar.jsx";
import Footer from "./components/Footer/Footer.jsx";

import Login from "./components/Login/Login.jsx";

const App = () => {
    return (
        <Router>
            <div className="App">
                <Helmet>
                    <meta name="author" content="Dominik Pioś" />

                    <title>Payless</title>
                </Helmet>
                <Navbar />
                <div className="Main">
                    <Switch>
                        <Route exact path="/login" component={ Login } />
                    </Switch>
                </div>
                <Footer />
            </div>
        </Router>
    );
};

export default App