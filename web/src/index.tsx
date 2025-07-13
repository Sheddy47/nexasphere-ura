import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<App />);
}
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  python-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Install nexasphere_ura package
        run: pip install -e .
      - name: Run pytest
        run: pytest --maxfail=1 --disable-warnings

  react-tests:
    runs-on: ubuntu-latest
    needs: python-tests
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16.x'
      - name: Install npm dependencies
        run: cd web && npm install
      - name: Run React tests
        run: cd web && npm test -- --watchAll        name: CI
        
        on:
          push:
            branches: [main]
          pull_request:
            branches: [main]
        
        jobs:
          python-tests:
            runs-on: ubuntu-latest
            steps:
              - name: Checkout code
                uses: actions/checkout@v4
              - name: Set up Python
                uses: actions/setup-python@v5                name: CI
                
                on:
                  push:
                    branches: [main]
                  pull_request:
                    branches: [main]
                
                jobs:
                  python-tests:
                    runs-on: ubuntu-latest
                    steps:
                      - name: Checkout code
                        uses: actions/checkout@v4
                      - name: Set up Python
                        uses: actions/setup-python@v5
                        with:
                          python-version: '3.x'
                      - name: Install dependencies
                        run: pip install -r requirements.txt
                      - name: Install nexasphere_ura package
                        run: pip install -e .
                      - name: Run pytest
                        run: pytest --maxfail=1 --disable-warnings
                
                  react-tests:
                    runs-on: ubuntu-latest
                    needs: python-tests
                    steps:
                      - name: Checkout code
                        uses: actions/checkout@v4
                      - name: Set up Node.js
                        uses: actions/setup-node@v3
                        with:
                          node-version: '16.x'
                      - name: Install npm dependencies
                        run: cd web && npm install
                      - name: Run React tests
                        run: cd web && npm test -- --watchAll=false
                with:
                  python-version: '3.x'
              - name: Install dependencies
                run: pip install -r requirements.txt
              - name: Install nexasphere_ura package
                run: pip install -e .
              - name: Run pytest
                run: pytest --maxfail=1 --disable-warnings
        
          react-tests:
            runs-on: ubuntu-latest
            needs: python-tests
            steps:
              - name: Checkout code
                uses: actions/checkout@v4
              - name: Set up Node.js
                uses: actions/setup-node@v3
                with:
                  node-version: '16.x'
              - name: Install npm dependencies
                run: cd web && npm install
              - name: Run React tests
                run: cd web && npm test -- --watchAll