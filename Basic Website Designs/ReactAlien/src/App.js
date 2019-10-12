import React, { Component } from "react";
import AlienAffinity from "./components/AlienAffinity";
import { Row, Column } from "simple-flexbox";
// import whyDidYouUpdate from "why-did-you-update";

import "./App.css";

// whyDidYouUpdate(React);

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            renderCount: 0
        };
        this.count = 0;
    }

    render() {
        this.count++;
        return (
            <div className="App">
                {/* <header className="App-header">
          <img
            src="https://66.media.tumblr.com/6e32fcfbe0fd1c7df642fdebd70abcb6/tumblr_olws6c7A2U1tt1gglo1_540.gif"
            alt="jhjh"
          />
        </header> */}
                <Row horizontal="center" vertical="center">
                    <Column>
                        <div>
                            <AlienAffinity id="alien-affinity" />
                        </div>
                    </Column>
                </Row>
            </div>
        );
    }
}

export default App;
