<script setup lang="ts">
import { useAuth } from "../composables/useAuth";
import "../styles/sidebar.css";

const { user } = useAuth();
</script>

<template>
  <nav class="sidebar">
    <section class="sidebar-header">
      <div>
        <h1>SolidKey</h1>
      </div>
      <div class="user-info">
        <h3>{{ user?.username }}</h3>
        <span class="role" v-if="user?.role === 'admin'">Admin</span>
        <!-- <LogOut /> -->
      </div>
    </section>
  </nav>
</template>
