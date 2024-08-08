// import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

// //import React from 'react';
// import { BrowserRouter as Router } from 'react-router-dom';
// import Home from './Home'; // Corrected path
// import About from './About'; // Corrected path
// import ConcertDetails from './Concert/ConcertDetails'; // Corrected path
// import Login from './Auth/Login'; // Corrected path
// import Register from './Auth/Register'; // Corrected path
// import Profile from './User/Profile'; // Corrected path


import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import About from './pages/About';
import ConcertDetails from './Concert/ConcertDetails';
import Login from './Auth/Login';
import Register from './Auth/Register';
import Profile from './User/Profile';
import ConcertList  from './Concert/ConcertList';
import Navbar from './Concert/NavBar';


function App() {
  return (
    <Router>
      <Navbar />
      <div>
        <main style={{ padding: '20px' }}>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/concert/:id" component={ConcertDetails} />
            <Route path='/concerts' component={ConcertList} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <Route path="/profile" component={Profile} />
            {/* <Route path="/cart" component={Cart} /> */}
            <Route path="*" render={() => <h1>404 Not Found</h1>} />
          </Switch>
        </main>
      </div>
    </Router>
  );
}

export default App;