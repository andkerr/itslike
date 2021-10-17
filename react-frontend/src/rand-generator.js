import './rand-generator.css';
import React from 'react';

class RandGenerator extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            rand1: "Airbnb",
            rand2: "parking spots"
        };
    }

    genRandom() {
        fetch('api/random')
         .then(response => response.json())
         .then(data => {
             this.setState({
                 rand1: data.rand1,
                 rand2: data.rand2
             });
         });
    }

    render() {
        return (
            <div className="rand-generator">

                <h3 className="perm-text">It's like...</h3>
                <div className="rand-text">
                    {this.state.rand1}
                </div>
                <h3 className="perm-text">for</h3>
                <div className="rand-text">{this.state.rand2}</div>

                <button
                    className="rand-button"
                    onClick={() => this.genRandom()}
                >
                    Give me another idea!
                </button>
            </div>
        );
    }
}

export default RandGenerator;