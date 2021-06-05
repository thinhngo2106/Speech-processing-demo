import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import './header.css';
import { Link} from 'react-router-dom';


import 'bootstrap/dist/js/bootstrap.bundle';


function Header() {
    return(
              <nav className="navbar navbar-expand-md header">
                <Link to="/">
                  <img className="header__logo" src= {process.env.PUBLIC_URL+ "/images/logo1.png"} alt="background-img" width={144} height={81} />
                </Link>
                <h2>The Bông Music</h2>
            </nav>
    );
}
  
  export default Header;