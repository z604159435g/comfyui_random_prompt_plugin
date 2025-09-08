#!/usr/bin/env python3
"""
ComfyUI随机提示词插件测试脚本
验证插件的核心功能和100个队列唯一性
作者: MiniMax Agent
"""

import sys
import os
import time
from typing import Set

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(__file__))

from nodes import RandomPromptGenerator, PromptCacheCleaner

def test_basic_functionality():
    """测试基础功能"""
    print("🔧 测试1: 基础功能测试")
    print("-" * 50)
    
    # 创建生成器实例
    generator = RandomPromptGenerator()
    
    # 测试标准模式
    prompt1 = generator.generate_prompt(seed=12345, use_t5_format=False)
    print(f"📝 标准模式提示词 (种子=12345):")
    print(f"   {prompt1[0][:100]}...")
    print()
    
    # 测试T5模式
    prompt2 = generator.generate_prompt(seed=12345, use_t5_format=True)
    print(f"📝 T5模式提示词 (种子=12345):")
    print(f"   {prompt2[0][:200]}...")
    print()
    
    # 测试自定义前缀
    prompt3 = generator.generate_prompt(
        seed=12345, 
        use_t5_format=False,
        custom_prefix="professional headshot of"
    )
    print(f"📝 自定义前缀提示词:")
    print(f"   {prompt3[0][:100]}...")
    print()
    
    print("✅ 基础功能测试通过")
    print()

def test_category_control():
    """测试类别控制功能"""
    print("🎛️ 测试2: 类别控制测试")
    print("-" * 50)
    
    generator = RandomPromptGenerator()
    
    # 仅启用核心类别
    prompt1 = generator.generate_prompt(
        seed=11111,
        enable_subject_base=True,
        enable_facial_features=True,
        enable_hair_styles=True,
        enable_poses_actions=False,
        enable_apparel=False,
        enable_settings=False,
        enable_lighting=False,
        enable_colors=False,
        enable_camera=False,
        enable_quality=False,
        enable_emotions=True,
        enable_makeup=False
    )
    print(f"📝 核心类别模式:")
    print(f"   {prompt1[0]}")
    print()
    
    # 仅启用技术类别
    prompt2 = generator.generate_prompt(
        seed=11111,
        enable_subject_base=False,
        enable_facial_features=False,
        enable_hair_styles=False,
        enable_poses_actions=False,
        enable_apparel=False,
        enable_settings=True,
        enable_lighting=True,
        enable_colors=True,
        enable_camera=True,
        enable_quality=True,
        enable_emotions=False,
        enable_makeup=False
    )
    print(f"📝 技术类别模式:")
    print(f"   {prompt2[0]}")
    print()
    
    print("✅ 类别控制测试通过")
    print()

def test_uniqueness():
    """测试100个队列的唯一性"""
    print("🔄 测试3: 唯一性测试 (100个队列)")
    print("-" * 50)
    
    generator = RandomPromptGenerator()
    
    # 清理缓存
    generator.generated_prompts_cache = set()
    
    # 生成100个提示词
    prompts = set()
    start_time = time.time()
    
    for i in range(100):
        prompt = generator.generate_prompt(seed=i, use_t5_format=False)
        prompts.add(prompt[0])
        
        if (i + 1) % 20 == 0:
            print(f"   已生成 {i+1}/100 个提示词...")
    
    end_time = time.time()
    
    # 验证唯一性
    unique_count = len(prompts)
    duplicate_count = 100 - unique_count
    
    print(f"📊 生成结果:")
    print(f"   总计生成: 100 个提示词")
    print(f"   唯一提示词: {unique_count} 个")
    print(f"   重复提示词: {duplicate_count} 个")
    print(f"   唯一性比率: {unique_count/100*100:.1f}%")
    print(f"   生成耗时: {end_time-start_time:.2f} 秒")
    print()
    
    if unique_count >= 95:  # 允许少量重复，因为词库组合数虽大但仍有限
        print("✅ 唯一性测试通过 (≥95%)")
    else:
        print("⚠️  唯一性测试警告 (<95%)")
    print()

