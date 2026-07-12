<script setup lang="ts">
import { onMounted } from "vue";
import { useAuth } from "./composables/useAuth";

const { validateToken } = useAuth();

onMounted(() => {
  validateToken();
});
</script>

<template>
  <router-view />
</template>
