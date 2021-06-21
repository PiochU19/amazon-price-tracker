import React, { useEffect, useState } from "react";
import "./Register.scss";
import { useHistory } from "react-router-dom";
import cookie from "react-cookies";

import Loader from "./../Loader/Loader";

import axiosInstance from "./../../axios";


const Register = () => {

    const initialFormData = Object.freeze({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        password_confirmation: ''
    });

    const history = useHistory();
    const [isReady, setIsReady] = useState(false); // is not authenticated
    const [formData, updateFormData] = useState(initialFormData);
    const [message, setMessage] = useState("register");

    useEffect(() => {
        if (!cookie.load("Logged")) {
            setIsReady(true);
        } else {
            history.push("/login");
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
            .post("account/user/", {
                first_name: formData.first_name,
                last_name: formData.last_name,
                email: formData.email,
                password: formData.password,
                password_confirmation: formData.password_confirmation
            }, {
                headers: {
                    "X-CSRFToken": cookie.load("csrftoken")
                }
            })
            .then(res => {
                history.push({
                    pathname: "/login",
                    state: {
                        message: "email was sent"
                    }
                });
            })
            .catch(error => {
                if (error.response.status === 429) {
                    setMessage("too many tries, try again later")
                } else {
                    setMessage("Something went wrong");
                };
            });
    };

    return (
        <>
            {isReady
                ?
                <form className="Register" onSubmit={handleSubmit}>
                    <div className="Register__title">
                        <h3>
                            {message}
                        </h3>
                    </div>
                    <div>
                        <input
                            className="Input"
                            id="email"
                            type="email"
                            placeholder="email"
                            onChange={handleChange}
                        />
                    </div>
                    <div>
                        <input
                            className="Input"
                            id="first_name"
                            type="text"
                            placeholder="first name"
                            onChange={handleChange}
                        />
                    </div>
                    <div>
                        <input
                            className="Input"
                            id="last_name"
                            type="text"
                            placeholder="last name"
                            onChange={handleChange}
                        />
                    </div>
                    <div>
                        <input
                            className="Input"
                            id="password"
                            type="password"
                            placeholder="password"
                            onChange={handleChange}
                        />
                    </div>
                    <div>
                        <input
                            className="Input"
                            id="password_confirmation"
                            type="password"
                            placeholder="password confirmation"
                            onChange={handleChange}
                        />
                    </div>
                    <div>
                        <input
                            className="Button"
                            type="submit"
                            value="register"
                        />
                    </div>
                </form>
                :
                <Loader />
            }
        </>
    );
};

export default Register