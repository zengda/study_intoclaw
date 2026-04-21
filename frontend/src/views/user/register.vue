<template>
  <div class="register-page">
    <div class="register-card">
      <h1>注册</h1>
      <form @submit.prevent="handleRegister">
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
          <label for="nickName">昵称</label>
          <input 
            id="nickName"
            v-model="form.nickName" 
            type="text" 
            placeholder="请输入昵称"
            required
          />
        </div>
        <div class="form-group">
          <label for="email">邮箱</label>
          <input 
            id="email"
            v-model="form.email" 
            type="email" 
            placeholder="请输入邮箱"
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
        <div class="form-group">
          <label for="confirmPassword">确认密码</label>
          <input 
            id="confirmPassword"
            v-model="form.confirmPassword" 
            type="password" 
            placeholder="请再次输入密码"
            required
          />
        </div>
        <div v-if="error" class="error-message">{{ error }}</div>
        <div v-if="success" class="success-message">{{ success }}</div>
        <button type="submit" class="btn-submit" :disabled="userStore.isLoading">
          {{ userStore.isLoading ? '注册中...' : '注册' }}
        </button>
      </form>
      <div class="form-footer">
        已有账号？<router-link to="/login">立即登录</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/modules/user'

const router = useRouter()
const userStore = useUserStore()

const form = ref({
  phone: '',
  nickName: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const error = ref('')
const success = ref('')

const handleRegister = async () => {
  error.value = ''
  success.value = ''
  
  if (form.value.password !== form.value.confirmPassword) {
    error.value = '两次输入的密码不一致'
    return
  }
  
  const result = await userStore.register({
    phone: form.value.phone,
    nickName: form.value.nickName,
    email: form.value.email,
    password: form.value.password
  })
  
  if (result.success) {
    success.value = '注册成功！即将跳转到登录页面...'
    setTimeout(() => {
      router.push('/login')
    }, 1500)
  } else {
    error.value = userStore.error || '注册失败'
  }
}
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables.scss';

.register-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.register-card {
  background: #fff;
  padding: 40px;
  border-radius: $border-radius-lg;
  box-shadow: $shadow-lg;
  width: 100%;
  max-width: 400px;
}

.register-card h1 {
  text-align: center;
  margin-bottom: 30px;
  color: $text-color;
}

.form-group {
  margin-bottom: 15px;
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

.success-message {
  color: $success-color;
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