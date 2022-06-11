import React, { useContext } from "react";
import DataContext from "../../../context/data-context";
import { Chart as ChartJS } from 'chart.js/auto'
import { Line } from 'react-chartjs-2';
import './chart.styles.scss';

const LineChart = () => {
    const ctx = useContext(DataContext);
    const date = ctx.bars.map(obj => obj.t.split('T')[0])
    const price = ctx.bars.map(obj => obj.vw)
    return (
        <div className="chart">
            <Line data={{
                labels: date,
                datasets: [{
                    label: 'price',
                    lineTension: 0.5,
                    backgroundColor: '#55c788',
                    borderColor: '#342626',
                    borderWidth: 1,
                    pointRadius: 0,
                    data: price,
                }]
            }}
                options={{
                    scales: {
                        xAxes: [{
                            type: 'time',
                            time: {
                                unit: 'day'
                            }
                        }]
                    },
                    title: {
                        display: true,
                        text: 'Average Rainfall per month',
                        fontSize: 20
                    },
                    legend: {
                        display: true,
                        position: 'right'
                    }
                }
                }
            />
        </div>
    );
};

export default LineChart;
