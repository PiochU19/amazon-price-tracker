import React from "react";
import "./App.scss";
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom";
import { Helmet } from "react-helmet";

import Navbar from "./components/Navbar/Navbar";
import Footer from "./components/Footer/Footer";

import Index from "./components/Index/Index";
import Login from "./components/Login/Login";
import Register from "./components/Register/Register";

import P404 from "./components/P404/P404";

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
                        <Route exact path="/" component={ Index } />
                        <Route exact path="/login" component={ Login } />
                        <Route exact path="/register" component={ Register } />
                        <Route exact path="/404" component={ P404 } />
                        <Redirect to="/404" />
                    </Switch>
                </div>
                <Footer />
            </div>
        </Router>
    );
};

export default App