import React from "react";
import { ReactComponent } from './x-sign.svg';
import './stock.style.scss'
const Stock = (props) => {
    const { name, onClick, isInList } = props;
    return (
        <button
            className="stock"
            style={{ backgroundColor: !isInList ? 'mediumseagreen' : '#41dc41' }}
            onClick={() => onClick(name, isInList)}
        >
            <div className="svg-stock">
                <ReactComponent />
            </div>
            {name}
        </button>
    );
};
export default Stock;