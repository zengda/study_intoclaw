<template>
  <div class="error-404">
    <h1>404</h1>
    <p>页面不存在</p>
    <router-link to="/" class="btn-primary">返回首页</router-link>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.error-404 {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.error-404 h1 {
  font-size: 120px;
  margin-bottom: 20px;
  color: #667eea;
}

.error-404 p {
  font-size: 24px;
  margin-bottom: 30px;
  color: #666;
}

.btn-primary {
  padding: 12px 32px;
  background: #667eea;
  color: #fff;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s;
}

.btn-primary:hover {
  background: #764ba2;
  transform: translateY(-2px);
}
</style>