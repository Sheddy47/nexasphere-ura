import React, { useRef, useEffect, forwardRef, useImperativeHandle } from 'react';

export interface HexWidgetProps {
  cells: Array<{ q: number; r: number; value?: number }>
  size?: number
}

const HexWidget = forwardRef<HTMLCanvasElement, HexWidgetProps>(({ cells, size = 30 }, ref) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useImperativeHandle(ref, () => canvasRef.current as HTMLCanvasElement);

  useEffect(() => {
    const ctx = canvasRef.current?.getContext('2d');
    if (!ctx) return;
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    cells.forEach(({ q, r, value }) => {
      const [x, y] = [size * (3/2 * q) + 200, size * (Math.sqrt(3) * (r + q/2)) + 200];
      ctx.beginPath();
      for (let i = 0; i < 6; i++) {
        const angle = Math.PI / 3 * i;
        const px = x + size * Math.cos(angle);
        const py = y + size * Math.sin(angle);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.fillStyle = value !== undefined ? `rgba(0,0,255,${Math.min(1, value)})` : '#eee';
      ctx.fill();
      ctx.strokeStyle = '#333';
      ctx.stroke();
    });
  }, [cells, size]);

  return <canvas ref={canvasRef} width={400} height={400} />;
});

export default HexWidget;
