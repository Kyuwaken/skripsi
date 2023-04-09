import axios from "axios";

const getAPI = axios.create({
  baseURL: "http://localhost:8000/",
  timeout: 170000,
  withCredentials: true
});

export { getAPI };
