import React, {useState, useEffect} from 'react';
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
            {placeholder}
        </header>
        </div>
    );
}

export default App;
