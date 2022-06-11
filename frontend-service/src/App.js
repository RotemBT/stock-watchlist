import React from "react";
import HeaderNavbar from './component/header-navbar/HeaderNavbar';
import FilterBar from "./component/data-visualization/filter-bar.component";
import SideBar from "./component/side-bar/side-bar.component";
import './App.styles.scss';

function App() {
  return (
    <div className="App">
      <div className="header">
        <HeaderNavbar />
      </div>
      <div className="menu">
        <SideBar />
      </div>
      <div className="main">
        <FilterBar />
      </div>
    </div>
  );
}

export default App;
