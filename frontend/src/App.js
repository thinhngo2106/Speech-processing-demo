import React from "react";
import { BrowserRouter as Router, Route} from "react-router-dom";
import Header from "./components/header";
import HomeScreen from "./views/HomeScreen";

import CarouselContainer from './components/CarouselContainer'
import Footer from "./components/footer";


function App() {
  const images = [
    'https://images.unsplash.com/photo-1449034446853-66c86144b0ad?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80',
    'https://images.unsplash.com/photo-1470341223622-1019832be824?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2288&q=80',
  ]
  return (
    <Router>
      <div>
      <Header /> 
     
      <main>
      <Route path="/" component={HomeScreen} exact></Route>
      </main>
      </div>
    </Router> 
  );
}

export default App;
