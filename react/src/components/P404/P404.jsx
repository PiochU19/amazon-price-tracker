import React from "react";
import "./P404.scss";
import { Link } from "react-router-dom";


const P404 = () => {
    return (
        <div className="P404">
            <div className="P404__title">
                <h1>Sorry, We couldn't find given path :(</h1>
            </div>
            <div className="P404__link">
                <Link to="/">Get back on the right track</Link>
            </div>
        </div>
    );
};

export default P404