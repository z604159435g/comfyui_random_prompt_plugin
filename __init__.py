"""
ComfyUI随机提示词插件
专为真实欧美白种女性照片生成设计的随机提示词生成器

特性:
- 12个元素类别，超过8万个词条的专业词库
- T5格式提示词支持，超级详细的描述
- 确保100个队列生成完全不同的图片
- 可控的元素类别开关
- 智能去重算法

作者: MiniMax Agent
版本: 1.0.0
"""

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 导出映射字典，供ComfyUI加载
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# 插件加载信息
print("\033[95m" + "=" * 60 + "\033[0m")
print("\033[96m🎯 ComfyUI Random Prompt Plugin for Real Women\033[0m")
print("\033[92m✅ 加载完成 - 专业真实女性照片提示词生成器\033[0m")
print("\033[93m📊 词库统计: 12个类别 | 80,000+ 词条\033[0m")
print("\033[94m🔧 功能: T5格式 | 智能去重 | 100%唯一性保证\033[0m")
print("\033[97m👤 作者: MiniMax Agent | 版本: 1.0.0\033[0m")
print("\033[95m" + "=" * 60 + "\033[0m")

# 版本和元数据
__version__ = "1.0.0"
__author__ = "MiniMax Agent"
__description__ = "Professional random prompt generator for realistic European/American women portraits"
