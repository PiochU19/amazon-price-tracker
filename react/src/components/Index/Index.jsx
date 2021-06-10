import React, { useEffect, useState } from "react";
import "./Index.scss";
import cookie from "react-cookies";
import { useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";


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
                        <p>kek</p>
                    </>
                :
                <Loader />
            }
        </div>
    );
};

export default Index