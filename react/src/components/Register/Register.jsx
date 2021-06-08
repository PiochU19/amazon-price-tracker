import React from "react";
import "./Register.scss";
import { Link } from "react-router-dom";


const Register = () => {

    const handleSubmit = async e => {
        e.preventDefault();
    };

    return (
        <form className="Register" onSubmit={ handleSubmit }>
            <div className="Register__title">
                <h3>
                    Register
                </h3>
            </div>
            <div>
                <input className="Input" name="email" type="email" placeholder="email" />
            </div>
            <div>
                <input className="Input" name="first_name" type="text" placeholder="first name" />
            </div>
            <div>
                <input className="Input" name="last_name" type="text" placeholder="last name" />
            </div>
            <div>
                <input className="Input" name="password" type="password" placeholder="password" />
            </div>
            <div>
                <input className="Input" name="password_confirmation" type="password" placeholder="password confirmation" />
            </div>
            <div>
                <input className="Button" type="submit" value="register" />
            </div>
        </form>
    );
};

export default Register