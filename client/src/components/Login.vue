<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuth } from "../composables/useAuth";

const { user, login } = useAuth();
const router = useRouter();

const username = ref("");
const password = ref("");
const error = ref("");

const handleLogin = async () => {
  error.value = "";
  const ok = await login(username.value, password.value);
  if (!ok) {
    error.value = "Usuario o contraseña incorrectos";
    return;
  }
  router.push("/");
};
</script>

<template>
  <section>
    <h1>Login</h1>
    <div>
      <input v-model="username" type="text" placeholder="Usuario" />
      <input v-model="password" type="password" placeholder="Contraseña" />
      <button @click="handleLogin">Entrar</button>
    </div>
    <p v-if="error">{{ error }}</p>
    <pre v-if="user">{{ user }}</pre>
  </section>
</template>
