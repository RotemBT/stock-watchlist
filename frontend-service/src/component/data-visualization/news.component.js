import React from "react";
import './news.styles.scss';

const renderTable = (news, symbol) => (
    <table className="table">
        <thead>
            <td>Symbol</td>
            <td>Headline</td>
            <td>Url</td>
            <td>Source</td>
            <td>Time created</td>
        </thead>
        {news && news.map(n => (
            <tr>
                <td>{symbol}</td>
                <td>{n.headline}</td>
                <td><a href={n.url}>Link to source</a></td>
                <td>{n.source}</td>
                <td>{new Date(n.created_at).toLocaleDateString('en-GB')}</td>
            </tr>
        ))}
    </table>
);
const News = ({ news, symbol }) => {

    return (
        <div className="news">
            {renderTable(news, symbol)}
        </div>

    );
};

export default News;