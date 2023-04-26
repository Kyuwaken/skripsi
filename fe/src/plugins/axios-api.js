import axios from "axios";

const getAPI = axios.create({
  baseURL: "https://backend-skripsi-production.up.railway.app/",
  timeout: 170000,
  withCredentials: true
});

export { getAPI };
