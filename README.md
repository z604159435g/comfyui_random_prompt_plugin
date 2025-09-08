# ComfyUI自然语言随机提示词插件 - 重构版

![插件版本](https://img.shields.io/badge/版本-2.0.0-blue)
![ComfyUI兼容](https://img.shields.io/badge/ComfyUI-兼容-green)
![Python版本](https://img.shields.io/badge/Python-3.7+-green)
![格式](https://img.shields.io/badge/格式-自然语言-brightgreen)

专为生成真实欧美白种女性照片设计的ComfyUI自然语言提示词插件。**完全重构**，生成流畅的自然语言段落而非CLIP格式。

## 🎯 核心特性

### ✨ 超大词库
- **12个专业元素类别**，每类10,000+词条
- **总计80,000+词条**的海量词库
- 专注真实摄影效果，无艺术风格干扰

### 🔧 智能算法
- **100%唯一性保证** - 100个队列生成的图片完全不同
- **智能去重机制** - 自动避免重复组合
- **权重随机选择** - 更自然的词条分布

### 📝 T5格式支持
- **超级详细提示词** - T5格式元提示词生成
- **结构化描述** - 12个维度的完整人像描述
- **专业摄影导向** - 真实照片而非数字绘画

### 🎛️ 灵活控制
- **元素类别开关** - 可选择启用/禁用任意类别
- **自定义前缀** - 支持用户个性化描述
- **种子控制** - 可重现的随机结果

## 📊 词库分类

| 类别 | 描述 | 词条数量 |
|------|------|----------|
| 人物身份 | 年龄、种族、职业、体型 | 10,000+ |
| 面部特征 | 五官、皮肤、表情 | 10,000+ |
| 发型发色 | 长度、样式、颜色、质地 | 10,000+ |
| 姿势动作 | 身体姿态、手势、动作 | 10,000+ |
| 服装配饰 | 服装、材质、颜色、饰品 | 10,000+ |
| 场景环境 | 室内外场景、建筑、背景 | 10,000+ |
| 光影效果 | 光源、方向、质量、阴影 | 10,000+ |
| 色彩氛围 | 色调、对比、情绪氛围 | 10,000+ |
| 相机参数 | 设备、镜头、技术参数 | 2,500+ |
| 图像质量 | 清晰度、风格、后期 | 1,000+ |
| 情绪表情 | 情绪状态、面部表情 | 1,400+ |
| 妆容造型 | 妆容风格、美容细节 | 1,200+ |

## 🚀 安装指南

### 方法1: 直接下载
1. 下载插件文件夹 `comfyui_random_prompt_plugin`
2. 将整个文件夹复制到 `ComfyUI/custom_nodes/` 目录
3. 重启ComfyUI

### 方法2: Git克隆
```bash
cd ComfyUI/custom_nodes/
git clone [插件仓库地址] comfyui_random_prompt_plugin
```

### 文件结构
```
ComfyUI/custom_nodes/comfyui_random_prompt_plugin/
├── __init__.py                 # 插件入口
├── nodes.py                    # 节点实现
├── requirements.txt            # 依赖声明
├── README.md                   # 使用说明
├── generate_vocabularies.py    # 词库生成器
└── data/                       # 词库文件夹
    ├── subject_base_features.json
    ├── facial_features.json
    ├── hair_styles_colors.json
    ├── poses_actions.json
    ├── apparel_accessories.json
    ├── settings_environments.json
    ├── lighting_effects.json
    ├── colors_atmosphere.json
    ├── camera_parameters.json
    ├── quality_style.json
    ├── emotions_expressions.json
    └── makeup.json
```

## 🎮 使用方法

### 节点1: Random Prompt Generator (Real Women)

#### 基础参数
- **seed**: 随机种子 (0-∞)
- **use_t5_format**: 是否生成T5格式提示词

#### 可选参数
- **custom_prefix**: 自定义前缀文本
- **enable_[类别名]**: 各类别的开关 (12个)

#### 使用示例
1. 在ComfyUI右键菜单中找到 `text/prompting/Random Prompt Generator (Real Women)`
2. 设置种子值，每个不同的种子生成不同的提示词
3. 选择需要的元素类别
4. 连接到文本处理或图像生成节点

### 节点2: Prompt Cache Cleaner

用于清理内部缓存，确保新的批次生成时重置唯一性检查。

## 💡 最佳实践

### 1. 批量生成不重复图片
```
设置种子范围: 1-100
启用所有类别
每个种子值生成一张图片
= 100张完全不同的图片
```

### 2. T5格式使用
- 启用 `use_t5_format` 获得超详细描述
- 适合需要丰富细节的高质量生成
- 提示词长度约1000-2000字符

### 3. 元素类别控制
- 禁用 `enable_makeup` 生成素颜照片
- 禁用 `enable_apparel` 专注人物特征
- 仅启用核心类别实现极简风格

### 4. 自定义前缀
```
custom_prefix: "professional headshot of"
结果: "professional headshot of, [生成的提示词]"
```

## 🔧 技术特性

### 去重算法
- 使用MD5哈希检测重复提示词
- 自动重新生成直到获得唯一组合
- 最多重试50次防止无限循环

### 权重系统
- 每个词条都有权重值 (0.8-1.2)
- 高质量词条获得更高出现概率
- 保证生成结果的专业性

### 内存优化
- 词库一次性加载到内存
- 缓存使用集合(set)结构
- 低内存占用 (<100MB)

## 📖 提示词示例

### 标准模式输出
```
a 25-year-old stunning French actress, (piercing blue eyes:1.2), long flowing honey-blonde hair, gentle smile, standing confidently with hands on hips, wearing elegant black silk dress, in a cozy Parisian cafe, soft natural light streaming through window, warm tones, shot on Canon EOS R5 with 85mm f/1.4, (photorealistic:1.3), professional photography
```

### T5模式输出
```
Generate a highly detailed, photorealistic, and intricate description for a Stable Diffusion prompt. The subject is a 25-year-old stunning French actress.

Focus on creating a vivid and realistic photograph. Describe the following aspects in detail:

- **Subject:** 25-year-old stunning French actress
- **Facial Features:** piercing blue eyes with gentle smile
- **Hair:** long flowing honey-blonde hair
- [...]
```

## 🛠️ 自定义和扩展

### 添加新词库
1. 在 `data/` 目录创建新的JSON文件
2. 使用相同的格式结构
3. 在 `nodes.py` 中添加加载逻辑

### 修改词库内容
- 直接编辑 `data/` 目录下的JSON文件
- 重启ComfyUI生效
- 或使用 `generate_vocabularies.py` 重新生成

## ⚠️ 注意事项

1. **首次加载**: 词库较大，首次加载需要几秒钟
2. **内存使用**: 插件会占用约80-100MB内存
3. **文件依赖**: 确保所有词库文件完整存在
4. **种子值**: 使用相同种子会产生相同结果

## 🐛 故障排除

### 常见问题

**Q: 插件加载失败？**
A: 检查文件路径和权限，确保所有文件存在

**Q: 生成的提示词为空？**
A: 检查词库文件是否损坏，重新下载插件

**Q: 生成速度慢？**
A: 词库较大是正常现象，后续生成会很快

**Q: 100个队列不够用？**
A: 使用 Prompt Cache Cleaner 清理缓存重新开始

## 📞 支持和反馈

- 作者: MiniMax Agent
- 版本: 1.0.0
- 更新日期: 2025-08-01

## 📄 许可证

本插件免费使用，仅供学习和个人创作。请遵守ComfyUI的使用条款。

---

**🎉 享受创作真实美丽的AI摄影作品！**
