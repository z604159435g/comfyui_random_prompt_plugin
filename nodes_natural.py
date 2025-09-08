"""
ComfyUI自然语言随机提示词插件 - 核心节点实现
专为真实欧美白种女性照片生成设计的自然语言提示词生成器
完全重构，生成流畅的自然语言段落而非CLIP格式
作者: MiniMax Agent
"""

import json
import os
import random
import hashlib
from typing import Dict, List, Tuple, Any, Optional

class NaturalLanguagePromptGenerator:
    """自然语言随机提示词生成器节点"""
    
    def __init__(self):
        self.vocabularies = {}
        self.generated_prompts_cache = set()  # 用于确保100个队列的唯一性
        self.data_dir = os.path.join(os.path.dirname(__file__), "data_natural")
        self.load_vocabularies()
    
    def load_vocabularies(self):
        """加载所有自然语言词库文件"""
        vocabulary_files = [
            "person_base_descriptions.json",
            "hair_facial_features.json", 
            "body_descriptions.json",
            "upper_clothing.json",
            "lower_clothing_accessories.json",
            "body_posture.json",
            "background_environment.json",
            "lighting_photography.json",
            "composition_angle.json",
            "overall_atmosphere.json"
        ]
        
        for vocab_file in vocabulary_files:
            file_path = os.path.join(self.data_dir, vocab_file)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        vocab_data = json.load(f)
                        self.vocabularies[vocab_data['category']] = vocab_data['entries']
                except Exception as e:
                    print(f"⚠️  加载词库文件 {vocab_file} 失败: {e}")
        
        print(f"✅ 已加载 {len(self.vocabularies)} 个自然语言词库文件")
    
    def get_random_term(self, category: str, random_gen: random.Random) -> str:
        """从指定类别中随机选择一个自然语言描述"""
        if category not in self.vocabularies:
            return ""
        
        entries = self.vocabularies[category]
        if not entries:
            return ""
        
        # 支持权重随机选择
        terms = [entry['term'] for entry in entries]
        weights = [entry.get('weight', 1.0) for entry in entries]
        
        return random_gen.choices(terms, weights=weights, k=1)[0]
    
    def connect_sentences_naturally(self, sentences: List[str]) -> str:
        """将多个自然语言描述连接成流畅的段落"""
        if not sentences:
            return ""
        
        # 过滤空句子
        valid_sentences = [s.strip() for s in sentences if s.strip()]
        if not valid_sentences:
            return ""
        
        # 如果只有一个句子，直接返回
        if len(valid_sentences) == 1:
            return valid_sentences[0]
        
        # 智能连接多个句子
        result = valid_sentences[0]
        
        for i, sentence in enumerate(valid_sentences[1:], 1):
            # 根据句子内容选择合适的连接方式
            if sentence.startswith("She "):
                # 直接连接以"She"开头的句子
                result += " " + sentence
            elif sentence.startswith("Her "):
                # 直接连接以"Her"开头的句子
                result += " " + sentence
            elif sentence.startswith("The "):
                # 直接连接以"The"开头的句子
                result += " " + sentence
            elif i == len(valid_sentences) - 1:
                # 最后一个句子，用适当的连接词
                result += " " + sentence
            else:
                # 中间的句子，直接连接
                result += " " + sentence
        
        return result
    
    def generate_natural_language_prompt(self, 
                                       seed: int, 
                                       enable_categories: Dict[str, bool],
                                       custom_prefix: str = "") -> str:
        """生成自然语言提示词"""
        
        # 使用种子初始化随机数生成器
        random_gen = random.Random(seed)
        
        # 从各个类别中选择元素
        selected_descriptions = []
        
        # 添加自定义前缀
        if custom_prefix.strip():
            selected_descriptions.append(custom_prefix.strip())
        
        # 按逻辑顺序选择描述
        if enable_categories.get('person_base', True):
            desc = self.get_random_term('person_base', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('hair_facial', True):
            desc = self.get_random_term('hair_facial', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('body_descriptions', True):
            desc = self.get_random_term('body_descriptions', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('upper_clothing', True):
            desc = self.get_random_term('upper_clothing', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('lower_accessories', True):
            desc = self.get_random_term('lower_accessories', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('body_posture', True):
            desc = self.get_random_term('body_posture', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('background_environment', True):
            desc = self.get_random_term('background_environment', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('lighting_photography', True):
            desc = self.get_random_term('lighting_photography', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('composition_angle', True):
            desc = self.get_random_term('composition_angle', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        if enable_categories.get('overall_atmosphere', True):
            desc = self.get_random_term('overall_atmosphere', random_gen)
            if desc:
                selected_descriptions.append(desc)
        
        # 连接成自然段落
        final_prompt = self.connect_sentences_naturally(selected_descriptions)
        
        # 确保唯一性（用于100个队列生成）
        prompt_hash = hashlib.md5(final_prompt.encode()).hexdigest()
        retry_count = 0
        max_retries = 50
        
        while prompt_hash in self.generated_prompts_cache and retry_count < max_retries:
            # 重新生成
            seed += 1
            random_gen = random.Random(seed)
            
            # 重新选择元素
            selected_descriptions = []
            if custom_prefix.strip():
                selected_descriptions.append(custom_prefix.strip())
            
            # 重新随机选择各类别
            for category_key, category_name in [
                ('person_base', 'person_base'),
                ('hair_facial', 'hair_facial'),
                ('body_descriptions', 'body_descriptions'),
                ('upper_clothing', 'upper_clothing'),
                ('lower_accessories', 'lower_accessories'),
                ('body_posture', 'body_posture'),
                ('background_environment', 'background_environment'),
                ('lighting_photography', 'lighting_photography'),
                ('composition_angle', 'composition_angle'),
                ('overall_atmosphere', 'overall_atmosphere')
            ]:
                if enable_categories.get(category_key, True):
                    desc = self.get_random_term(category_name, random_gen)
                    if desc:
                        selected_descriptions.append(desc)
            
            final_prompt = self.connect_sentences_naturally(selected_descriptions)
            prompt_hash = hashlib.md5(final_prompt.encode()).hexdigest()
            retry_count += 1
        
        # 添加到缓存
        self.generated_prompts_cache.add(prompt_hash)
        
        return final_prompt
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "custom_prefix": ("STRING", {"multiline": True, "default": ""}),
                "enable_person_base": ("BOOLEAN", {"default": True}),
                "enable_hair_facial": ("BOOLEAN", {"default": True}),
                "enable_body_descriptions": ("BOOLEAN", {"default": True}),
                "enable_upper_clothing": ("BOOLEAN", {"default": True}),
                "enable_lower_accessories": ("BOOLEAN", {"default": True}),
                "enable_body_posture": ("BOOLEAN", {"default": True}),
                "enable_background": ("BOOLEAN", {"default": True}),
                "enable_lighting": ("BOOLEAN", {"default": True}),
                "enable_composition": ("BOOLEAN", {"default": True}),
                "enable_atmosphere": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("natural_language_prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "text/prompting"
    
    def generate_prompt(self, 
                       seed: int,
                       custom_prefix: str = "",
                       enable_person_base: bool = True,
                       enable_hair_facial: bool = True,
                       enable_body_descriptions: bool = True,
                       enable_upper_clothing: bool = True,
                       enable_lower_accessories: bool = True,
                       enable_body_posture: bool = True,
                       enable_background: bool = True,
                       enable_lighting: bool = True,
                       enable_composition: bool = True,
                       enable_atmosphere: bool = True) -> Tuple[str]:
        """生成自然语言随机提示词"""
        
        enable_categories = {
            'person_base': enable_person_base,
            'hair_facial': enable_hair_facial,
            'body_descriptions': enable_body_descriptions,
            'upper_clothing': enable_upper_clothing,
            'lower_accessories': enable_lower_accessories,
            'body_posture': enable_body_posture,
            'background_environment': enable_background,
            'lighting_photography': enable_lighting,
            'composition_angle': enable_composition,
            'overall_atmosphere': enable_atmosphere,
        }
        
        prompt = self.generate_natural_language_prompt(
            seed=seed,
            enable_categories=enable_categories,
            custom_prefix=custom_prefix
        )
        
        return (prompt,)


class PromptCacheCleaner:
    """提示词缓存清理节点"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clear_cache": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("status",)
    FUNCTION = "clear_cache"
    CATEGORY = "text/prompting"
    
    def clear_cache(self, clear_cache: bool = False) -> Tuple[str]:
        """清理提示词缓存"""
        if clear_cache:
            # 清理缓存
            NaturalLanguagePromptGenerator.generated_prompts_cache = set()
            return ("Natural language prompt cache cleared successfully",)
        else:
            cache_size = len(getattr(NaturalLanguagePromptGenerator, 'generated_prompts_cache', set()))
            return (f"Natural language prompt cache contains {cache_size} entries",)


# 节点类映射
NODE_CLASS_MAPPINGS = {
    "NaturalLanguagePromptGenerator": NaturalLanguagePromptGenerator,
    "PromptCacheCleaner": PromptCacheCleaner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NaturalLanguagePromptGenerator": "Natural Language Prompt Generator",
    "PromptCacheCleaner": "Prompt Cache Cleaner",
}
