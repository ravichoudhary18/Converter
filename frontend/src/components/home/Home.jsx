import React from 'react';
import useAxiosPrivate from '../../hooks/useAxiosPrivate'
import Button from 'react-bootstrap/Button';
import NavBar from '../navBar/NavBar'


const Home = () => {

    return (
        <div>
            <NavBar />
            <Button>Home</Button>
        </div>
    );
}

export default Home;
