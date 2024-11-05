// src/UploadRecipe.js

import React, { useState } from 'react';
import axios from 'axios';
import { useForm } from 'react-hook-form';

const UploadRecipe = () => {
  const { register, handleSubmit, reset } = useForm({
    defaultValues: {
      save_to_drive: true,
      save_locally: true
    }
  });
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const onSubmit = async (data) => {
    setResponse(null);
    setError(null);

    const formData = new FormData();
    if (data.text) {
      formData.append('text', data.text);
    }
    if (data.file && data.file[0]) {
      formData.append('file', data.file[0]);
    }
    formData.append('save_to_drive', data.save_to_drive);
    formData.append('save_locally', data.save_locally);

    try {
      const res = await axios.post('http://localhost:8000/upload-recipe/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponse(res.data);
      reset({
        text: '',
        file: null,
        save_to_drive: true,
        save_locally: true
      });
    } catch (err) {
      if (err.response && err.response.data) {
        setError(err.response.data.detail);
      } else {
        setError('An unexpected error occurred.');
      }
    }
  };

  return (
    <div style={styles.container}>
      <h2>Upload Recipe</h2>
      <form onSubmit={handleSubmit(onSubmit)} style={styles.form}>
        <div style={styles.field}>
          <label>Recipe Text:</label>
          <textarea {...register('text')} placeholder="Enter recipe text here..." style={styles.textarea}></textarea>
        </div>
        <div style={styles.field}>
          <label>Or Upload PDF:</label>
          <input type="file" {...register('file')} accept="application/pdf" />
        </div>
        <div style={styles.field}>
          <label>Save Options:</label>
          <div style={styles.checkboxGroup}>
            <label>
              <input type="checkbox" {...register('save_to_drive')} />
              Save to Google Drive
            </label>
            <label>
              <input type="checkbox" {...register('save_locally')} />
              Save Locally
            </label>
          </div>
        </div>
        <button type="submit" style={styles.button}>Submit</button>
      </form>

      {response && (
        <div style={styles.success}>
          <h3>{response.message}</h3>
          <p><strong>Category:</strong> {response.category}</p>
          {response.google_drive_file_id && (
            <p><strong>Google Drive File ID:</strong> {response.google_drive_file_id}</p>
          )}
          {response.local_file_path && (
            <p><strong>Local File Path:</strong> {response.local_file_path}</p>
          )}
        </div>
      )}

      {error && (
        <div style={styles.error}>
          <h3>Error</h3>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

const styles = {
  container: {
    maxWidth: '600px',
    margin: '50px auto',
    padding: '20px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    fontFamily: 'Arial, sans-serif',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
  },
  field: {
    marginBottom: '15px',
  },
  textarea: {
    width: '100%',
    height: '100px',
    padding: '10px',
    fontSize: '16px',
  },
  checkboxGroup: {
    display: 'flex',
    flexDirection: 'column',
    gap: '10px',
    marginTop: '5px',
  },
  button: {
    padding: '10px',
    fontSize: '16px',
    backgroundColor: '#28a745',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
  },
  success: {
    marginTop: '20px',
    padding: '15px',
    backgroundColor: '#d4edda',
    border: '1px solid #c3e6cb',
    borderRadius: '4px',
    color: '#155724',
  },
  error: {
    marginTop: '20px',
    padding: '15px',
    backgroundColor: '#f8d7da',
    border: '1px solid #f5c6cb',
    borderRadius: '4px',
    color: '#721c24',
  },
};

export default UploadRecipe;
