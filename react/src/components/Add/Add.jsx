import React, { useEffect, useState } from "react";
import "./Add.scss";
import cookie from "react-cookies";
import { useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";

import axiosInstance from "./../../axios";


const Add = () => {

    const initialFormData = Object.freeze({
        product_name: '',
        price: '',
    });

    const history = useHistory();
    const [ready, setReady] = useState(false);
    const [fetching, setFetching] = useState(false);
    const [products, setProducts] = useState(false);
    const [formData, updateFormData] = useState(initialFormData);

    useEffect(() => {
        if (cookie.load("Logged")) {
            setReady(true);
        } else {
            history.push("/login");
        };
    }, []);

    const handleChange = e => {
        updateFormData({
            ...formData,
            [e.target.id]: e.target.value.trim(),
        });
    };

    const handleSubmit = async e => {
        e.preventDefault();
        setFetching(true);

        axiosInstance
            .post("products/list/", {
                product_name: formData.product_name
            }, {
                headers: {
                    "X-CSRFToken": cookie.load("csrftoken")
                }
            })
            .then(res => {
                setProducts(res.data);
                setFetching(false);
            })
            .catch(error => {
                setProducts(null);
                setFetching(false);
            });
    };

    const handleSubmitTrack = async e => {
        e.preventDefault();
        if (formData.price !== "") {
            const id = e.target.id;
            const product = products[id];

            axiosInstance
                .post("products/tracker/", {
                    product_name: product[0],
                    link: product[3],
                    image: product[1],
                    price: formData.price,
                }, {
                    headers: {
                        "X-CSRFToken": cookie.load("csrftoken")
                    }
                })
                .then(res => {
                    history.push("/");
                })
                .catch(error => {
                    setProducts(null);
                });
        };
    };

    return (
        <div className="Add">
            {ready
                ?
                <>
                    <form onSubmit={handleSubmit}>
                        <div className="Add__input">
                            <input
                                className="Input Input__add"
                                type="text"
                                id="product_name"
                                placeholder="product name"
                                onChange={handleChange}
                            />
                        </div>
                        <div className="Add_button">
                            <input
                                className="Button"
                                type="submit"
                                value="search"
                            />
                        </div>
                    </form>
                    <div className="Add__body">
                        {(() => {
                            if (fetching) {
                                return (
                                    <div className="Add__loader">
                                        <Loader />
                                    </div>
                                )
                            } else if (products) {
                                return (
                                    <>
                                        <div className="Add__price__input">
                                            <h3>
                                                Set the price
                                            </h3>
                                            <input
                                                type="number"
                                                id="price"
                                                className="Input"
                                                placeholder="price"
                                                onChange={handleChange}
                                            />
                                        </div>
                                        {products.map((product, index) => (
                                            <form
                                                key={index}
                                                id={index}
                                                className="Add__product"
                                                onSubmit={handleSubmitTrack}
                                            >
                                                <div className="Add__product__image">
                                                    <img src={product[1]} className="Add__product-image" />
                                                </div>
                                                <div className="Add__product__name">
                                                    <h6>
                                                        {product[0]}
                                                    </h6>
                                                </div>
                                                <div className="Add__product__price__button">
                                                    <div>
                                                        <h4>
                                                            {product[2]} PLN
                                                        </h4>
                                                    </div>
                                                    <div>
                                                        <input
                                                            type="submit"
                                                            className="Button"
                                                            value="track"
                                                        />
                                                    </div>
                                                </div>
                                            </form>
                                        ))}
                                    </>
                                );
                            } else if (products === null) {
                                return (
                                    <p className="Add__noneprod">
                                        We couldn't find any products :(
                                    </p>
                                )
                            }
                        })()}
                    </div>
                </>
                :
                <Loader />
            }
        </div>
    );
};

export default Add