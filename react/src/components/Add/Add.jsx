import React, { useEffect, useState } from "react";
import "./Add.scss";
import cookie from "react-cookies";
import { useHistory } from "react-router-dom";

import Loader from "./../Loader/Loader";

import axios from "axios";


const Add = () => {

    const initialFormData = Object.freeze({
		product_name: '',
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

        axios
            .get("https://run.mocky.io/v3/d6148a81-29b2-4a76-88c3-60dbd7f7e6a0")
            .then(res => {
                setProducts(res.data);
                setFetching(false);
            })
            .catch(error => {
                setProducts(null);
                setFetching(false);
            });
    };

    return (
        <form className="Add" onSubmit={ handleSubmit }>
            { ready
                ?
                    <>
                        <div className="Add__input">
                            <input
                                className="Input Input__add"
                                type="text"
                                id="product_name"
                                placeholder="product name"
                                onChange={ handleChange }
                            />
                        </div>
                        <div className="Add_button">
                            <input
                                className="Button"
                                type="submit"
                                value="search"
                            />
                        </div>
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
                                            {products.map((product, index) => (
                                                <div key={ index } id={ index }>
                                                    { product[0] }
                                                </div>
                                            ))}
                                        </>
                                    );
                                } else if (products === null) {
                                    return (
                                        <p>
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
        </form>
    );
};

export default Add