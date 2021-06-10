import React, { useEffect, useState } from "react";
import "./Index.scss";
import cookie from "react-cookies";
import { Link, useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";
import { ReactComponent as LogoutSVG } from "./../../assets/svgs/logout.svg";


const Index = () => {

    const history = useHistory();
    const [isReady, setIsReady] = useState(false);

    useEffect(() => {
        if (cookie.load("Logged")) {
            setIsReady(true);
        } else {
            history.push("/login");
        };
    }, []);

    return (
        <div className="Index">
            { isReady
                ?
                    <>
                        <Link to="/logout">
                            <LogoutSVG className="LogoutSVG" />
                        </Link>
                    </>
                :
                <Loader />
            }
        </div>
    );
};

export default Index