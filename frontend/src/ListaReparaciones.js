import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ListaReparaciones = () => {
  const [reparaciones, setReparaciones] = useState([]);

  useEffect(() => {
    // Realizar la solicitud GET a la API para obtener las reparaciones
    axios.get('http://127.0.0.1:5000/reparaciones')
      .then(response => {
        setReparaciones(response.data);
      })
      .catch(error => {
        console.error('Hubo un error al obtener las reparaciones:', error);
      });
  }, []);

  return (
    <div>
      <h2>Lista de Reparaciones</h2>
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
          {reparaciones.map(reparacion => (
            <tr key={reparacion.id}>
              <td>{reparacion.id}</td>
              <td>{reparacion.vehiculo_id}</td>
              <td>{reparacion.descripcion}</td>
              <td>{reparacion.fecha}</td>
              <td>{reparacion.costo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ListaReparaciones;
