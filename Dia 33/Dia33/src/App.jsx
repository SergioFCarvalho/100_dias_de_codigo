import { useState } from "react";
import "./App.css";
import MyComponent from "./components/MyComponent";

function App() {
  return (
    <>
      <MyComponent
        title="Título via propriedades(props)"
        description="Descrição via (props)"
      />
    </>
  );
}

export default App;
