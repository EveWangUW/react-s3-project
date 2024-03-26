import React from 'react';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

const HelloWorld: React.FC = () => {
  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom>
        Hello, World!
      </Typography>
      <Typography variant="body1">
        This is a basic hello world frontend using Material-UI (mui) library.
      </Typography>
      <Button variant="contained" color="primary">
        Click me!
      </Button>
    </Container>
  );
};

export default HelloWorld;
