import React from "react";
import './App.styles.scss';
import AddStock from "./component/add-stocks/add-stocks.component";
import HeaderNavbar from './component/header-navbar/HeaderNavbar';
import News from "./component/News/news.component";
import SideBar from "./component/side-bar/side-bar.component";
function App() {
  return (
    <div className="App">
      <HeaderNavbar />
      <SideBar />
      <div>
        <News />
        <AddStock />
      </div>
      
    </div>
  );
}

export default App;
