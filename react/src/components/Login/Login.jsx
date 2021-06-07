import React from "react";
import "./Login.scss";
import { Link } from "react-router-dom";


const Login = () => {

    const handleSubmit = async e => {
        e.preventDefault();
        console.log("Submited");
    };

    return (
        <form className="Login" onSubmit={ handleSubmit } spellCheck="false">
            <div className="Login__title">
                <h3>
                    Login
                </h3>
            </div>
            <div className="Login__email">
                <input className="Login__input" type="text" name="email" placeholder="email" />
            </div>
            <div className="Login__password">
                <input className="Login__input" type="password" name="password" placeholder="password" />
            </div>
            <div className="Login__footer">
                <h6>
                    No account? <Link to="/register">Register here</Link>
                </h6>
            </div>
            <div className="Login__submit">
                <input className="Login__submit-button" type="submit" value="login" />
            </div>
        </form >
    );
};

export default Login