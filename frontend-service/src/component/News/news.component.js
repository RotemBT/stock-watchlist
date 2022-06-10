import React from "react";
import './news.styles.scss';

const renderTable = (news) => (
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
                <td>{n.symbol}</td>
                <td>{n.headline}</td>
                <td><a href={n.url}>Link to source</a></td>
                <td>{n.source}</td>
                <td>{n.timeCreate}</td>
            </tr>
        ))}
    </table>
);
const News = (props) => {
    const { news } = props;
    return (
        <div className="news">
            {renderTable(news)}
        </div>

    );
};

export default News;