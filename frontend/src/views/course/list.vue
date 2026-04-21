<template>
  <div class="courses-page">
    <header class="header">
      <div class="container">
        <div class="logo">Study Intoclaw</div>
        <nav class="nav">
          <router-link to="/" class="nav-item">首页</router-link>
          <router-link to="/courses" class="nav-item">课程</router-link>
          <template v-if="userStore.isLoggedIn">
            <router-link to="/user/profile" class="nav-item">个人中心</router-link>
            <router-link to="/user/courses" class="nav-item">我的课程</router-link>
            <a href="#" class="nav-item" @click.prevent="handleLogout">退出</a>
          </template>
          <template v-else>
            <router-link to="/login" class="nav-item">登录</router-link>
            <router-link to="/register" class="nav-item">注册</router-link>
          </template>
        </nav>
      </div>
    </header>

    <main class="main">
      <div class="container">
        <div class="page-header">
          <h1>课程列表</h1>
          <div class="search-box">
            <input type="text" placeholder="搜索课程..." v-model="searchKeyword" />
            <button @click="search">搜索</button>
          </div>
        </div>
        
        <div v-if="courseStore.isLoading" class="loading">加载中...</div>
        <div v-else-if="courseStore.error" class="error">{{ courseStore.error }}</div>
        
        <div v-else class="courses-grid">
          <div 
            v-for="course in courses" 
            :key="course.id" 
            class="course-card"
            @click="goToCourse(course.slug)"
          >
            <div class="course-image">
              <img :src="course.thumbnail || 'https://via.placeholder.com/300x200'" :alt="course.title" />
            </div>
            <div class="course-info">
              <h3>{{ course.title }}</h3>
              <p class="course-desc">{{ course.description }}</p>
              <div class="course-meta">
                <span class="price">¥{{ course.price }}</span>
                <span class="students">{{ course.students }} 学员</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="footer">
      <div class="container">
        <p>&copy; 2026 Study Intoclaw. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/modules/user'
import { useCourseStore } from '@/stores/modules/course'
import type { Course } from '@/api/types'

const router = useRouter()
const userStore = useUserStore()
const courseStore = useCourseStore()

const searchKeyword = ref('')

const courses = computed(() => {
  if (!searchKeyword.value) {
    return courseStore.courses
  }
  return courseStore.courses.filter(course => 
    course.title.includes(searchKeyword.value) || 
    course.description.includes(searchKeyword.value)
  )
})

onMounted(async () => {
  await courseStore.fetchCourses()
})

const goToCourse = (slug: string) => {
  router.push(`/course/${slug}`)
}

const search = () => {
  // 搜索逻辑已在 computed 中处理
}

const handleLogout = async () => {
  await userStore.logout()
  router.push('/')
}
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables.scss';

.courses-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: $bg-color;
}

.header {
  background: #fff;
  box-shadow: $shadow-sm;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
}

.logo {
  font-size: 20px;
  font-weight: bold;
  color: $primary-color;
}

.nav {
  display: flex;
  gap: 20px;
}

.nav-item {
  color: $text-color-secondary;
  transition: color 0.3s;
  &:hover,
  &.router-link-active {
    color: $primary-color;
  }
}

.main {
  flex: 1;
  padding: 40px 0;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.page-header h1 {
  color: $text-color;
}

.search-box {
  display: flex;
  gap: 10px;
  input {
    padding: 8px 12px;
    border: 1px solid $border-color;
    border-radius: $border-radius-base;
    width: 200px;
  }
  button {
    padding: 8px 16px;
    background: $primary-color;
    color: #fff;
    border: none;
    border-radius: $border-radius-base;
    cursor: pointer;
  }
}

.loading,
.error {
  text-align: center;
  padding: 40px;
  color: $text-color-light;
}

.error {
  color: $danger-color;
}

.courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

.course-card {
  background: #fff;
  border-radius: $border-radius-lg;
  overflow: hidden;
  box-shadow: $shadow-base;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
  &:hover {
    transform: translateY(-5px);
    box-shadow: $shadow-lg;
  }
}

.course-image {
  width: 100%;
  height: 160px;
  overflow: hidden;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.course-info {
  padding: 15px;
}

.course-info h3 {
  margin-bottom: 10px;
  color: $text-color;
  font-size: 16px;
}

.course-desc {
  color: $text-color-light;
  font-size: 14px;
  margin-bottom: 15px;
  line-height: 1.5;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.course-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  color: $danger-color;
  font-size: 18px;
  font-weight: bold;
}

.students {
  color: $text-color-light;
  font-size: 12px;
}

.footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-top: auto;
}

@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }
  
  .search-box {
    width: 100%;
    input {
      flex: 1;
    }
  }
}
</style>