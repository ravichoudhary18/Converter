import React from 'react'

function NavBar() {
    return (
        <nav className='nav__primary__bg__color'>
            <div className='d-flex flex-row justify-content-between align-items-center'>
                <div className='d-flex flex-column'>
                    <a href="">
                        Convert
                    </a>
                </div>
                <ul className='d-flex flex-row justify-content-between align-items-center'>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Products</a></li>
                    <li><a href="#">Product List</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Contect US</a></li>
                </ul>
            </div>
        </nav>
    )
}

export default NavBar