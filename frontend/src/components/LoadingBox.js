import React from 'react';
import PacmanLoader from "react-spinners/PacmanLoader";

export default function LoadingBox() {
  return (
    <div className="loading">
      <i className="fa fa-spinner fa-spin"></i> Loading...
    </div>
  );
}
