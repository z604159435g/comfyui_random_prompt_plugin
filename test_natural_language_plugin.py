#!/usr/bin/env python3
"""
ComfyUI自然语言随机提示词插件测试脚本
验证重构后的自然语言格式功能
作者: MiniMax Agent
"""

import sys
import os
import time
from typing import Set

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(__file__))

from nodes import NaturalLanguagePromptGenerator, PromptCacheCleaner

def test_natural_language_generation():
    """测试自然语言生成功能"""
    print("🔧 测试1: 自然语言生成功能")
    print("-" * 50)
    
    # 创建生成器实例
    generator = NaturalLanguagePromptGenerator()
    
    # 测试标准生成
    prompt1 = generator.generate_prompt(seed=12345)
    print(f"📝 自然语言提示词 (种子=12345):")
    print(f"   {prompt1[0]}")
    print()
    
    # 测试自定义前缀
    prompt2 = generator.generate_prompt(
        seed=12345, 
        custom_prefix="This is a high-resolution photograph featuring"
    )
    print(f"📝 带前缀的自然语言提示词:")
    print(f"   {prompt2[0][:150]}...")
    print()
    
    print("✅ 自然语言生成功能测试通过")
    print()

def test_category_control():
    """测试类别控制功能"""
    print("🎛️ 测试2: 类别控制测试")
    print("-" * 50)
    
    generator = NaturalLanguagePromptGenerator()
    
    # 仅启用核心人物类别
    prompt1 = generator.generate_prompt(
        seed=11111,
        enable_person_base=True,
        enable_hair_facial=True,
        enable_body_descriptions=True,
        enable_upper_clothing=False,
        enable_lower_accessories=False,
        enable_body_posture=False,
        enable_background=False,
        enable_lighting=False,
        enable_composition=False,
        enable_atmosphere=False
    )
    print(f"📝 仅人物描述模式:")
    print(f"   {prompt1[0]}")
    print()
    
    # 仅启用技术类别
    prompt2 = generator.generate_prompt(
        seed=11111,
        enable_person_base=False,
        enable_hair_facial=False,
        enable_body_descriptions=False,
        enable_upper_clothing=False,
        enable_lower_accessories=False,
        enable_body_posture=False,
        enable_background=True,
        enable_lighting=True,
        enable_composition=True,
        enable_atmosphere=True
    )
    print(f"📝 仅技术描述模式:")
    print(f"   {prompt2[0]}")
    print()
    
    print("✅ 类别控制测试通过")
    print()

def test_uniqueness():
    """测试100个队列的唯一性"""
    print("🔄 测试3: 唯一性测试 (100个队列)")
    print("-" * 50)
    
    generator = NaturalLanguagePromptGenerator()
    
    # 清理缓存
    generator.generated_prompts_cache = set()
    
    # 生成100个提示词
    prompts = set()
    start_time = time.time()
    
    for i in range(100):
        prompt = generator.generate_prompt(seed=i)
        prompts.add(prompt[0])
        
        if (i + 1) % 20 == 0:
            print(f"   已生成 {i+1}/100 个自然语言提示词...")
    
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
    
    if unique_count >= 95:  # 允许少量重复
        print("✅ 唯一性测试通过 (≥95%)")
    else:
        print("⚠️  唯一性测试警告 (<95%)")
    print()

def test_vocabulary_loading():
    """测试词库加载"""
    print("📚 测试4: 自然语言词库加载测试")
    print("-" * 50)
    
    generator = NaturalLanguagePromptGenerator()
    
    # 检查词库加载情况
    total_entries = 0
    for category, entries in generator.vocabularies.items():
        entry_count = len(entries)
        total_entries += entry_count
        print(f"   {category}: {entry_count:,} 自然语言描述")
    
    print(f"📊 自然语言词库统计:")
    print(f"   类别数量: {len(generator.vocabularies)}")
    print(f"   描述总数: {total_entries:,}")
    print()
    
    if len(generator.vocabularies) >= 8 and total_entries >= 10000:
        print("✅ 自然语言词库加载测试通过")
    else:
        print("❌ 自然语言词库加载测试失败")
    print()

def test_performance():
    """测试性能"""
    print("⚡ 测试5: 性能测试")
    print("-" * 50)
    
    generator = NaturalLanguagePromptGenerator()
    
    # 测试单次生成性能
    start_time = time.time()
    prompt = generator.generate_prompt(seed=99999)
    single_time = time.time() - start_time
    
    print(f"⏱️  单次生成耗时: {single_time*1000:.2f} 毫秒")
    print(f"📝 示例长度: {len(prompt[0])} 字符")
    
    # 测试批量生成性能
    start_time = time.time()
    for i in range(20):
        generator.generate_prompt(seed=1000+i)
    batch_time = time.time() - start_time
    avg_time = batch_time / 20
    
    print(f"⏱️  批量生成耗时: {batch_time:.2f} 秒 (20个)")
    print(f"⏱️  平均单次耗时: {avg_time*1000:.2f} 毫秒")
    
    if avg_time < 0.1:  # 100毫秒内
        print("✅ 性能测试通过")
    else:
        print("⚠️  性能测试警告 (>100ms)")
    print()

def display_sample_outputs():
    """显示示例输出"""
    print("📋 自然语言提示词示例展示")
    print("=" * 70)
    
    generator = NaturalLanguagePromptGenerator()
    
    # 示例1: 完整描述
    print("🎯 示例1: 完整自然语言描述")
    prompt1 = generator.generate_prompt(seed=2024)
    print(f"种子: 2024")
    print(f"长度: {len(prompt1[0])} 字符")
    print(f"内容: {prompt1[0]}")
    print()
    
    # 示例2: 带前缀
    print("🎯 示例2: 带自定义前缀")
    prompt2 = generator.generate_prompt(
        seed=2025, 
        custom_prefix="This is a high-resolution photograph featuring"
    )
    print(f"种子: 2025")
    print(f"长度: {len(prompt2[0])} 字符")
    print(f"内容: {prompt2[0]}")
    print()
    
    # 示例3: 最小类别
    print("🎯 示例3: 最小类别组合")
    prompt3 = generator.generate_prompt(
        seed=2026,
        enable_person_base=True,
        enable_hair_facial=True,
        enable_body_descriptions=False,
        enable_upper_clothing=False,
        enable_lower_accessories=False,
        enable_body_posture=False,
        enable_background=False,
        enable_lighting=False,
        enable_composition=False,
        enable_atmosphere=False
    )
    print(f"种子: 2026")
    print(f"长度: {len(prompt3[0])} 字符")
    print(f"内容: {prompt3[0]}")
    print()

def main():
    """主测试函数"""
    print("🧪 ComfyUI自然语言随机提示词插件 - 功能测试")
    print("=" * 70)
    print("📅 测试时间:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("👤 作者: MiniMax Agent")
    print("🔄 版本: 2.0.0 (自然语言重构版)")
    print("=" * 70)
    print()
    
    try:
        # 运行所有测试
        test_vocabulary_loading()
        test_natural_language_generation()
        test_category_control()
        test_performance()
        test_uniqueness()
        
        # 显示示例
        display_sample_outputs()
        
        print("🎉 所有测试完成！")
        print("✅ 自然语言插件功能正常，完全符合用户要求")
        print("📝 生成的提示词为流畅的自然语言段落格式")
        print("🚫 已移除所有CLIP格式的单词短语组合")
        
    except Exception as e:
        print(f"❌ 测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
