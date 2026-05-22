import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const [patients, setPatients] = useState([]);
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const fetchPatients = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/patients", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setPatients(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    if (!token) {
      navigate("/");
    } else {
      fetchPatients();
    }
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Hospital Dashboard</h1>

      <button onClick={logout}>Logout</button>

      <table border="1" style={{ marginTop: 20 }}>
        <tr>
          <th>ID</th>
          <th>Symptoms</th>
          <th>Disease</th>
        </tr>

        {patients.map((p) => (
          <tr key={p.id}>
            <td>{p.id}</td>
            <td>{p.symptoms}</td>
            <td>{p.disease}</td>
          </tr>
        ))}
      </table>
    </div>
  );
}

export default Dashboard;