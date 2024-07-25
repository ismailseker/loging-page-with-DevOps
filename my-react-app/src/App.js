// import React from 'react';
// import { Container, CssBaseline, AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Login from './components/login';
// import Register from './components/register';
// import Admin from './components/admin';
// import UserManagement from './components/usermanagement';

// function App() {
//   return (
//     <Router>
//       <CssBaseline />
//       <AppBar position="static">
//         <Toolbar>
//           <Typography variant="h6" sx={{ flexGrow: 1 }}>
//             My App
//           </Typography>
//           <Button color="inherit" href="/login">Login</Button>
//           <Button color="inherit" href="/register">Register</Button>
//           <Button color="inherit" href="/admin">Admin</Button>
//           <Button color="inherit" href="/user-management">User Management</Button>
//         </Toolbar>
//       </AppBar>
//       <Container sx={{ marginTop: 4 }}>
//         <Routes>
//           <Route path="/login" element={<Login />} />
//           <Route path="/register" element={<Register />} />
//           <Route path="/admin" element={<Admin />} />
//           <Route path="/user-management" element={<UserManagement />} />
//         </Routes>
//       </Container>
//     </Router>
//   );
// }

// export default App;
import React, { useState, useEffect } from 'react';
import { Container, CssBaseline, AppBar, Toolbar, Typography, Button } from '@mui/material';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Login from './components/login';
import Register from './components/register';
import Admin from './components/admin';
import UserManagement from './components/usermanagement';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  

  useEffect(() => {
    // Oturum kontrolü yap
    axios.get('http://localhost:5000/home', { withCredentials: true })
      .then(response => {
        if (response.data.username) {
          setLoggedIn(true);
          setUsername(response.data.username);
        }
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const handleLogout = () => {
    axios.get('http://localhost:5000/logout', { withCredentials: true })
      .then(response => {
        setLoggedIn(false);
        setUsername('');
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <Router>
      <CssBaseline />
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            My App
          </Typography>
          {!loggedIn ? (
            <>
              <Button color="inherit" href="/login">Login</Button>
              <Button color="inherit" href="/register">Register</Button>
            </>
          ) : (
            <>
              <Typography variant="h6" sx={{ flexGrow: 1 }}>
                Welcome, {username}
              </Typography>
              <Button color="inherit" href="/admin">Admin</Button>
              <Button color="inherit" href="/user-management">User Management</Button>
              <Button color="inherit" onClick={handleLogout}>Logout</Button>
            </>
          )}
        </Toolbar>
      </AppBar>
      <Container sx={{ marginTop: 4 }}>
        <Routes>
          <Route path="/login" element={<Login setLoggedIn={setLoggedIn} setUsername={setUsername} />} />
          <Route path="/register" element={<Register />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/user-management" element={<UserManagement />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
