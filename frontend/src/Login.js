import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/login", {
        username,
        password,
      });

      if (res.data.access_token) {
        localStorage.setItem("token", res.data.access_token);
        navigate("/dashboard");
      } else {
        alert("Invalid login");
      }
    } catch (err) {
      alert("Server error");
    }
  };

  return (
    <div style={{ padding: 50 }}>
      <h1>Doctor Login</h1>

      <input
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />
      <br /><br />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <br /><br />

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;