import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Reparaciones = () => {
  const [reparaciones, setReparaciones] = useState([]);

  // Fetch de las reparaciones desde la API
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/reparaciones')
      .then(response => {
        setReparaciones(response.data);
      })
      .catch(error => {
        console.error("Hubo un error al obtener las reparaciones!", error);
      });
  }, []);

  return (
    <div>
      <h1>Lista de Reparaciones</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Vehículo ID</th>
            <th>Descripción</th>
            <th>Fecha</th>
            <th>Costo</th>
          </tr>
        </thead>
        <tbody>
          {reparaciones.map((reparacion) => (
            <tr key={reparacion.id}>
              <td>{reparacion.id}</td>
              <td>{reparacion.vehiculo_id}</td>
              <td>{reparacion.descripcion}</td>
              <td>{new Date(reparacion.fecha).toLocaleString()}</td>
              <td>{reparacion.costo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Reparaciones;
