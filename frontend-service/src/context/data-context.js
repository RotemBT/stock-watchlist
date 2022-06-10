import React, { useState } from "react";
import { SYMBOLS } from "./stocks.constant";

const DataContext = React.createContext({
    stocksWatch: [],
    stocksUnwatch: [...SYMBOLS],
    onWatch: (stock, isInList) => { }
});
export const DataContextProvider = (props) => {
    const [stocksWatch, setStocksWatch] = useState([]);
    const [stocksUnwatch, setSymbolsUnwatch] = useState([...SYMBOLS]);
    const onWatch = (stock, isInList) => {
        if (isInList) {
            setStocksWatch([...stocksWatch.filter(s => s !== stock)]);
            setSymbolsUnwatch([...stocksUnwatch, stock]);
        } else {
            setStocksWatch([...stocksWatch, stock]);
            setSymbolsUnwatch([...stocksUnwatch.filter(s => s !== stock)]);
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