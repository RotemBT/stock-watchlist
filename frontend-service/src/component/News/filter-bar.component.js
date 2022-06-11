import React, { useContext, useEffect, useState } from "react";
import DataContext from "../../context/data-context";
import News from "./news.component";
import './filter-bar.styles.scss';
const dummy = [
    { symbol: 'AAPL', headline: 'this is apple', url: 'www.example.com', source: 'benzinga', timeCreate: '22/2/2022' },
    { symbol: 'TLSA', headline: 'this is tesla', url: 'www.example.com', source: 'benzinga', timeCreate: '22/2/2022' },
    { symbol: 'MSFT', headline: 'this is microsoft', url: 'www.example.com', source: 'benzinga', timeCreate: '22/2/2022' },
    { symbol: 'FB', headline: 'this is Meta', url: 'www.example.com', source: 'benzinga', timeCreate: '22/2/2022' }
];
const FilterBar = (props) => {
    const news = dummy;
    const ctx = useContext(DataContext);
    const [filterSymbol, setFilterSymbol] = useState('');
    const filteredNews = (news, filterSymbol) => news?.filter(obj => obj.symbol === filterSymbol);

    useEffect(() => {
        if (!filterSymbol && ctx.stocksWatch.length !== 0) {
            setFilterSymbol(ctx.stocksWatch[0]);
        }
        ctx.fetchNews();
    }, [filterSymbol, ctx.stocksWatch, ctx.onWatch]);

    return (
        <div className="news-wrapper">
            <div className="filter-wrapper">
                {ctx.stocksWatch.length === 0 && (
                    <h3 className="empty-list">
                        Please Add some stocks to list
                    </h3>
                )}
                {ctx.stocksWatch && ctx.stocksWatch.map(s => (
                    <button
                        style={{ backgroundColor: s === filterSymbol && 'white', boxShadow: s === filterSymbol && '-2px 0px 3px 1px rgb(0 0 0 / 50%)' }}
                        className="tab"
                        type="button"
                        onClick={() => setFilterSymbol(s)}
                    >
                        {s}
                    </button>
                ))}
            </div>

            <News news={filteredNews(news, filterSymbol)} />
        </div>
    );
};

export default FilterBar;