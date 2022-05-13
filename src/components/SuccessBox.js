import React, {useState} from 'react';
import './SuccessBox.css';
import Button from '@mui/material/Button';

function SuccessBox(){
    const [style, setStyle] = useState("box");
    const [blur, setBlur] = useState('blur')
    const changeStyle = () => {
        setStyle("box2");
        setBlur("blur2")
        setTimeout(function(){setStyle("box3")}, 250)
    }
    return(
        <div id='total'>
            <div className={blur}></div>
            <div className={style}>
                <h1 id='title'>SUCCESS!</h1>
                <h2>You have successfully signed into eventbrite!</h2>
                <Button variant="contained" color='success' id='button' onClick={changeStyle}>
                    Continue to the Calendar
                </Button>
            </div>
        </div>

    )
}

export default SuccessBox