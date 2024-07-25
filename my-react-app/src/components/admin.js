
import React from 'react';
import { Typography, Box, Paper, Grid, Button, Card, CardContent } from '@mui/material';
import { Link } from 'react-router-dom';

function Admin() {
  return (
    <Box sx={{ padding: 4, maxWidth: 1200, margin: 'auto' }}>
      <Typography variant="h4" gutterBottom>
        Admin Dashboard
      </Typography>

      <Grid container spacing={4}>
        {/* User Management Card */}
        <Grid item xs={12} sm={6} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">User Management</Typography>
              <Typography color="textSecondary" paragraph>
                Manage users, view their details, and perform administrative tasks.
              </Typography>
              <Link to="/user-management" style={{ textDecoration: 'none' }}>
                <Button variant="contained" color="primary" fullWidth>
                  Go to User Management
                </Button>
              </Link>
            </CardContent>
          </Card>
        </Grid>

        {/* Statistics Card */}
        <Grid item xs={12} sm={6} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Statistics</Typography>
              <Typography color="textSecondary" paragraph>
                View and analyze statistics related to users and system performance.
              </Typography>
              <Button variant="contained" color="secondary" fullWidth>
                View Statistics
              </Button>
            </CardContent>
          </Card>
        </Grid>

        {/* Settings Card */}
        <Grid item xs={12} sm={6} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Settings</Typography>
              <Typography color="textSecondary" paragraph>
                Configure system settings and preferences.
              </Typography>
              <Button variant="contained" color="info" fullWidth>
                Go to Settings
              </Button>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}

export default Admin;
