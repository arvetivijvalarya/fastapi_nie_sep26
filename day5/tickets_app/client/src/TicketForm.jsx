import { useState } from 'react';
import api from './api';

function TicketForm() {
  const [hospitalName, setHospitalName] = useState('');
  const [bloodType, setBloodType] = useState('');
  const [units, setUnits] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/requests', {
        hospital_name: hospitalName,
        blood_type: bloodType,
        units: parseInt(units),
        status: "Pending"
      });
      setMessage('Blood request created successfully!');
      setHospitalName('');
      setBloodType('');
      setUnits('');
    } catch (err) {
      setMessage('Failed to create request.');
    }
  };

  return (
    <div>
      <h2>Create Blood Request</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Hospital Name:</label>
          <input 
            type="text" 
            value={hospitalName} 
            onChange={(e) => setHospitalName(e.target.value)} 
            required 
          />
        </div>
        <div>
          <label>Blood Type:</label>
          <input 
            type="text" 
            value={bloodType} 
            onChange={(e) => setBloodType(e.target.value)} 
            placeholder="e.g. O+" 
            required 
          />
        </div>
        <div>
          <label>Units:</label>
          <input 
            type="number" 
            value={units} 
            onChange={(e) => setUnits(e.target.value)} 
            required 
          />
        </div>
        <button type="submit">Submit Request</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default TicketForm;
