import React from "react";
import { ReactComponent } from './x.svg';
import './stock.style.scss'
const Stock = (props) => {
    return (
        <button className="stock">
            <div className="svg-stock">
                <ReactComponent />
            </div>
            {props.name}
        </button>
    );
};
export default Stock;