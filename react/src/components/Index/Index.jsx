import React, { useEffect, useState } from "react";
import "./Index.scss";
import cookie from "react-cookies";
import { Link, useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";
import { ReactComponent as LogoutSVG } from "./../../assets/svgs/logout.svg";

import axios from "axios";


const Index = () => {

    const history = useHistory();
    const [data, setData] = useState(false);
    const [products, setProducts] = useState(false);

    useEffect(() => {
        if (cookie.load("Logged")) {

            axios
                .get("https://run.mocky.io/v3/2ca493f1-d1d5-41cb-96e5-addeb747f550")
                .then(res => {
                    setData(res.data);
                    setProducts(res.data.products);
                })
                .catch(error => {
                    console.log(error);
                });
        } else {
            history.push("/login");
        };
    }, []);

    return (
        <div className="Index">
            { data
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
                                    Hello { data.first_name }!
                                </h2>
                            </div>
                            <div className="Index__header-logout">
                                <Link to="/logout">
                                    <LogoutSVG className="LogoutSVG" />
                                </Link>
                            </div>
                        </div>
                        <div className="Index__body">
                            { products
                                ?
                                <>
                                    Tu będą produkty
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