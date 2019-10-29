import axios from 'axios';

export async function call(store) {
  const payload = {
    intervalSize: store.intervalSize,
    xileSize: store.xileSize,
    sampleSize: store.sampleSize,
    expression: store.expression,
    variables: store.variables,
  };
  try {
    const response = await axios.post('/generate-data', payload);
    return response.data;
  } catch (e) {
    throw e.response.data.error;
  }
};