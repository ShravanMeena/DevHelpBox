import React, { Component } from "react";
import "../styles/RenderCounter.css";

class RenderCounter extends Component {
    constructor(props) {
        super(props);

        this.state = {
            count: 1
        };
    }

    render() {
        const { renderCount } = this.props;
        return (
            <div>
                <h4 id="render-count">I've rendered {renderCount} times!</h4>
            </div>
        );
    }
}

export default RenderCounter;
