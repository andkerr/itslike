function RandButton() {
    function handleClick() {
           fetch('/random')
            .then(response => response.json())
            .then(data => {
                console.log(data.rand1, data.rand2);
            });
    }

    return (
        <button
            className="randomizeButton"
            onClick={() => handleClick()}
        >
            Click Me!
        </button>
    );
}

export default RandButton;