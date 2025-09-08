#!/usr/bin/env python3
"""
ComfyUI随机提示词插件 - 一键安装脚本
自动检测ComfyUI安装位置并安装插件
作者: MiniMax Agent
"""

import os
import sys
import shutil
import json
from pathlib import Path

def find_comfyui_directory():
    """查找ComfyUI安装目录"""
    possible_paths = [
        "ComfyUI",
        "../ComfyUI", 
        "../../ComfyUI",
        os.path.expanduser("~/ComfyUI"),
        os.path.expanduser("~/Desktop/ComfyUI"),
        "/opt/ComfyUI",
        "C:/ComfyUI",
        "C:/ai/ComfyUI",
        "D:/ComfyUI",
        "D:/ai/ComfyUI"
    ]
    
    for path in possible_paths:
        comfy_path = Path(path)
        if comfy_path.exists() and (comfy_path / "main.py").exists():
            return comfy_path
    
    return None

def get_plugin_info():
    """获取插件信息"""
    current_dir = Path(__file__).parent
    
    # 检查必需文件
    required_files = [
        "__init__.py",
        "nodes.py", 
        "README.md",
        "requirements.txt",
        "data"
    ]
    
    missing_files = []
    for file in required_files:
        if not (current_dir / file).exists():
            missing_files.append(file)
    
    if missing_files:
        return None, missing_files
    
    # 统计词库文件
    data_dir = current_dir / "data"
    vocab_files = list(data_dir.glob("*.json"))
    
    return {
        "name": "comfyui_random_prompt_plugin",
        "path": current_dir,
        "vocab_files": len(vocab_files),
        "size_mb": sum(f.stat().st_size for f in current_dir.rglob("*") if f.is_file()) / 1024 / 1024
    }, None

def install_plugin(comfyui_path, plugin_info):
    """安装插件到ComfyUI"""
    custom_nodes_dir = comfyui_path / "custom_nodes"
    target_dir = custom_nodes_dir / plugin_info["name"]
    
    # 检查目标目录
    if target_dir.exists():
        print(f"⚠️  插件目录已存在: {target_dir}")
        response = input("是否覆盖安装? (y/N): ").lower()
        if response != 'y':
            print("❌ 安装已取消")
            return False
        
        # 备份原有安装
        backup_dir = target_dir.with_suffix(".backup")
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        shutil.move(str(target_dir), str(backup_dir))
        print(f"📦 已备份原安装到: {backup_dir}")
    
    # 复制插件文件
    try:
        shutil.copytree(str(plugin_info["path"]), str(target_dir))
        print(f"✅ 插件已安装到: {target_dir}")
        return True
    except Exception as e:
        print(f"❌ 安装失败: {e}")
        return False

def verify_installation(comfyui_path, plugin_name):
    """验证安装"""
    target_dir = comfyui_path / "custom_nodes" / plugin_name
    
    # 检查关键文件
    key_files = ["__init__.py", "nodes.py", "data"]
    missing = []
    
    for file in key_files:
        if not (target_dir / file).exists():
            missing.append(file)
    
    if missing:
        print(f"❌ 安装验证失败，缺少文件: {missing}")
        return False
    
    # 检查词库文件
    data_dir = target_dir / "data"
    vocab_count = len(list(data_dir.glob("*.json")))
    
    if vocab_count < 10:
        print(f"❌ 词库文件不完整，只找到 {vocab_count} 个")
        return False
    
    print(f"✅ 安装验证成功")
    print(f"   📁 插件目录: {target_dir}")
    print(f"   📚 词库文件: {vocab_count} 个")
    
    return True

def main():
    """主安装函数"""
    print("🚀 ComfyUI随机提示词插件 - 自动安装程序")
    print("=" * 60)
    print("👤 作者: MiniMax Agent")
    print("📅 版本: 1.0.0")
    print("=" * 60)
    print()
    
    # 1. 检查插件文件
    print("🔍 步骤1: 检查插件文件...")
    plugin_info, missing_files = get_plugin_info()
    
    if not plugin_info:
        print(f"❌ 插件文件不完整，缺少: {missing_files}")
        print("请确保所有插件文件都在当前目录中")
        return
    
    print(f"✅ 插件文件完整")
    print(f"   📦 大小: {plugin_info['size_mb']:.1f} MB")
    print(f"   📚 词库: {plugin_info['vocab_files']} 个文件")
    print()
    
    # 2. 查找ComfyUI
    print("🔍 步骤2: 查找ComfyUI安装目录...")
    comfyui_path = find_comfyui_directory()
    
    if not comfyui_path:
        print("❌ 未找到ComfyUI安装目录")
        print("请手动指定ComfyUI目录路径:")
        manual_path = input("ComfyUI路径: ").strip()
        
        if manual_path and Path(manual_path).exists():
            comfyui_path = Path(manual_path)
        else:
            print("❌ 无效路径，安装终止")
            return
    
    print(f"✅ 找到ComfyUI: {comfyui_path}")
    print()
    
    # 3. 安装插件
    print("⚙️  步骤3: 安装插件...")
    if not install_plugin(comfyui_path, plugin_info):
        return
    print()
    
    # 4. 验证安装
    print("✅ 步骤4: 验证安装...")
    if not verify_installation(comfyui_path, plugin_info["name"]):
        return
    print()
    
    # 5. 安装完成
    print("🎉 安装完成！")
    print("-" * 40)
    print("📋 下一步操作:")
    print("1. 重启ComfyUI")
    print("2. 在右键菜单中找到 'text/prompting/Random Prompt Generator (Real Women)'")
    print("3. 开始创作真实美丽的AI摄影作品！")
    print()
    print("📖 使用帮助:")
    print(f"   查看: {comfyui_path}/custom_nodes/{plugin_info['name']}/README.md")
    print()
    print("🧪 功能测试:")
    print(f"   运行: python {comfyui_path}/custom_nodes/{plugin_info['name']}/test_plugin.py")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ 安装被用户中断")
    except Exception as e:
        print(f"\n❌ 安装过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
