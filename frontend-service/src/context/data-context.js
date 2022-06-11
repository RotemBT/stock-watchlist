import React, { useState } from "react";
import { SYMBOLS } from "./stocks.constant";
import { NEWS_DATA } from "../news.data";
import { CHART_DATA } from '../chart.data';

const DataContext = React.createContext({
    stocksWatch: [],
    stocksUnwatch: [...SYMBOLS],
    onWatch: (stock, isInList) => { },
    fetchNews: () => { },
    fetchBars: () => { },
    news: [...NEWS_DATA],
    bars: [...CHART_DATA]
});
export const DataContextProvider = (props) => {
    const [stocksWatch, setStocksWatch] = useState([]);
    const [stocksUnwatch, setSymbolsUnwatch] = useState([...SYMBOLS]);
    const [news, setNews] = useState([...NEWS_DATA]);
    const [bars, setBars] = useState([...CHART_DATA]);
    const url = 'https://localhost:8085/api/';
    const onWatch = (stock, isInList) => {
        if (isInList) {
            setStocksWatch([...stocksWatch.filter(s => s !== stock)]);
            setSymbolsUnwatch([...stocksUnwatch, stock]);
        } else {
            setStocksWatch([...stocksWatch, stock]);
            setSymbolsUnwatch([...stocksUnwatch.filter(s => s !== stock)]);
        }
    };
    const fetchNews = async () => {
        const stocks = [...stocksWatch].join(',');
        const response = await fetch(`${url}news/?${stocks}`,
            {
                mode: 'no-cors',
            });
        const data = await response.json();
        const getNews = [...data.news];
        console.log(data);
        setNews(getNews);
    };
    const fetchBars = async (stock) => {
        const response = await fetch(`${url}bars/?${stock}`,
            {
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/json'
                },
            });
        const data = await response.json();
        const bars = [...data.bars];
        console.log(data);
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