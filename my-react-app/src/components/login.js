
// import React, { useState } from 'react';
// import { TextField, Button, Typography, Box, Paper } from '@mui/material';
// import axios from 'axios';

// function Login() {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');
//   const [msg, setMsg] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post('http://localhost:5000/login', { username, password });
//       if (response.status === 200) {
//         window.location.href = '/home';
//       } else {
//         setMsg('Incorrect username/password. Try Again!');
//       }
//     } catch (error) {
//       setMsg('Error logging in');
//     }
//   };

//   return (
//     <Box component={Paper} elevation={3} sx={{ padding: 4, maxWidth: 400, margin: 'auto', marginTop: 4 }}>
//       <Typography variant="h5" gutterBottom>Login</Typography>
//       {msg && <Typography color="error">{msg}</Typography>}
//       <form onSubmit={handleSubmit}>
//         <TextField
//           label="Username"
//           variant="outlined"
//           fullWidth
//           margin="normal"
//           value={username}
//           onChange={(e) => setUsername(e.target.value)}
//         />
//         <TextField
//           label="Password"
//           type="password"
//           variant="outlined"
//           fullWidth
//           margin="normal"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//         />
//         <Button type="submit" variant="contained" color="primary" fullWidth>
//           Login
//         </Button>
//       </form>
//     </Box>
//   );
// }

// export default Login;
import React, { useState } from 'react';
import { TextField, Button, Typography, Box, Paper } from '@mui/material';
import axios from 'axios';

function Login({ setLoggedIn, setUsername }) {
  const [username, setUsernameLocal] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/login', { username, password }, { withCredentials: true });
      if (response.status === 200) {
        setLoggedIn(true);
        setUsername(username);
        window.location.href = '/home';
      } else {
        setMsg('Incorrect username/password. Try Again!');
      }
    } catch (error) {
      setMsg('Error logging in');
    }
  };

  return (
    <Box component={Paper} elevation={3} sx={{ padding: 4, maxWidth: 400, margin: 'auto', marginTop: 4 }}>
      <Typography variant="h5" gutterBottom>Login</Typography>
      {msg && <Typography color="error">{msg}</Typography>}
      <form onSubmit={handleSubmit}>
        <TextField
          label="Username"
          variant="outlined"
          fullWidth
          margin="normal"
          value={username}
          onChange={(e) => setUsernameLocal(e.target.value)}
        />
        <TextField
          label="Password"
          type="password"
          variant="outlined"
          fullWidth
          margin="normal"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Login
        </Button>
      </form>
    </Box>
  );
}

export default Login;
