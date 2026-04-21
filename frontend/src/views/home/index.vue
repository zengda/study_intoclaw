<template>
<div class="home">
    <main class="main">
      <!-- 主要内容区域 -->
      <section class="main-content">
        <div class="container">
          <div class="content-wrapper">
            <!-- 左侧分类列表 -->
            <div class="left-sidebar">
              <div 
                v-for="category in categories" 
                :key="category.id"
                class="category-item"
                :class="{ active: activeCategory === category.id }"
                @click="toggleCategory(category.id)"
              >
                <span class="category-name">{{ category.name }}</span>
                <span class="category-arrow" :class="{ rotated: activeCategory === category.id }">></span>
              </div>
            </div>
            
            <!-- 中间课程推广banner -->
            <div class="center-content">
              <div class="promotion-banner">
                <div class="banner-tag">面试最强一课 | 冲刺金三银四</div>
                <div class="banner-content">
                  <h3>独孤求败-小滴云架构大课十八式</h3>
                  <p>+多领域项目实战</p>
                  <div class="banner-description">
                    <p>【用最少的时间，产生最大的价值】最体系化学习最核心技术！</p>
                    <p>【最强面大课】项目实践和理论比例7:3，超多实践案例远大于理论，拒绝PPT论练师！</p>
                  </div>
                  <div class="banner-price">
                    <span class="original-price">狂欢价: ¥7799</span>
                    <span class="target-level">对标阿里P7~P8架构师能力</span>
                  </div>
                  <div class="banner-footer">
                    <span class="season-tag">金三银四</span>
                    <span class="season-desc">跳槽涨薪季</span>
                  </div>
                </div>
                <div class="banner-controls">
                  <button class="prev-btn">‹</button>
                  <button class="next-btn">›</button>
                </div>
                <div class="banner-pagination">
                  <span class="dot active"></span>
                  <span class="dot"></span>
                  <span class="dot"></span>
                  <span class="dot"></span>
                  <span class="dot"></span>
                </div>
                <div class="banner-status">已完结</div>
              </div>
              
              <!-- 快捷入口 -->
              <div class="quick-entries">
                <div class="entry-item">
                  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=frontend%20one%20on%20one%20training%20icon&image_size=square" alt="前端一对一" />
                  <span>前端一对一</span>
                </div>
                <div class="entry-item">
                  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=backend%20one%20on%20one%20training%20icon&image_size=square" alt="后端一对一" />
                  <span>后端一对一</span>
                </div>
                <div class="entry-item">
                  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=big%20data%20processing%20course%20icon&image_size=square" alt="海量数据处理" />
                  <span>海量数据处理</span>
                </div>
                <div class="entry-item">
                  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=cloud%20architecture%20course%20icon&image_size=square" alt="云架构大课十八式" />
                  <span>云架构大课十八式</span>
                </div>
                <div class="entry-item">
                  <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=permanent%20member%20icon&image_size=square" alt="永久会员" />
                  <span>永久会员</span>
                </div>
              </div>
            </div>
            
            <!-- 右侧功能区 -->
            <div class="right-sidebar">
              <div class="login-card">
                <div class="login-header">
                  <h4>新人专享福利</h4>
                  <span class="bonus">200元</span>
                </div>
                <button class="login-btn">登录/注册</button>
                <div class="danmaku-control">
                  <span>弹幕</span>
                  <label class="switch">
                    <input type="checkbox" checked>
                    <span class="slider"></span>
                  </label>
                </div>
              </div>
              
              <div class="ai-assistant">
                <div class="assistant-header">
                  <span>小滴AI助手</span>
                </div>
                <div class="assistant-content">
                  <p>有任何问题，随时咨询我哦！</p>
                </div>
              </div>
              
              <div class="side-buttons">
                <button class="side-btn contact-btn">
                  <span>联系讲师</span>
                </button>
                <button class="side-btn free-btn">
                  <span>免费试学</span>
                </button>
                <button class="side-btn help-btn">
                  <span>帮助中心</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h3>关于我们</h3>
            <ul>
              <li><a href="#">公司简介</a></li>
              <li><a href="#">联系方式</a></li>
              <li><a href="#">加入我们</a></li>
              <li><a href="#">隐私政策</a></li>
            </ul>
          </div>
          <div class="footer-section">
            <h3>学习资源</h3>
            <ul>
              <li><a href="#">课程中心</a></li>
              <li><a href="#">学习路径</a></li>
              <li><a href="#">技术博客</a></li>
              <li><a href="#">常见问题</a></li>
            </ul>
          </div>
          <div class="footer-section">
            <h3>服务支持</h3>
            <ul>
              <li><a href="#">帮助中心</a></li>
              <li><a href="#">在线客服</a></li>
              <li><a href="#">意见反馈</a></li>
              <li><a href="#">退款政策</a></li>
            </ul>
          </div>
          <div class="footer-section">
            <h3>关注我们</h3>
            <div class="footer-social">
              <a href="#" class="social-icon">微信</a>
              <a href="#" class="social-icon">微博</a>
              <a href="#" class="social-icon">GitHub</a>
              <a href="#" class="social-icon">知乎</a>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2026 Study Intoclaw. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/modules/user'
