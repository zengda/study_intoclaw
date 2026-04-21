<template>
  <header class="header">
    <div class="container">
      <div class="header-nav">
        <div class="logo">
          <img src="https://via.placeholder.com/120x40" alt="Study Intoclaw" @click="$router.push('/')" />
        </div>
        <nav class="nav">
          <router-link to="/" class="nav-item" :class="{ active: $route.path === '/' }">首页</router-link>
          <router-link to="/courses" class="nav-item">课程中心</router-link>
          <a href="#" class="nav-item">超级会员</a>
          <a href="#" class="nav-item">工具</a>
          <a href="#" class="nav-item">自学路线</a>
          <a href="#" class="nav-item">一对一辅导</a>
        </nav>
        <div class="header-right">
          <div class="header-search">
            <input type="text" placeholder="请输入搜索内容" v-model="searchQuery" @keyup.enter="handleSearch" />
            <button @click="handleSearch">搜索</button>
          </div>
          <div class="header-buttons">
            <a href="#" class="btn-activate">激活</a>
            <a href="#" class="btn-cloud">云服务器</a>
            <router-link to="/login" class="btn-login">登录</router-link>
            <router-link to="/register" class="btn-register">注册</router-link>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const searchQuery = ref('')

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    console.log('搜索:', searchQuery.value)
    router.push({ path: '/courses', query: { search: searchQuery.value } })
  }
}
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables.scss';

.header {
  background: #fff;
  box-shadow: $shadow-sm;
  position: sticky;
  top: 0;
  z-index: 100;
}

.container {
  width: 100%;
  max-width: 100%;
  padding: 0 20px;
}

.header-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  max-width: 100%;
  padding: 25px 20px;
}

.logo {
  cursor: pointer;
  flex-shrink: 0;
  img {
    height: 40px;
  }
}

.nav {
  display: flex;
  gap: 16px;
  flex: 1;
  justify-content: center;
  .nav-item {
    color: $text-color-secondary;
    font-size: 15px;
    font-weight: 500;
    text-decoration: none;
    transition: color 0.3s;
    padding: 5px 10px;
    &:hover,
    &.active {
      color: $primary-color;
    }
  }
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

.header-search {
  display: flex;
  input {
    padding: 6px 12px;
    border: 1px solid $border-color;
    border-radius: $border-radius-base 0 0 $border-radius-base;
    font-size: 14px;
    width: 160px;
    &:focus {
      outline: none;
      border-color: $primary-color;
    }
  }
  button {
    padding: 0 12px;
    background: $primary-color;
    color: #fff;
    border: none;
    border-radius: 0 $border-radius-base $border-radius-base 0;
    cursor: pointer;
    font-size: 14px;
    transition: background 0.3s;
    &:hover {
      background: darken($primary-color, 10%);
    }
  }
}

.header-buttons {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-activate {
  padding: 6px 12px;
  background: #ff6b6b;
  color: #fff;
  border-radius: $border-radius-base;
  font-size: 14px;
  text-decoration: none;
  transition: all 0.3s;
  &:hover {
    background: darken(#ff6b6b, 10%);
  }
}

.btn-cloud {
  padding: 6px 12px;
  background: #4ecdc4;
  color: #fff;
  border-radius: $border-radius-base;
  font-size: 14px;
  text-decoration: none;
  transition: all 0.3s;
  &:hover {
    background: darken(#4ecdc4, 10%);
  }
}

.btn-login {
  padding: 6px 12px;
  background: #fff;
  color: $text-color-secondary;
  border-radius: $border-radius-base;
  font-size: 14px;
  text-decoration: none;
  transition: all 0.3s;
  border: 1px solid $border-color;
  &:hover {
    color: $primary-color;
    border-color: $primary-color;
  }
}

.btn-register {
  padding: 6px 12px;
  background: $primary-color;
  color: #fff;
  border-radius: $border-radius-base;
  font-size: 14px;
  text-decoration: none;
  transition: all 0.3s;
  &:hover {
    background: darken($primary-color, 10%);
  }
}
</style>
