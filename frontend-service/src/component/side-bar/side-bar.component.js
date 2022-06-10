import React, { useState, useContext } from "react";
import DataContext from "../../context/data-context";
import Stock from "./stock-component/stock.component";
import './side-bar.styles.scss';

const SideBar = () => {
    const [isOpen, setOpen] = useState(false);
    const ctx = useContext(DataContext);
    return (
        <div
            className="left-pane"
            style={{ width: isOpen ? '300px' : '60px' }}
        >
            <button
                className="left-pane-button"
                type="button"
                onClick={() => setOpen(!isOpen)}
            >
                Add stock
            </button>
            <hr />
            <div className="stocks-wrapper" style={{ overflowY: !isOpen ? 'none' : 'scroll' }}>
                {ctx.stocksWatch && isOpen && <p className="stock-text">Stock Watch:</p>}
                {ctx.stocksWatch && isOpen && (
                    ctx.stocksWatch?.map(symbol => <Stock
                        name={symbol}
                        onClick={ctx.onWatch}
                        isInList={true}
                    />)
                )}
                {isOpen && (
                    <div className="unwatch-stocks-wrapper">
                        <p className="stock-text">Stock Unwatch:</p>
                        {ctx.stocksUnwatch?.map(symbol => <Stock
                            name={symbol}
                            onClick={ctx.onWatch}
                            isInList={false}
                        />
                        )}

                    </div>
                )}
            </div>
        </div>
    );
};
export default SideBar;