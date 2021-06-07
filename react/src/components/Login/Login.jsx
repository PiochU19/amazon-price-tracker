import React from "react";
import "./Login.scss";


const Login = () => {
    return (
        <form className="Login">
            <div className="Login__title">
                <p>
                    Login
                </p>
            </div>
            <div className="Login__email">
                <input type="text" name="email" placeholder="email" />
            </div>
            <div className="Login__password">
                <input type="password" name="password" placeholder="password" />
            </div>
            <div className="Login__footer">
                <p>
                    No account? Sign up here
                </p>
            </div>
        </form>
    );
};

export default Login