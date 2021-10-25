import './App.css';
import RandGenerator from './rand-generator';
import Header from './header';
import process from 'process';

console.log(process.env);

function App() {
    return (
        <div className="App">
            <Header />
            <RandGenerator />
        </div>
    );
}

export default App;
