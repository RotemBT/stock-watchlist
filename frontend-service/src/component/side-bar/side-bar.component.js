import React, { useState } from "react";
import './side-bar.styles.scss';
import Stock from "./stock.component";
import { SYMBOLS } from "./add-stocks.constant";
const SideBar = (props) => {
    const [isOpen, setOpen] = useState(false);
    return (
        <div className="left-pane" style={{width: isOpen? '250px' : '50px', minHeight: 'calc(100vh - 83px)'}}>
            <button 
                className="left-pane-button" 
                type="button"
                onClick={() => setOpen(!isOpen)}
            >
                Add stock
            </button>
            {isOpen && (
                <div>
                    {SYMBOLS.map( symbol => <Stock name={symbol}/> )}
                   
                </div>
            )}
        </div>
    );
};
export default SideBar;