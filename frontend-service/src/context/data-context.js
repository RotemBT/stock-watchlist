import React, { useState } from "react";
import { SYMBOLS } from "./stocks.constant";

const DataContext = React.createContext({
    stocksWatch: [],
    stocksUnwatch: [...SYMBOLS],
    onWatch: (stock, isInList) => { },
    fetchNews: () => { },
    news: []
});
export const DataContextProvider = (props) => {
    const [stocksWatch, setStocksWatch] = useState([]);
    const [stocksUnwatch, setSymbolsUnwatch] = useState([...SYMBOLS]);
    const [news, setNews] = useState([]);
    const url = 'https://data.alpaca.markets/v1beta1/news?start=2021-12-28T00:00:00Z&end=2021-12-31T11:59:59Z&symbols=AAPL,TSLA\' --header \'Apca-Api-Key-Id: AKQMMBGXFI6VWHXB20T5\' --header \'Apca-Api-Secret-Key: 6BgrUicRl7xMOmBl2w8OgxsbdQOsCJUdSC3geEne\'';

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
        const response = await fetch(url);
        const data = await response.json();
        const getNews = [...data.news];
        console.log(data);
        setNews(getNews);
    };
    return (
        <DataContext.Provider value={{
            stocksWatch: stocksWatch,
            stocksUnwatch: stocksUnwatch,
            onWatch: onWatch,
            fetchNews: fetchNews,
            news: news
        }}>{props.children}</DataContext.Provider>
    );
}
export default DataContext;