import { useCourseStore } from '@/stores/modules/course'
import type { Course } from '@/api/types'

const router = useRouter()
const userStore = useUserStore()
const courseStore = useCourseStore()

const courses = ref<Course[]>([])

// 分类数据
const categories = ref([
  { id: 1, name: '后端 | 架构' },
  { id: 2, name: '前端 | 全栈' },
  { id: 3, name: '测试 | 测开' },
  { id: 4, name: '运维 | 容器' },
  { id: 5, name: '架构 | 管理' },
  { id: 6, name: '算法人工智能' },
  { id: 7, name: '大数据' }
])

// 激活的分类
const activeCategory = ref<number | null>(null)

// 标签数据
const tagsData = {
  1: [
    { id: 101, name: 'Java', size: 18 },
    { id: 102, name: 'Spring Boot', size: 16 },
    { id: 103, name: 'MySQL', size: 14 },
    { id: 104, name: 'Redis', size: 15 },
    { id: 105, name: 'Docker', size: 14 },
    { id: 106, name: 'Kubernetes', size: 16 },
    { id: 107, name: '微服务', size: 17 },
    { id: 108, name: '分布式', size: 15 },
    { id: 109, name: '高并发', size: 14 },
    { id: 110, name: 'Spring Cloud', size: 16 }
  ],
  2: [
    { id: 201, name: 'JavaScript', size: 18 },
    { id: 202, name: 'React', size: 16 },
    { id: 203, name: 'Vue', size: 17 },
    { id: 204, name: 'TypeScript', size: 15 },
    { id: 205, name: 'HTML/CSS', size: 14 },
    { id: 206, name: 'Webpack', size: 14 },
    { id: 207, name: 'Node.js', size: 16 },
    { id: 208, name: 'Next.js', size: 15 },
    { id: 209, name: 'Vite', size: 14 },
    { id: 210, name: '前端工程化', size: 16 }
  ],
  3: [
    { id: 301, name: '自动化测试', size: 17 },
    { id: 302, name: '性能测试', size: 15 },
    { id: 303, name: '接口测试', size: 16 },
    { id: 304, name: 'UI测试', size: 14 },
    { id: 305, name: '测试框架', size: 15 },
    { id: 306, name: '测试工具', size: 14 },
    { id: 307, name: '测试用例', size: 14 },
    { id: 308, name: '测试策略', size: 15 },
    { id: 309, name: '持续集成', size: 16 },
    { id: 310, name: '测试自动化', size: 17 }
  ],
  4: [
    { id: 401, name: 'Linux', size: 18 },
    { id: 402, name: 'Shell', size: 15 },
    { id: 403, name: 'Nginx', size: 16 },
    { id: 404, name: 'Docker', size: 17 },
    { id: 405, name: 'Kubernetes', size: 16 },
    { id: 406, name: '监控', size: 14 },
    { id: 407, name: '日志', size: 14 },
    { id: 408, name: '安全', size: 15 },
    { id: 409, name: '备份', size: 14 },
    { id: 410, name: '灾备', size: 15 }
  ],
  5: [
    { id: 501, name: '系统架构', size: 18 },
    { id: 502, name: '技术管理', size: 16 },
    { id: 503, name: '项目管理', size: 15 },
    { id: 504, name: '团队管理', size: 14 },
    { id: 505, name: '架构设计', size: 17 },
    { id: 506, name: '技术选型', size: 15 },
    { id: 507, name: '性能优化', size: 16 },
    { id: 508, name: '安全架构', size: 14 },
    { id: 509, name: '可扩展性', size: 15 },
    { id: 510, name: '高可用性', size: 16 }
  ],
  6: [
    { id: 601, name: '算法', size: 18 },
    { id: 602, name: '数据结构', size: 16 },
    { id: 603, name: '机器学习', size: 17 },
    { id: 604, name: '深度学习', size: 16 },
    { id: 605, name: '神经网络', size: 15 },
    { id: 606, name: '自然语言处理', size: 16 },
    { id: 607, name: '计算机视觉', size: 15 },
    { id: 608, name: '强化学习', size: 14 },
    { id: 609, name: 'AI框架', size: 15 },
    { id: 610, name: '大数据分析', size: 16 }
  ],
  7: [
    { id: 701, name: 'Hadoop', size: 17 },
    { id: 702, name: 'Spark', size: 18 },
    { id: 703, name: 'Hive', size: 15 },
    { id: 704, name: 'Kafka', size: 16 },
    { id: 705, name: 'Flume', size: 14 },
    { id: 706, name: 'HBase', size: 15 },
    { id: 707, name: 'MapReduce', size: 14 },
    { id: 708, name: '数据仓库', size: 16 },
    { id: 709, name: '数据挖掘', size: 15 },
    { id: 710, name: '大数据架构', size: 17 }
  ]
}

