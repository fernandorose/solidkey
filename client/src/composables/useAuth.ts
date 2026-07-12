import { ref } from "vue";

const user = ref<{
  id: string;
  username: string;
  email: string;
  role: string;
} | null>(null);

export const useAuth = () => {
  const login = async (username: string, password: string) => {
    const res = await fetch("http://localhost:8000/api/users/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (!res.ok) {
      user.value = null;
      return false;
    }

    const data = await res.json();
    localStorage.setItem("token", data.token);
    user.value = data.user;
    return true;
  };

  const validateToken = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      user.value = null;
      return false;
    }
    const res = await fetch("http://localhost:8000/api/users/me", {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!res.ok) {
      user.value = null;
      return false;
    }

    user.value = await res.json();
    return true;
  };
  const logout = () => {
    localStorage.removeItem("token");
    user.value = null;
  };

  return {
    user,
    login,
    validateToken,
    logout,
  };
};
