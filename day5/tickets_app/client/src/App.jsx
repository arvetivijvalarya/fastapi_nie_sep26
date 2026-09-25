import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import TicketForm from './TicketForm';
import TicketList from './TicketList';

function Navigation() {
  return (
    <nav>
      <ul>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/register">Register Donor</Link></li>
        <li><Link to="/request">Create Request</Link></li>
        <li><Link to="/requests">View Requests</Link></li>
      </ul>
    </nav>
  );
}

function App() {
  return (
    <Router>
      <div>
        <h1>Blood Bank System</h1>
        <Navigation />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/request" element={<TicketForm />} />
          <Route path="/requests" element={<TicketList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
