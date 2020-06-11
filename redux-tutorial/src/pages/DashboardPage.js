import React, { Component } from 'react';
import { Link } from 'react-router-dom';

const DashboardPage = () => (
    <section>
        <h1>Dashboard</h1>
        <p>This is the Dashboard</p>

        <Link to="/posts" className="button">
            View Posts
        </Link>
    </section>
)



export default DashboardPage;