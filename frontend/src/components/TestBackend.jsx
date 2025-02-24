import React, { useState, useEffect } from 'react';

const TestBackend = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/hello')
            .then((res) => res.json())
            .then((data) => setMessage(data.message))
            .catch((error) => console.error('Error:', error));
    }, []);

    return <div>Backend says: {message}</div>;
};

export default TestBackend;
