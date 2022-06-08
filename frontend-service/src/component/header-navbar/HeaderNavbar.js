import React from "react";
import { ReactComponent as ReactLogo } from './stock.svg';
import './header-navbar.styles.scss';

const HeaderNavbar = () => {
    return (
        <div className="top-navbar">
            <div className="left">
                <div className="svg">
                    <ReactLogo/>
                </div>
                <h1 className="text">Stock Watchlist</h1>
            </div>
            <div className="right">
                <a href="mailto:name@email.com"> Contact us </a>
            </div>
            
        </div>
    );
};
export default HeaderNavbar;