// 当前标签
const currentTags = computed(() => {
  if (!activeCategory.value) return []
  return tagsData[activeCategory.value as keyof typeof tagsData] || []
})

// 切换分类
const toggleCategory = (categoryId: number) => {
  activeCategory.value = activeCategory.value === categoryId ? null : categoryId
}

onMounted(async () => {
  await courseStore.fetchCourses()
  courses.value = courseStore.courses
})

const goToCourse = (slug: string) => {
  router.push(`/course/${slug}`)
}

const handleLogout = async () => {
  await userStore.logout()
  router.push('/')
}
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables.scss';

.home {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: $bg-color;
}

.content-wrapper {
  display: flex;
  gap: 20px;
  align-items: flex-start;
  width: 100%;
  max-width: 100%;
  margin: 0 auto;
  padding: 0 20px;
}

/* 左侧分类列表 */
.left-sidebar {
  width: 180px;
  background: #f5f5f5;
  border-radius: $border-radius-lg;
  overflow: hidden;
  min-height: 400px;
}

.category-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 20px;
  cursor: pointer;
  transition: all 0.3s;
  border-bottom: 1px solid #e8e8e8;
  &:hover {
    background: #e8e8e8;
  }
  &.active {
    background: $primary-color;
    color: #fff;
  }
  &:last-child {
    border-bottom: none;
  }
}

.category-name {
  font-size: 14px;
  font-weight: 500;
}

.category-arrow {
  font-size: 12px;
  transition: transform 0.3s;
  &.rotated {
    transform: rotate(90deg);
  }
}

/* 中间内容区域 */
.center-content {
  flex: 1;
  min-width: 0;
  
}

/* 推广banner */
.promotion-banner {
  position: relative;
  background: linear-gradient(135deg, #f0f9ff 0%, #e6f7ff 100%);
  border-radius: $border-radius-lg;
  overflow: hidden;
  padding: 30px;
  margin-bottom: 20px;
  min-height: 250px;
  display: flex;
  flex-direction: column;
}

.banner-tag {
  position: absolute;
  top: 15px;
  left: 20px;
  background: rgba(0, 0, 0, 0.6);
  color: #fff;
  padding: 4px 12px;
  border-radius: $border-radius-sm;
  font-size: 12px;
  z-index: 2;
}

.banner-content {
  z-index: 1;
  flex: 1;
  h3 {
    font-size: 24px;
    color: #333;
    margin: 10px 0;
    font-weight: bold;
  }
  p {
    font-size: 16px;
    color: #666;
    margin-bottom: 15px;
  }
}

.banner-description {
  margin-bottom: 15px;
  p {
    font-size: 14px;
    color: #666;
    margin-bottom: 8px;
    line-height: 1.4;
  }
}

.banner-price {
  margin-bottom: 15px;
  .original-price {
    font-size: 18px;
    color: $danger-color;
    font-weight: bold;
    margin-right: 20px;
  }
  .target-level {
    font-size: 14px;
    color: #666;
  }
}

.banner-footer {
  display: flex;
  align-items: center;
  gap: 10px;
  .season-tag {
    background: #ff6b00;
    color: #fff;
    padding: 4px 12px;
    border-radius: $border-radius-sm;
    font-size: 12px;
  }
  .season-desc {
    font-size: 14px;
    color: #666;
  }
}

.banner-controls {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
  z-index: 2;
  .prev-btn,
  .next-btn {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.8);
    border: none;
    cursor: pointer;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
    &:hover {
      background: rgba(255, 255, 255, 1);
      transform: scale(1.1);
    }
  }
}

.banner-pagination {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 3;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: all 0.3s;
  &.active {
    background: #ff6b00;
    width: 20px;
    border-radius: 4px;
  }
}

