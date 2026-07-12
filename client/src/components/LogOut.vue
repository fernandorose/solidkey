<script setup lang="ts">
import { useRouter } from "vue-router";
import { useAuth } from "../composables/useAuth";

const { logout } = useAuth();
const router = useRouter();

const handleLogout = () => {
  logout();
  router.push("/login");
};
</script>

<template>
  <button @click="handleLogout">Logout</button>
</template>
