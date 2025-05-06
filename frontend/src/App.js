import React from 'react';
import './index.css';  // Desde la misma carpeta src
import ListaReparaciones from './ListaReparaciones';
import AgregarReparacion from './AgregarReparacion';

function App() {
  return (
    <div className="App">
      <h1>Bienvenido al Taller Mecánico</h1>
      <ListaReparaciones />
      <AgregarReparacion />
    </div>
  );
}

export default App;


