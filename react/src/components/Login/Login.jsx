import React, { useEffect, useState } from "react";
import "./Login.scss";
import cookie from "react-cookies";
import { Link, useHistory, useLocation } from "react-router-dom";

import Loader from "./../Loader/Loader";

import axiosInstance from "./../../axios";


const Login = () => {

    const initialFormData = Object.freeze({
        email: '',
        password: '',
    });

    const history = useHistory();
    const location = useLocation();
    const [isReady, setIsReady] = useState(false); // is not authenticated
    const [formData, updateFormData] = useState(initialFormData);
    const [message, setMessage] = useState("login");

    useEffect(() => {
        if (cookie.load("Logged")) { // checking if cookie exist
            history.push('/');
        } else {
            setIsReady(true);
        }
    }, []);

    const handleChange = e => {
        updateFormData({
            ...formData,
            [e.target.id]: e.target.value.trim(),
        });
    };

    const handleSubmit = async e => {
        e.preventDefault();

        axiosInstance
            .post("account/login/", {
                email: formData.email,
                password: formData.password
            }, {
                headers: {
                    "X-CSRFToken": cookie.load("csrftoken")
                }
            })
            .then(res => {
                cookie.save("Logged", true);
                history.push("/");
            })
            .catch(error => {
                setMessage("something went wrong");
            });
    };

    return (
        <>
            {isReady
                ?
                <form className="Login" onSubmit={handleSubmit} spellCheck="false">
                    <div className="Login__title">
                        <h3>
                            {message}
                        </h3>
                    </div>
                    <div className="Login__email">
                        <input
                            className="Input"
                            type="text" name="email"
                            placeholder="email"
                            id="email"
                            onChange={handleChange}
                        />
                    </div>
                    <div className="Login__password">
                        <input
                            className="Input"
                            type="password"
                            placeholder="password"
                            id="password"
                            onChange={handleChange}
                        />
                    </div>
                    <div className="Login__footer">
                        <h6>
                            No account? <Link to="/register">Register here</Link>
                        </h6>
                    </div>
                    <div className="Login__submit">
                        <input
                            className="Button"
                            type="submit"
                            value="login"
                        />
                    </div>
                </form >
                :
                <Loader />
            }
        </>
    );
};

export default Login