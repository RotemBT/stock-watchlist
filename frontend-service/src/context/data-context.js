import React, { useState } from "react";
import { SYMBOLS } from "./stocks.constant";

const DataContext = React.createContext({
    stocksWatch: [],
    stocksUnwatch: [...SYMBOLS],
    onWatch: (stock, isInList) => { },
    fetchNews: () => { },
    fetchBars: () => { },
    news: {},
    bars: []
});
export const DataContextProvider = (props) => {
    const [stocksWatch, setStocksWatch] = useState([]);
    const [stocksUnwatch, setSymbolsUnwatch] = useState([...SYMBOLS]);
    const [news, setNews] = useState({});
    const [bars, setBars] = useState([]);
    const url = 'http://localhost:8085/api/';
    const onWatch = (stock, isInList) => {
        if (isInList) {
            setStocksWatch([...stocksWatch.filter(s => s !== stock)]);
            setSymbolsUnwatch([...stocksUnwatch, stock]);
        } else {
            setStocksWatch([...stocksWatch, stock]);
            setSymbolsUnwatch([...stocksUnwatch.filter(s => s !== stock)]);
        }
    };
    const filterNews = (news, filterSymbol) => news?.filter(obj => obj.symbols?.includes(filterSymbol));

    const fetchNews = async () => {
        const stocks = [...stocksWatch].join(',');
        const response = await fetch(`${url}news?stocks=${stocks}`);
        const data = await response.json();
        stocksWatch.forEach(s => {
            if (!news[s]) {
                Object.assign(news, { [s]: filterNews([...data.news], s) });
            } else {
                news[s].concat(...filterNews([...data.news], s));
            }
        });
        const getNews = { ...news };

        setNews(getNews);
    };
    const fetchBars = async (stock) => {
        const response = await fetch(`${url}bars?stock=${stock}`);
        const data = await response.json();
        const bars = [...data[stock]];
        setBars(bars);
    };
    return (
        <DataContext.Provider value={{
            stocksWatch: stocksWatch,
            stocksUnwatch: stocksUnwatch,
            onWatch: onWatch,
            fetchNews: fetchNews,
            fetchBars: fetchBars,
            news: news,
            bars: bars
        }}>{props.children}</DataContext.Provider>
    );
}
export default DataContext;