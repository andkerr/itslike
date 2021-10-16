import React, {useState, useEffect} from 'react';
import './App.css';
import RandButton from './rand-button';

function App() {
    const [placeholder, setPlaceholder] = useState('Flask is not connected');

    useEffect(() => {
        fetch('/hello')
            .then(response => response.json())
            .then(data => {setPlaceholder(data.response)});
    });
    
    return (
        <div className="App">
            {placeholder}
            <RandButton />
        </div>
    );
}

export default App;
