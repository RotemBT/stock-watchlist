import React, { useState } from "react";
import { SYMBOLS } from "./stocks.constant";

const DataContext = React.createContext({
    stocksWatch: [],
    stocksUnwatch: [...SYMBOLS],
    onWatch: (stock, isInList) => { }
});
export const DataContextProvider = (props) => {
    const [stocksWatch, setStocks] = useState([]);
    const [stocksUnwatch, setSymbols] = useState([...SYMBOLS]);
    const onWatch = (stock, isInList) => {
        if (isInList) {
            setStocks([...stocksWatch.filter(s => s !== stock)]);
            setSymbols([...stocksUnwatch, stock]);
        } else {
            setStocks([...stocksWatch, stock]);
            setSymbols([...stocksUnwatch.filter(s => s !== stock)]);
        }
    };
    return (
        <DataContext.Provider value={{
            stocksWatch: stocksWatch,
            stocksUnwatch: stocksUnwatch,
            onWatch: onWatch
        }}>{props.children}</DataContext.Provider>
    );
}
export default DataContext;