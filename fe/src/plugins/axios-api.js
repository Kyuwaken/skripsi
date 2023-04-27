import axios from "axios";

const getAPI = axios.create({
  baseURL: "https://skripsi-production.up.railway.app/",
  // baseURL: "http://localhost:8000/",
  timeout: 170000,
  withCredentials: true
});

export { getAPI };
