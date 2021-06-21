import React, { useEffect, useState } from "react";
import "./Index.scss";
import cookie from "react-cookies";
import { Link, useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";
import { ReactComponent as LogoutSVG } from "./../../assets/svgs/logout.svg";

import axiosInstance from "./../../axios";


const Index = () => {

    const history = useHistory();
    const [firstName, setFirstName] = useState(false);
    const [trackers, setTrackers] = useState([]);

    useEffect(() => {
        if (cookie.load("Logged")) {
            loadTrackers();
        } else {
            history.push("/login");
        };
    }, []);

    const loadTrackers = () => {
        axiosInstance
            .get("account/user/")
            .then(res => {
                setFirstName(res.data.first_name);
                setTrackers(res.data.trackers);
            })
            .catch(error => {
                cookie.remove("Logged");
                history.push("/login");
            });
    };

    const handleDelete = async e => {
        e.preventDefault();
        setFirstName(false);
        const slug = e.target.id;

        axiosInstance
            .delete(`products/tracker/${slug}/`, {
                headers: {
                    "X-CSRFToken": cookie.load("csrftoken")
                }
            })
            .then(res => {
                loadTrackers();
            })
            .catch(error => {
                history.push("/login");
            });
    };

    return (
        <div className="Index">
            {firstName
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
                                Hello {firstName}!
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
                                {trackers.map((tracker, index) => (
                                    <form
                                        key={index}
                                        id={tracker.product.slug}
                                        className="Add__product"
                                        onSubmit={handleDelete}
                                    >
                                        <div className="Add__product__image">
                                            <img src={tracker.product.image} className="Add__product-image" />
                                        </div>
                                        <div className="Add__product__name">
                                            <h6>
                                                {tracker.product.name}
                                            </h6>
                                        </div>
                                        <div className="Add__product__price__button">
                                            <div>
                                                <h4>
                                                    {tracker.price} PLN
                                                </h4>
                                            </div>
                                            <div>
                                                <input
                                                    type="submit"
                                                    className="Button"
                                                    value="delete"
                                                />
                                            </div>
                                        </div>
                                    </form>
                                ))}
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