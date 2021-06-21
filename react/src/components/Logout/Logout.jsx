import React, { useEffect } from "react";
import { useHistory } from "react-router-dom";
import cookie from "react-cookies";

import Loader from "./../Loader/Loader";

import axiosInstance from "../../axios";


const Logout = () => {

    const history = useHistory();

    useEffect(() => {
        axiosInstance
            .post("account/logout/", {}, {
                headers: {
                    "X-CSRFToken": cookie.load("csrftoken")
                }
            })
            .then(res => {
                cookie.remove("Logged");
                history.push("/login");
            });
    }, []);

    return (
        <Loader />
    )
};

export default Logout