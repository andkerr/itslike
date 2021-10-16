import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
    const [placeholder, setPlaceholder] = useState('Flask is not connected');

    useEffect(() => {
        fetch('/hello')
            .then(response => response.json())
            .then(data => {setPlaceholder(data.response)});
    });
    
    return (
        <div className="App">
        <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
            Edit <code>src/App.js</code> and save to reload.
            </p>
            {placeholder}
        </header>
        </div>
    );
}

export default App;
