import React, { useState } from 'react';
import HexWidget from './HexWidget';
import ParetoChart from './ParetoChart';

const sampleCells = Array.from({ length: 19 }, (_, i) => ({ q: i - 9, r: 0, value: Math.random() }));
const paretoData = Array.from({ length: 10 }, (_, i) => ({ x: i, y: 10 - i + Math.random() }));

const Dashboard: React.FC = () => {
  const [cells] = useState(sampleCells);
  const [pareto] = useState(paretoData);

  return (
    <div style={{ display: 'flex', gap: 32 }}>
      <HexWidget cells={cells} />
      <ParetoChart data={pareto} />
    </div>
  );
};

export default Dashboard;
