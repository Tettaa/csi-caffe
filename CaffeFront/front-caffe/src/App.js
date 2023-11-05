import logo from './logo.svg';
import './App.css';
import Coffee from './caffe/Caffee';
import ModalAddForm from './modal/ModalAddForm';
import AddCaffeForm from './AddCaffeForm'
import ManageColleghi from './ManageColleghi'

// Then import Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';

import React, { useState, useEffect } from 'react';

import {
  createBrowserRouter,
  Link,
  Route,
  RouterProvider,
  BrowserRouter,
  Routes,
  Outlet
} from "react-router-dom";
import Tabellone from './Tabellone';




function Dashboard() {
  return (
    <>
    <header>
      
      <div className='d-flex flex-row'>
        <Link to='/' className='p-2'>Tabellone</Link><br/>
        <Link to='/colleghi-admin/' className='p-2'>Gestione colleghi</Link><br/>
      </div>
      
      
      
    </header>
    
    <div>
      
      <h1>Dashboard</h1>

      <main>
        <Outlet />
      </main>
    
    </div>
    </>
  );
}


function Layout() {
  // `BrowserRouter` component removed, but the <Routes>/<Route>
  // component below are unchanged
  return (
      <Routes>
        <Route path="" element={<Dashboard />}>
          <Route path="/" element={<Tabellone />} />
          <Route path="/add-caffe/:id" element={<AddCaffeForm />} />
          <Route path="/colleghi-admin/*" element={<ManageColleghi />} />
        </Route>        
      </Routes>
  );
}

const router = createBrowserRouter([
  { path: "*", Component: Layout },
]);



export default function App() {
  return <RouterProvider router={router} />;
}