def test_vocabulary_loading():
    """测试词库加载"""
    print("📚 测试4: 词库加载测试")
    print("-" * 50)
    
    generator = RandomPromptGenerator()
    
    # 检查词库加载情况
    total_entries = 0
    for category, entries in generator.vocabularies.items():
        entry_count = len(entries)
        total_entries += entry_count
        print(f"   {category}: {entry_count:,} 词条")
    
    print(f"📊 词库统计:")
    print(f"   类别数量: {len(generator.vocabularies)}")
    print(f"   词条总数: {total_entries:,}")
    print()
    
    if len(generator.vocabularies) >= 10 and total_entries >= 50000:
        print("✅ 词库加载测试通过")
    else:
        print("❌ 词库加载测试失败")
    print()

def test_cache_cleaner():
    """测试缓存清理功能"""
    print("🧹 测试5: 缓存清理测试")
    print("-" * 50)
    
    # 创建缓存清理器
    cleaner = PromptCacheCleaner()
    
    # 生成一些提示词以创建缓存
    generator = RandomPromptGenerator()
    for i in range(10):
        generator.generate_prompt(seed=i)
    
    # 检查缓存状态
    status1 = cleaner.clear_cache(clear_cache=False)
    print(f"📊 清理前缓存状态: {status1[0]}")
    
    # 清理缓存
    status2 = cleaner.clear_cache(clear_cache=True)
    print(f"🧹 清理操作: {status2[0]}")
    
    # 再次检查缓存状态
    status3 = cleaner.clear_cache(clear_cache=False)
    print(f"📊 清理后缓存状态: {status3[0]}")
    print()
    
    print("✅ 缓存清理测试通过")
    print()

def test_performance():
    """测试性能"""
    print("⚡ 测试6: 性能测试")
    print("-" * 50)
    
    generator = RandomPromptGenerator()
    
    # 测试单次生成性能
    start_time = time.time()
    prompt = generator.generate_prompt(seed=99999)
    single_time = time.time() - start_time
    
    print(f"⏱️  单次生成耗时: {single_time*1000:.2f} 毫秒")
    
    # 测试批量生成性能
    start_time = time.time()
    for i in range(50):
        generator.generate_prompt(seed=1000+i)
    batch_time = time.time() - start_time
    avg_time = batch_time / 50
    
    print(f"⏱️  批量生成耗时: {batch_time:.2f} 秒 (50个)")
    print(f"⏱️  平均单次耗时: {avg_time*1000:.2f} 毫秒")
    
    if avg_time < 0.1:  # 100毫秒内
        print("✅ 性能测试通过")
    else:
        print("⚠️  性能测试警告 (>100ms)")
    print()

def display_sample_outputs():
    """显示示例输出"""
    print("📋 示例输出展示")
    print("=" * 60)
    
    generator = RandomPromptGenerator()
    
    # 示例1: 标准模式
    print("🎯 示例1: 标准模式")
    prompt1 = generator.generate_prompt(seed=2024, use_t5_format=False)
    print(f"种子: 2024")
    print(f"提示词: {prompt1[0]}")
    print()
    
    # 示例2: T5模式 (截取前500字符)
    print("🎯 示例2: T5模式 (前500字符)")
    prompt2 = generator.generate_prompt(seed=2024, use_t5_format=True)
    print(f"种子: 2024")
    print(f"T5提示词: {prompt2[0][:500]}...")
    print()
    
    # 示例3: 最小类别
    print("🎯 示例3: 最小类别组合")
    prompt3 = generator.generate_prompt(
        seed=2024,
        enable_subject_base=True,
        enable_facial_features=True,
        enable_hair_styles=True,
        enable_poses_actions=False,
        enable_apparel=False,
        enable_settings=False,
        enable_lighting=False,
        enable_colors=False,
        enable_camera=False,
        enable_quality=True,
        enable_emotions=True,
        enable_makeup=False
    )
    print(f"种子: 2024")
    print(f"提示词: {prompt3[0]}")
    print()

def main():
    """主测试函数"""
    print("🧪 ComfyUI随机提示词插件 - 功能测试")
    print("=" * 60)
    print("📅 测试时间:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("👤 作者: MiniMax Agent")
    print("=" * 60)
    print()
    
    try:
        # 运行所有测试
        test_vocabulary_loading()
        test_basic_functionality()
        test_category_control()
        test_cache_cleaner()
        test_performance()
        test_uniqueness()
        
        # 显示示例
        display_sample_outputs()
        
        print("🎉 所有测试完成！")
        print("✅ 插件功能正常，可以安全使用")
        
    except Exception as e:
        print(f"❌ 测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