.banner-status {
  position: absolute;
  top: 15px;
  right: 20px;
  background: #ff6b00;
  color: #fff;
  padding: 4px 12px;
  border-radius: $border-radius-sm;
  font-size: 12px;
  z-index: 2;
}

/* 快捷入口 */
.quick-entries {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 15px;
  background: #f9f9f9;
  padding: 20px;
  border-radius: $border-radius-lg;
}

.entry-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: transform 0.3s;
  &:hover {
    transform: translateY(-5px);
  }
  img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
  }
  span {
    font-size: 14px;
    color: $text-color-secondary;
    text-align: center;
  }
}

/* 右侧功能区 */
.right-sidebar {
  width: 220px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.login-card {
  background: #f9f9f9;
  border-radius: $border-radius-lg;
  padding: 20px;
  text-align: center;
}

.login-header {
  margin-bottom: 20px;
  h4 {
    font-size: 16px;
    color: $text-color;
    margin-bottom: 10px;
  }
  .bonus {
    display: inline-block;
    background: #ff6b00;
    color: #fff;
    padding: 4px 12px;
    border-radius: $border-radius-sm;
    font-size: 14px;
    font-weight: bold;
  }
}

.login-btn {
  width: 100%;
  padding: 10px;
  background: $primary-color;
  color: #fff;
  border: none;
  border-radius: $border-radius-base;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  &:hover {
    background: lighten($primary-color, 10%);
  }
  margin-bottom: 15px;
}

.danmaku-control {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-size: 14px;
  color: $text-color-secondary;
}

.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: .4s;
    border-radius: 20px;
    &:before {
      position: absolute;
      content: "";
      height: 16px;
      width: 16px;
      left: 2px;
      bottom: 2px;
      background-color: white;
      transition: .4s;
      border-radius: 50%;
    }
  }
  input:checked + .slider {
    background-color: $primary-color;
  }
  input:checked + .slider:before {
    transform: translateX(20px);
  }
}

.ai-assistant {
  background: #f9f9f9;
  border-radius: $border-radius-lg;
  padding: 20px;
  text-align: center;
}

.assistant-header {
  margin-bottom: 15px;
  span {
    font-size: 16px;
    color: $text-color;
    font-weight: 500;
  }
}

.assistant-content {
  p {
    font-size: 14px;
    color: $text-color-secondary;
    line-height: 1.4;
  }
}

.side-buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.side-btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: $border-radius-base;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
  span {
    margin-left: 8px;
  }
}

.contact-btn {
  background: #ff6b6b;
  color: #fff;
  &:hover {
    background: darken(#ff6b6b, 10%);
  }
}

.free-btn {
  background: #4ecdc4;
  color: #fff;
  &:hover {
    background: darken(#4ecdc4, 10%);
  }
}

.help-btn {
  background: #45b7d1;
  color: #fff;
  &:hover {
    background: darken(#45b7d1, 10%);
  }
}

.footer {
  background: #333;
  color: #fff;
  padding: 40px 0;
  margin-top: auto;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
  margin-bottom: 30px;
}

.footer-section h3 {
  font-size: 16px;
  margin-bottom: 20px;
  color: #fff;
}

.footer-section ul {
  list-style: none;
}

.footer-section li {
  margin-bottom: 10px;
}

.footer-section a {
  color: #ccc;
  font-size: 14px;
  transition: color 0.3s;
  &:hover {
    color: #fff;
  }
}

.footer-social {
  display: flex;
  gap: 15px;
}

.social-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  transition: background 0.3s;
  &:hover {
    background: $primary-color;
  }
}

.footer-bottom {
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 14px;
  color: #ccc;
}

@media (max-width: 1024px) {
  .header-nav {
    flex-wrap: wrap;
    gap: 10px;
  }
  
  .nav {
    order: 3;
    flex: 100%;
    margin: 10px 0;
    justify-content: center;
  }
  
  .header-right {
    order: 2;
  }
}

@media (max-width: 768px) {
  .header-nav {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
    padding: 15px;
  }
  
  .nav {
    flex-wrap: wrap;
    gap: 15px;
    padding: 10px 0;
  }
  
  .header-right {
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }
  
  .header-search {
    width: 100%;
  }
  
  .header-buttons {
    width: 100%;
    justify-content: space-between;
  }
  

  
  .courses-grid {
    grid-template-columns: 1fr;
  }
  
  .teachers-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .path-grid {
    grid-template-columns: 1fr;
  }
  
  .footer-content {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>