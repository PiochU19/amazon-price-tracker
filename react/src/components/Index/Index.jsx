import React, { useEffect, useState } from "react";
import "./Index.scss";
import cookie from "react-cookies";
import { Link, useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";
import { ReactComponent as LogoutSVG } from "./../../assets/svgs/logout.svg";

import axiosInstance from "./../../axios";


const Index = () => {

    const history = useHistory();
    const [data, setData] = useState(false);
    const [trackers, setTrackers] = useState(false);

    useEffect(() => {
        if (cookie.load("Logged")) {

            axiosInstance
                .get("account/user/")
                .then(res => {
                    console.log(res);
                    setData(res.data);
                    setTrackers(res.data.trackers);
                })
                .catch(error => {
                    cookie.remove("Logged");
                    history.push("/login");
                });
        } else {
            history.push("/login");
        };
    }, []);

    return (
        <div className="Index">
            {data
                ?
                <>
                    <div className="Index__header">
                        <div className="Index__header-button">
                            <Link to="/add">
                                <input className="Button Button__login" type="submit" value="add" />
                            </Link>
                        </div>
                        <div className="Index__header-user">
                            <h2>
                                Hello {data.first_name}!
                            </h2>
                        </div>
                        <div className="Index__header-logout">
                            <Link to="/logout">
                                <LogoutSVG className="LogoutSVG" />
                            </Link>
                        </div>
                    </div>
                    <div className="Index__body">
                        {trackers.length !== 0
                            ?
                            <>
                                ll be trackers
                            </>
                            :
                            <p className="Index__noprod">
                                You track no products :(
                            </p>
                        }
                    </div>
                </>
                :
                <Loader />
            }
        </div>
    );
};

export default Index