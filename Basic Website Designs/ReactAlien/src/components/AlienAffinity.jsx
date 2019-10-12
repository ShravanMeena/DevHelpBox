import React, { Component } from "react";
import RenderCounter from "./RenderCounter";
import "../styles/AlienAffinity.css";

const animeImgObject = {
    img1:
        "http://www.scified.com/topics/571343805484005.jpg",
    img2:
        "https://dumielauxepices.net/sites/default/files/xenomorph-clipart-alien-queen-829179-3720683.jpg",
    img3:
        "https://78.media.tumblr.com/892c9f06dacdd4c3099b8c692213cd4f/tumblr_oozvleGZR71txn1qro1_r2_1280.png",
    img4:
        "https://i.pinimg.com/originals/6d/e1/32/6de13278901d8c4d5f426b8fa2872533.png",
    img5:
        "https://cdn11.bigcommerce.com/s-0kvv9/images/stencil/1280x1280/products/200483/283385/apio6fx9f__97660.1519947716.jpg?c=2&imbypass=on",
    img6:
        "https://secure.i.telegraph.co.uk/multimedia/archive/03064/Alien-intro_3064438b.jpg"
};

const img = Object.values(animeImgObject);

let toggle;
let i = 0;

class AlienAffinity extends Component {
    constructor(props) {
        super(props);
        this.count = 0;
        this.state = {
            renderCount: 0,
            image: null,
            images: [],
            imgSrc: null
        };
    }

    componentWillMount() {
        const currentImg = img[img.length - 1];
        // const currentImg = img[0];
        this.setState({
            imgSrc: currentImg
        });
        toggle = setInterval(this.handleImgChange, 1000);
    }

    handleImgChange = () => {
        if (i < img.length) {
            this.setState({
                imgSrc: img[i++]
            });
        } else {
            i = 0;
        }
        return;
    };

    // future feature
    // addImgToSite = img => {
    //     animeImgObject.img5 = img;
    // };

    componentWillUnmount() {
        clearInterval(toggle);
    }

    render() {
        const { imgSrc } = this.state;
        return (
            <div id="main-app">
                <>
                    <img id="img" src={imgSrc} alt="anime stuff" />
                    <RenderCounter renderCount={++this.count} />
                </>
            </div>
        );
    }
}
export default AlienAffinity;
