<script setup lang="ts">
import { useAuth } from "../composables/useAuth";

const { user } = useAuth();
</script>

<template>
  <section>
    <h1>SolidKey</h1>
    <!-- <button @click="validateToken">Validar token</button> -->
    <pre v-if="user">Autenticado</pre>
    <p v-else>No autenticado</p>
  </section>
</template>
