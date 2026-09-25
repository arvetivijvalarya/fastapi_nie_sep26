import { useState } from 'react';
import api from './api';

function Register() {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [bloodType, setBloodType] = useState('');
  const [contact, setContact] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Call your FastAPI donor registration endpoint
      await api.post('/donors', {
        name,
        age: parseInt(age),
        blood_type: bloodType,
        contact
      });
      setMessage('Donor registered successfully!');
      setName('');
      setAge('');
      setBloodType('');
      setContact('');
    } catch (err) {
      setMessage('Registration failed. Please check your input.');
    }
  };

  return (
    <div>
      <h2>Donor Registration</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input 
            type="text" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            required 
          />
        </div>
        <div>
          <label>Age:</label>
          <input 
            type="number" 
            value={age} 
            onChange={(e) => setAge(e.target.value)} 
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
          <label>Contact:</label>
          <input 
            type="text" 
            value={contact} 
            onChange={(e) => setContact(e.target.value)} 
            required 
          />
        </div>
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Register;
