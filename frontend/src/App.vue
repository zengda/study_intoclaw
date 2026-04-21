<template>
  <div id="app">
    <TheHeader />
    <router-view />
  </div>
</template>

<script setup lang="ts">
import TheHeader from '@/components/layout/TheHeader.vue'
</script>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

#app > .router-view {
  flex: 1;
}
</style>
