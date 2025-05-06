import React, { useState } from 'react';
import axios from 'axios';

const AgregarReparacion = () => {
  const [vehiculoId, setVehiculoId] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [fecha, setFecha] = useState('');
  const [costo, setCosto] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validar que los campos no estén vacíos
    if (!vehiculoId || !descripcion || !fecha || !costo) {
      alert('Por favor complete todos los campos');
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:5000/reparaciones', {
        vehiculo_id: vehiculoId,
        descripcion: descripcion,
        fecha: fecha,
        costo: costo,
      });

      // Comprobar si la respuesta tiene la propiedad "mensaje"
      if (response.data && response.data.mensaje) {
        alert(response.data.mensaje);  // Mostrar el mensaje del backend
      } else {
        alert('No se recibió una respuesta válida');
      }
    } catch (error) {
      console.error('Hubo un error al agregar la reparación:', error);
      alert('Hubo un error al agregar la reparación');
    }
  };

  return (
    <div>
      <h2>Agregar Reparación</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Vehículo ID:</label>
          <input
            type="number"
            value={vehiculoId}
            onChange={(e) => setVehiculoId(e.target.value)}
          />
        </div>
        <div>
          <label>Descripción:</label>
          <input
            type="text"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
          />
        </div>
        <div>
          <label>Fecha:</label>
          <input
            type="date"
            value={fecha}
            onChange={(e) => setFecha(e.target.value)}
          />
        </div>
        <div>
          <label>Costo:</label>
          <input
            type="number"
            value={costo}
            onChange={(e) => setCosto(e.target.value)}
          />
        </div>
        <button type="submit">Agregar Reparación</button>
      </form>
    </div>
  );
};

export default AgregarReparacion;
