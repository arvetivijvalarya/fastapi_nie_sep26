import { useEffect, useState } from 'react';
import api from './api';

function TicketList() {
  const [requests, setRequests] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchRequests = async () => {
      try {
        const res = await api.get('/requests');
        setRequests(res.data);
      } catch (err) {
        setError('Failed to load requests.');
      }
    };
    fetchRequests();
  }, []);

  return (
    <div>
      <h2>Blood Requests</h2>
      {error && <p>{error}</p>}
      <ul>
        {requests.map((req) => (
          <li key={req.id}>
            <strong>{req.hospital_name}</strong> — {req.blood_type}, {req.units} units ({req.status})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TicketList;
