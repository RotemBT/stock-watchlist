import React from "react";
import './modal.styles.scss';

const Modal = (props) => {
    return (
        <div className="modal">
            {props.children}
        </div>
    );
};
export default Modal;