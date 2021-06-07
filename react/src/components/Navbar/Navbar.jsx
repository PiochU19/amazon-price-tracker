import React from "react";
import "./Navbar.scss";
import { Link } from "react-router-dom";
import { ReactComponent as ChartSVG } from "./../../assets/svgs/chart.svg";


const Navbar = () => {
    return (
        <navbar className="Navbar">
            <div className="Navbar__logo">
                <Link to="/">
                    <ChartSVG className="Navbar__logo-chartsvg" />
                </Link>
            </div>
            <div className="Navbar__title">
                <h4>
                    Payless - Price Tracker
                </h4>
            </div>
        </navbar>
    );
};

export default Navbar