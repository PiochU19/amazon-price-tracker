import React, { useEffect } from "react";
import { useHistory } from "react-router-dom";
import cookie from "react-cookies";

import Loader from "./../Loader/Loader";


const Logout = () => {

    const history = useHistory();

    useEffect(() => {
        cookie.remove("Logged");
        history.push("/login");
    }, []);

    return (
        <Loader />
    )
};

export default Logout