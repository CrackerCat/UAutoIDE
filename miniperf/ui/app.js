import React from 'react'
// import Window from "./window";
import MainPage from "./Components/MainPage";

class App extends React.Component {
  render() {
    return(
      <div style={{position: "relative", width:"100%", height: "100%"}}>
        <MainPage/>
      </div>
    )
  }
}

export  default App