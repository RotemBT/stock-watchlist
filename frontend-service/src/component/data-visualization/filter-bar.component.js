import React, { useContext, useEffect, useState } from "react";
import DataContext from "../../context/data-context";
import News from "./news.component";
import LineChart from "./chart/chart.component";
import './filter-bar.styles.scss';

const FilterBar = () => {
    const ctx = useContext(DataContext);
    const news = ctx.news;
    const [filterSymbol, setFilterSymbol] = useState('');
    const filteredNews = (news, filterSymbol) => news?.filter(obj => obj.symbols?.includes(filterSymbol));

    useEffect(() => {
        if (!filterSymbol && ctx.stocksWatch.length !== 0) {
            setFilterSymbol(ctx.stocksWatch[0]);
        }
    }, [filterSymbol, ctx, ctx.stocksWatch]);

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
                        onClick={() => {
                            setFilterSymbol(s);
                            ctx.fetchBars(s);
                            ctx.fetchNews();
                        }}
                    >
                        {s}
                    </button>
                ))}
            </div>
            <div>
                <News
                    news={filteredNews(news, filterSymbol)}
                    symbol={filterSymbol}
                />
                <h3>Bar chart - {filterSymbol}</h3>
                <LineChart />
            </div>
        </div>
    );
};

export default FilterBar;