<template>
  <div class="login-page">
    <div class="login-card">
      <h1>登录</h1>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="phone">手机号</label>
          <input 
            id="phone"
            v-model="form.phone" 
            type="text" 
            placeholder="请输入手机号"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input 
            id="password"
            v-model="form.password" 
            type="password" 
            placeholder="请输入密码"
            required
          />
        </div>
        <div v-if="userStore.error" class="error-message">{{ userStore.error }}</div>
        <button type="submit" class="btn-submit" :disabled="userStore.isLoading">
          {{ userStore.isLoading ? '登录中...' : '登录' }}
        </button>
      </form>
      <div class="form-footer">
        还没有账号？<router-link to="/register">立即注册</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/modules/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const form = ref({
  phone: '',
  password: ''
})

const handleLogin = async () => {
  const result = await userStore.login(form.value.phone, form.value.password)
  
  if (result.success) {
    const redirect = route.query.redirect as string || '/'
    router.push(redirect)
  }
}
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables.scss';

.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
  background: #fff;
  padding: 40px;
  border-radius: $border-radius-lg;
  box-shadow: $shadow-lg;
  width: 100%;
  max-width: 400px;
}

.login-card h1 {
  text-align: center;
  margin-bottom: 30px;
  color: $text-color;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: $text-color-secondary;
  font-size: 14px;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid $border-color;
  border-radius: $border-radius-base;
  font-size: 14px;
  transition: border-color 0.3s;
  &:focus {
    outline: none;
    border-color: $primary-color;
  }
}

.error-message {
  color: $danger-color;
  font-size: 14px;
  margin-bottom: 15px;
  text-align: center;
}

.btn-submit {
  width: 100%;
  padding: 12px;
  background: $primary-color;
  color: #fff;
  border: none;
  border-radius: $border-radius-base;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
  &:hover:not(:disabled) {
    background: lighten($primary-color, 10%);
  }
  &:disabled {
    background: lighten($primary-color, 20%);
    cursor: not-allowed;
  }
}

.form-footer {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: $text-color-secondary;
  a {
    color: $primary-color;
    &:hover {
      text-decoration: underline;
    }
  }
}
</style>