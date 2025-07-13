import React from 'react';
import { Scatter } from 'react-chartjs-2';
import { Chart, ScatterController, PointElement, LinearScale, Title, Tooltip, Legend } from 'chart.js';

Chart.register(ScatterController, PointElement, LinearScale, Title, Tooltip, Legend);

export interface ParetoChartProps {
  data: Array<{ x: number; y: number }>
}

const ParetoChart: React.FC<ParetoChartProps> = ({ data }) => {
  return (
    <Scatter
      data={{
        datasets: [
          {
            label: 'Pareto Front',
            data,
            backgroundColor: 'rgba(255,99,132,1)',
          },
        ],
      }}
      options={{
        scales: {
          x: { title: { display: true, text: 'Objective 1' } },
          y: { title: { display: true, text: 'Objective 2' } },
        },
        plugins: { legend: { display: false } },
      }}
    />
  );
};

export default ParetoChart;
