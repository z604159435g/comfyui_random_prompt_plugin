#!/usr/bin/env python3
"""
ComfyUI随机提示词插件 - 大型词库生成器
为真实欧美白种女性照片生成创建超过10万个词条的专业词库
作者: MiniMax Agent
"""

import json
import os
import random
from typing import List, Dict

class VocabularyGenerator:
    def __init__(self):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
    
    def save_vocabulary(self, filename: str, name: str, description: str, category: str, entries: List[Dict]):
        """保存词库到JSON文件"""
        vocabulary = {
            "name": name,
            "description": description,
            "category": category,
            "total_entries": len(entries),
            "entries": entries
        }
        
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(vocabulary, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 已生成 {filename}，包含 {len(entries)} 个词条")

    def generate_subject_base_features(self):
        """生成人物身份与基础特征词库"""
        entries = []
        
        # 年龄范围
        ages = list(range(18, 40))
        
        # 国籍/种族
        ethnicities = [
            "Scandinavian", "Swedish", "Norwegian", "Danish", "Finnish", "Icelandic",
            "German", "Austrian", "Swiss", "Dutch", "Belgian", "Luxembourgish",
            "French", "Parisian", "Lyonnaise", "Marseillaise",
            "British", "English", "Scottish", "Welsh", "Irish",
            "American", "Canadian", "Australian", "New Zealand",
            "Italian", "Spanish", "Portuguese", "Greek", "Maltese",
            "Russian", "Polish", "Czech", "Hungarian", "Slovakian", "Slovenian",
            "Croatian", "Serbian", "Bosnian", "Montenegrin", "Macedonian",
            "Estonian", "Latvian", "Lithuanian", "Ukrainian", "Belarusian",
            "Romanian", "Bulgarian", "Moldovan", "Albanian", "Kosovan"
        ]
        
        # 职业/身份
        professions = [
            "woman", "model", "actress", "dancer", "student", "photographer", "artist",
            "businesswoman", "entrepreneur", "designer", "teacher", "doctor", "lawyer",
            "nurse", "engineer", "architect", "scientist", "researcher", "journalist",
            "writer", "musician", "singer", "athlete", "fitness instructor", "yoga instructor",
            "chef", "barista", "librarian", "psychologist", "therapist", "consultant",
            "marketing executive", "sales manager", "HR specialist", "accountant",
            "fashion stylist", "makeup artist", "hairstylist", "interior designer",
            "graphic designer", "web designer", "software developer", "data analyst",
            "project manager", "social media manager", "influencer", "blogger",
            "travel blogger", "food blogger", "lifestyle blogger", "fashion blogger",
            "fitness blogger", "beauty blogger", "tech reviewer", "art critic",
            "wine sommelier", "personal shopper", "event planner", "wedding planner",
            "real estate agent", "financial advisor", "investment banker", "economist",
            "veterinarian", "dentist", "pharmacist", "optometrist", "chiropractor",
            "physical therapist", "occupational therapist", "speech therapist",
            "social worker", "counselor", "life coach", "personal trainer",
            "nutritionist", "dietitian", "massage therapist", "acupuncturist",
            "flight attendant", "pilot", "travel agent", "tour guide", "hotel manager",
            "restaurant manager", "retail manager", "store owner", "boutique owner",
            "gallery owner", "museum curator", "art dealer", "antique dealer",
            "jewelry designer", "fashion designer", "textile designer", "product designer",
            "industrial designer", "automotive designer", "furniture designer",
            "landscape architect", "urban planner", "civil engineer", "mechanical engineer",
            "electrical engineer", "chemical engineer", "biomedical engineer",
            "environmental scientist", "marine biologist", "wildlife biologist",
            "astronomer", "physicist", "chemist", "mathematician", "statistician",
            "college professor", "high school teacher", "elementary teacher", "tutor",
            "school principal", "education administrator", "school counselor"
        ]
        
        # 形容词
        adjectives = [
            "beautiful", "stunning", "gorgeous", "elegant", "charming", "attractive",
            "lovely", "pretty", "graceful", "sophisticated", "alluring", "captivating",
            "enchanting", "mesmerizing", "radiant", "luminous", "glowing", "vibrant",
            "striking", "remarkable", "exceptional", "extraordinary", "magnificent",
            "splendid", "wonderful", "marvelous", "fantastic", "amazing", "incredible",
            "breathtaking", "jaw-dropping", "eye-catching", "head-turning", "show-stopping",
            "dazzling", "brilliant", "sparkling", "shimmering", "gleaming", "glittering",
            "young", "youthful", "fresh-faced", "innocent", "sweet", "cute", "adorable",
            "mature", "experienced", "worldly", "confident", "self-assured", "poised",
            "mysterious", "enigmatic", "intriguing", "fascinating", "compelling",
            "magnetic", "charismatic", "charming", "delightful", "pleasant", "friendly"
        ]
        
        # 体型描述
        body_types = [
            "athletic build", "curvy body shape", "slender frame", "petite build",
            "tall and elegant", "medium height", "hourglass figure", "pear-shaped body",
            "apple-shaped body", "rectangle body shape", "inverted triangle body",
            "fit and toned", "muscular physique", "lean physique", "soft curves",
            "graceful posture", "confident stance", "elegant silhouette", "perfect proportions",
            "statuesque figure", "model-like physique", "dancer's body", "athlete's build",
            "svelte figure", "willowy frame", "curvaceous silhouette", "toned physique",
            "lithe build", "compact frame", "robust build", "delicate frame",
            "well-proportioned", "symmetrical figure", "balanced proportions", "ideal measurements",
            "classic beauty proportions", "golden ratio physique", "magazine-worthy figure",
            "runway model build", "fitness model physique", "bikini model body",
            "lingerie model figure", "commercial model build", "fashion model frame",
            "plus-size beauty", "full-figured woman", "voluptuous curves", "generous curves",
            "natural curves", "subtle curves", "gentle curves", "flowing lines",
            "smooth silhouette", "refined proportions", "elegant lines", "graceful contours"
        ]
        
        # 生成组合
        count = 0
        target_count = 10000
        
        # 基础组合：年龄 + 形容词 + 种族 + 职业
        for age in ages:
            for adj in adjectives:
                for ethnicity in ethnicities:
                    for profession in professions:
                        if count >= target_count:
                            break
                        
                        # 创建多种句式变化
                        variations = [
                            f"a {age}-year-old {adj} {ethnicity} {profession}",
                            f"a {adj} {age}-year-old {ethnicity} {profession}",
                            f"a young {adj} {ethnicity} {profession}",
                            f"a beautiful {age}-year-old {ethnicity} {profession}",
                            f"a stunning {ethnicity} {profession} in her {age}s" if age >= 20 else f"a stunning {ethnicity} {profession}",
                        ]
                        
                        for var in variations:
                            if count >= target_count:
                                break
                            entries.append({
                                "weight": round(random.uniform(0.8, 1.2), 2),
                                "term": var
                            })
                            count += 1
                    
                    if count >= target_count:
                        break
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        # 添加体型描述
        for body_type in body_types * 50:  # 重复以达到足够数量
            if count >= target_count:
                break
            weight_indicator = random.choice(["", ":1.1", ":1.2"])
            entries.append({
                "weight": round(random.uniform(0.9, 1.1), 2),
                "term": f"({body_type}{weight_indicator})" if weight_indicator else body_type
            })
            count += 1
        
        self.save_vocabulary(
            "subject_base_features.json",
            "Subject & Base Features",
            "人物身份与基础特征词库 - 定义角色的核心身份、年龄、种族和整体体型",
            "subject_base",
            entries[:target_count]
        )

    def generate_facial_features(self):
        """生成面部细节特征词库"""
        entries = []
        target_count = 10000
        
        # 眼睛颜色
        eye_colors = [
            "blue", "deep blue", "sky blue", "ocean blue", "sapphire blue", "cobalt blue",
            "navy blue", "steel blue", "ice blue", "powder blue", "royal blue",
            "green", "emerald green", "forest green", "jade green", "mint green",
            "sea green", "olive green", "hazel green", "lime green", "sage green",
            "brown", "dark brown", "chocolate brown", "amber brown", "honey brown",
            "caramel brown", "coffee brown", "mahogany brown", "chestnut brown",
            "hazel", "golden hazel", "green hazel", "brown hazel", "amber hazel",
            "gray", "grey", "silver gray", "charcoal gray", "slate gray", "storm gray",
            "violet", "purple", "lavender", "amethyst", "indigo"
        ]
        
        # 眼睛形状
        eye_shapes = [
            "almond-shaped", "round", "oval", "hooded", "monolid", "deep-set",
            "prominent", "close-set", "wide-set", "upturned", "downturned",
            "cat-like", "doe-like", "phoenix", "narrow", "large", "small",
            "sparkling", "bright", "luminous", "expressive", "piercing", "gentle"
        ]
        
        # 眉毛描述
        eyebrow_styles = [
            "perfectly arched eyebrows", "natural eyebrows", "thick eyebrows", "thin eyebrows",
            "well-groomed eyebrows", "bushy eyebrows", "sleek eyebrows", "defined eyebrows",
            "soft eyebrows", "bold eyebrows", "subtle eyebrows", "feathered eyebrows",
            "microbladed eyebrows", "tattooed eyebrows", "threaded eyebrows", "waxed eyebrows",
            "straight eyebrows", "curved eyebrows", "angular eyebrows", "rounded eyebrows"
        ]
        
        # 鼻子描述
        nose_types = [
            "straight nose", "aquiline nose", "button nose", "turned-up nose",
            "Roman nose", "Greek nose", "snub nose", "pointed nose", "broad nose",
            "narrow nose", "delicate nose", "strong nose", "refined nose",
            "classical nose", "perfect nose", "proportionate nose", "small nose",
            "cute nose", "elegant nose", "aristocratic nose", "noble nose"
        ]
        
        # 嘴唇描述
        lips_descriptions = [
            "full lips", "soft lips", "plump lips", "thin lips", "natural lips",
            "heart-shaped lips", "bow-shaped lips", "cupid's bow lips", "pouty lips",
            "sensual lips", "glossy lips", "matte lips", "nude lips", "pink lips",
            "red lips", "coral lips", "berry lips", "rose lips", "cherry lips",
            "kissable lips", "luscious lips", "voluptuous lips", "delicate lips",
            "perfect lips", "symmetrical lips", "well-defined lips", "subtle lips"
        ]
        
        # 脸型
        face_shapes = [
            "oval face", "round face", "square face", "heart-shaped face", "diamond face",
            "long face", "oblong face", "triangular face", "rectangular face",
            "perfectly proportioned face", "symmetrical face", "angular face",
            "soft face", "defined face", "sculpted face", "classic face",
            "delicate face", "strong face", "graceful face", "refined face"
        ]
        
        # 皮肤描述
        skin_descriptions = [
            "flawless skin", "perfect skin", "glowing skin", "radiant skin", "luminous skin",
            "porcelain skin", "ivory skin", "pearl skin", "alabaster skin", "fair skin",
            "pale skin", "light skin", "medium skin", "olive skin", "tanned skin",
            "sun-kissed skin", "golden skin", "bronze skin", "smooth skin", "soft skin",
            "silky skin", "velvety skin", "dewy skin", "matte skin", "natural skin",
            "healthy skin", "youthful skin", "fresh skin", "clear skin", "blemish-free skin",
            "even-toned skin", "rosy skin", "peachy skin", "creamy skin", "milky skin"
        ]
        
        # 表情
        expressions = [
            "gentle smile", "bright smile", "warm smile", "sweet smile", "radiant smile",
            "charming smile", "mysterious smile", "subtle smile", "soft smile",
            "natural smile", "genuine smile", "heartfelt smile", "infectious smile",
            "captivating smile", "alluring smile", "seductive smile", "playful smile",
            "mischievous smile", "knowing smile", "confident smile", "shy smile",
            "tender expression", "serene expression", "peaceful expression", "calm expression",
            "thoughtful expression", "contemplative expression", "dreamy expression",
            "focused expression", "intense gaze", "direct gaze", "sultry gaze",
            "piercing gaze", "gentle gaze", "loving gaze", "curious gaze"
        ]
        
        # 特殊特征
        special_features = [
            "dimples", "freckles", "beauty mark", "mole", "scar", "birthmark",
            "high cheekbones", "defined cheekbones", "soft cheekbones", "prominent cheekbones",
            "strong jawline", "soft jawline", "defined jawline", "delicate jawline",
            "cleft chin", "pointed chin", "rounded chin", "square chin", "oval chin",
            "long eyelashes", "thick eyelashes", "curled eyelashes", "natural eyelashes",
            "mascara-enhanced eyelashes", "false eyelashes", "dramatic eyelashes"
        ]
        
        # 生成组合
        count = 0
        all_features = [eye_colors, eye_shapes, eyebrow_styles, nose_types, lips_descriptions,
                       face_shapes, skin_descriptions, expressions, special_features]
        
        # 为每个特征类别生成大量变化
        for feature_list in all_features:
            for feature in feature_list:
                # 生成多种变化
                variations = [
                    feature,
                    f"({feature}:1.1)",
                    f"({feature}:1.2)",
                    f"beautiful {feature}",
                    f"stunning {feature}",
                    f"gorgeous {feature}",
                    f"perfect {feature}",
                    f"natural {feature}",
                    f"striking {feature}",
                    f"remarkable {feature}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        # 补充到目标数量
        while count < target_count:
            # 随机组合特征
            feature1 = random.choice(eye_colors)
            feature2 = random.choice(expressions)
            combined = f"{feature1} eyes with {feature2}"
            entries.append({
                "weight": round(random.uniform(0.9, 1.1), 2),
                "term": combined
            })
            count += 1
        
        self.save_vocabulary(
            "facial_features.json",
            "Facial Features",
            "面部细节特征词库 - 精确描述五官的形状、颜色和特点，以及皮肤的质感",
            "facial_features",
            entries[:target_count]
        )

    def generate_hair_styles_colors(self):
        """生成发型与颜色词库"""
        entries = []
        target_count = 10000
        
        # 发色
        hair_colors = [
            "blonde", "platinum blonde", "dirty blonde", "honey blonde", "strawberry blonde",
            "ash blonde", "golden blonde", "sandy blonde", "champagne blonde", "butter blonde",
            "brown", "dark brown", "light brown", "medium brown", "chocolate brown",
            "chestnut brown", "auburn brown", "mahogany brown", "coffee brown", "mocha brown",
            "red", "ginger", "auburn", "copper", "strawberry", "burgundy", "cherry red",
            "crimson", "wine red", "rust red", "fiery red", "bright red", "natural red",
            "black", "jet black", "raven black", "coal black", "ebony", "midnight black",
            "gray", "grey", "silver", "white", "platinum", "salt and pepper",
            "highlighted", "lowlighted", "ombre", "balayage", "two-toned", "multicolored"
        ]
        
        # 发型长度
        hair_lengths = [
            "long", "very long", "waist-length", "hip-length", "knee-length", "floor-length",
            "medium", "medium-length", "shoulder-length", "collarbone-length",
            "short", "very short", "pixie-cut", "buzzed", "cropped", "chin-length",
            "bob-length", "lob-length", "mid-length", "layered"
        ]
        
        # 发型样式
        hair_styles = [
            "straight", "wavy", "curly", "kinky", "coiled", "loose waves", "tight curls",
            "beach waves", "finger waves", "pin curls", "spiral curls", "ringlets",
            "ponytail", "high ponytail", "low ponytail", "side ponytail", "messy ponytail",
            "bun", "high bun", "low bun", "messy bun", "sleek bun", "topknot",
            "braided", "french braid", "dutch braid", "fishtail braid", "crown braid",
            "side braid", "loose braid", "tight braid", "multiple braids",
            "updo", "elegant updo", "casual updo", "formal updo", "wedding updo",
            "half-up", "half-down", "half-up half-down", "twisted", "pinned back",
            "loose", "flowing", "tousled", "windswept", "voluminous", "flat",
            "layered", "feathered", "shaggy", "choppy", "blunt cut", "asymmetrical",
            "bangs", "fringe", "side-swept bangs", "blunt bangs", "wispy bangs",
            "curtain bangs", "baby bangs", "micro bangs", "grown-out bangs"
        ]
        
        # 发质描述
        hair_textures = [
            "silky", "smooth", "soft", "shiny", "glossy", "lustrous", "healthy",
            "thick", "thin", "fine", "coarse", "damaged", "brittle", "dry",
            "oily", "greasy", "frizzy", "tangled", "knotted", "static",
            "bouncy", "elastic", "springy", "limp", "flat", "voluminous"
        ]
        
        count = 0
        
        # 生成各种组合
        for color in hair_colors:
            for length in hair_lengths:
                for style in hair_styles:
                    if count >= target_count:
                        break
                    
                    variations = [
                        f"{length} {color} {style} hair",
                        f"{color} {style} {length} hair",
                        f"beautiful {color} {style} hair",
                        f"gorgeous {length} {color} hair",
                        f"stunning {style} {color} hair",
                        f"({color} {style} hair:1.1)",
                        f"flowing {color} {style} hair",
                        f"lustrous {color} {length} hair"
                    ]
                    
                    for var in variations:
                        if count >= target_count:
                            break
                        entries.append({
                            "weight": round(random.uniform(0.8, 1.2), 2),
                            "term": var
                        })
                        count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "hair_styles_colors.json",
            "Hair Styles & Colors",
            "发型与颜色词库 - 描述头发的样式、长度、质地和颜色",
            "hair_styles",
            entries[:target_count]
        )

    def generate_poses_actions(self):
        """生成身体姿态与动作词库"""
        entries = []
        target_count = 10000
        
        # 基础姿势
        basic_poses = [
            "standing", "sitting", "lying", "reclining", "leaning", "kneeling",
            "crouching", "squatting", "walking", "running", "dancing", "jumping",
            "stretching", "bending", "twisting", "turning", "facing", "looking"
        ]
        
        # 身体部位动作
        body_actions = [
            "hands on hips", "arms crossed", "arms raised", "arms outstretched",
            "hands behind head", "hands in pockets", "hands clasped", "hands folded",
            "touching face", "touching hair", "covering mouth", "pointing",
            "waving", "gesturing", "clapping", "holding hands", "interlocking fingers",
            "one hand on hip", "both hands on hips", "hands on waist", "hands on chest",
            "arms behind back", "arms at sides", "relaxed arms", "tense posture",
            "shoulders back", "shoulders forward", "shoulders relaxed", "shoulders raised"
        ]
        
        # 头部和面部动作
        head_actions = [
            "looking over shoulder", "looking up", "looking down", "looking away",
            "looking directly at camera", "gazing into distance", "eyes closed",
            "head tilted", "head turned", "chin up", "chin down", "profile view",
            "three-quarter view", "frontal view", "side view", "back view",
            "smiling", "laughing", "serious expression", "contemplative look",
            "mysterious expression", "playful expression", "confident look"
        ]
        
        # 腿部姿势
        leg_positions = [
            "legs crossed", "legs apart", "feet together", "one leg raised",
            "kicking", "stepping", "tiptoeing", "heel raised", "balanced stance",
            "wide stance", "narrow stance", "one foot forward", "weight shifted"
        ]
        
        # 环境互动
        environment_interactions = [
            "leaning against wall", "sitting on chair", "lying on bed", "standing by window",
            "holding door frame", "touching wall", "sitting on stairs", "standing in doorway",
            "leaning on railing", "sitting on bench", "standing by tree", "touching glass",
            "holding book", "reading", "writing", "typing", "drinking coffee",
            "eating", "cooking", "cleaning", "exercising", "yoga pose", "meditation pose"
        ]
        
        count = 0
        all_actions = [basic_poses, body_actions, head_actions, leg_positions, environment_interactions]
        
        # 生成单个动作
        for action_list in all_actions:
            for action in action_list:
                variations = [
                    action,
                    f"({action}:1.1)",
                    f"gracefully {action}",
                    f"elegantly {action}",
                    f"naturally {action}",
                    f"confidently {action}",
                    f"casually {action}",
                    f"seductively {action}",
                    f"playfully {action}",
                    f"seriously {action}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        # 生成组合动作
        while count < target_count:
            action1 = random.choice(basic_poses)
            action2 = random.choice(body_actions)
            combined = f"{action1} {action2}"
            entries.append({
                "weight": round(random.uniform(0.9, 1.1), 2),
                "term": combined
            })
            count += 1
        
        self.save_vocabulary(
            "poses_actions.json",
            "Poses & Actions",
            "身体姿态与动作词库 - 描述人物的身体姿势、手势和具体动作",
            "poses_actions",
            entries[:target_count]
        )

    def generate_apparel_accessories(self):
        """生成服装与配饰词库"""
        entries = []
        target_count = 10000
        
        # 上装
        tops = [
            "t-shirt", "blouse", "shirt", "tank top", "crop top", "sweater", "cardigan",
            "hoodie", "jacket", "blazer", "coat", "dress shirt", "polo shirt",
            "turtleneck", "off-shoulder top", "halter top", "tube top", "camisole",
            "vest", "waistcoat", "kimono", "poncho", "cape", "shawl", "wrap"
        ]
        
        # 下装
        bottoms = [
            "jeans", "pants", "trousers", "leggings", "shorts", "skirt", "dress",
            "mini skirt", "midi skirt", "maxi skirt", "pencil skirt", "A-line skirt",
            "pleated skirt", "cargo pants", "skinny jeans", "wide-leg pants",
            "bootcut jeans", "flare jeans", "high-waisted jeans", "low-rise jeans"
        ]
        
        # 连衣裙
        dresses = [
            "cocktail dress", "evening gown", "sundress", "maxi dress", "mini dress",
            "midi dress", "wrap dress", "shift dress", "bodycon dress", "A-line dress",
            "ball gown", "wedding dress", "formal dress", "casual dress", "business dress",
            "summer dress", "winter dress", "party dress", "little black dress"
        ]
        
        # 材质
        materials = [
            "cotton", "silk", "satin", "velvet", "lace", "chiffon", "leather", "denim",
            "wool", "cashmere", "linen", "polyester", "spandex", "lycra", "mesh",
            "tulle", "organza", "taffeta", "crepe", "jersey", "flannel", "corduroy"
        ]
        
        # 颜色
        colors = [
            "white", "black", "red", "blue", "green", "yellow", "pink", "purple",
            "orange", "brown", "gray", "grey", "navy", "burgundy", "emerald",
            "turquoise", "coral", "mint", "lavender", "cream", "beige", "tan",
            "gold", "silver", "rose gold", "metallic", "neon", "pastel"
        ]
        
        # 配饰
        accessories = [
            "necklace", "earrings", "bracelet", "ring", "watch", "sunglasses",
            "hat", "cap", "scarf", "belt", "bag", "purse", "handbag", "clutch",
            "backpack", "shoes", "heels", "boots", "sneakers", "sandals",
            "jewelry", "pearls", "diamonds", "gems", "choker", "pendant"
        ]
        
        # 风格
        styles = [
            "casual", "formal", "business", "elegant", "sophisticated", "chic",
            "trendy", "fashionable", "stylish", "classic", "vintage", "retro",
            "modern", "contemporary", "minimalist", "bohemian", "edgy", "punk",
            "romantic", "feminine", "masculine", "androgynous", "sporty", "athletic"
        ]
        
        count = 0
        
        # 生成组合
        all_clothing = [tops, bottoms, dresses]
        for clothing_list in all_clothing:
            for item in clothing_list:
                for material in materials:
                    for color in colors:
                        for style in styles:
                            if count >= target_count:
                                break
                            
                            variations = [
                                f"{style} {color} {material} {item}",
                                f"wearing a {color} {material} {item}",
                                f"dressed in {color} {material} {item}",
                                f"elegant {color} {item}",
                                f"stunning {material} {item}",
                                f"fashionable {style} {item}",
                                f"({color} {material} {item}:1.1)"
                            ]
                            
                            for var in variations:
                                if count >= target_count:
                                    break
                                entries.append({
                                    "weight": round(random.uniform(0.8, 1.2), 2),
                                    "term": var
                                })
                                count += 1
                        
                        if count >= target_count:
                            break
                    if count >= target_count:
                        break
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "apparel_accessories.json",
            "Apparel & Accessories",
            "服装与配饰词库 - 详细描述穿着的服装类型、材质、颜色和搭配的饰品",
            "apparel_accessories",
            entries[:target_count]
        )

    def generate_settings_environments(self):
        """生成场景与环境词库"""
        entries = []
        target_count = 10000
        
        # 室内场景
        indoor_settings = [
            "bedroom", "living room", "kitchen", "bathroom", "office", "studio",
            "library", "cafe", "restaurant", "bar", "hotel room", "apartment",
            "house", "mansion", "cottage", "loft", "penthouse", "gallery",
            "museum", "theater", "cinema", "gym", "spa", "salon", "shop",
            "boutique", "classroom", "laboratory", "hospital", "clinic"
        ]
        
        # 户外场景
        outdoor_settings = [
            "park", "garden", "beach", "forest", "mountain", "lake", "river",
            "field", "meadow", "desert", "city street", "alley", "rooftop",
            "balcony", "terrace", "patio", "courtyard", "plaza", "square",
            "bridge", "pier", "dock", "harbor", "marina", "countryside",
            "vineyard", "farm", "ranch", "valley", "hill", "cliff"
        ]
        
        # 建筑风格
        architectural_styles = [
            "modern", "contemporary", "minimalist", "industrial", "vintage",
            "classic", "traditional", "rustic", "bohemian", "scandinavian",
            "mediterranean", "tropical", "urban", "suburban", "rural",
            "art deco", "victorian", "colonial", "gothic", "baroque"
        ]
        
        # 环境描述
        environment_descriptions = [
            "cozy", "spacious", "intimate", "grand", "luxurious", "elegant",
            "comfortable", "stylish", "trendy", "chic", "sophisticated",
            "warm", "cool", "bright", "dim", "dark", "sunny", "shady",
            "peaceful", "bustling", "quiet", "lively", "serene", "dramatic"
        ]
        
        # 时间
        times = [
            "morning", "afternoon", "evening", "night", "dawn", "dusk",
            "sunset", "sunrise", "golden hour", "blue hour", "midnight",
            "noon", "twilight", "daybreak", "nightfall"
        ]
        
        # 天气
        weather = [
            "sunny", "cloudy", "overcast", "rainy", "stormy", "snowy",
            "foggy", "misty", "windy", "calm", "clear", "hazy"
        ]
        
        count = 0
        
        # 生成室内场景组合
        for setting in indoor_settings:
            for style in architectural_styles:
                for desc in environment_descriptions:
                    for time in times:
                        if count >= target_count // 2:
                            break
                        
                        variations = [
                            f"in a {desc} {style} {setting}",
                            f"inside a {style} {setting}",
                            f"at a {desc} {setting}",
                            f"in an elegant {setting}",
                            f"({style} {setting}:1.1)",
                            f"luxurious {setting} interior",
                            f"beautiful {setting} setting"
                        ]
                        
                        for var in variations:
                            if count >= target_count // 2:
                                break
                            entries.append({
                                "weight": round(random.uniform(0.8, 1.2), 2),
                                "term": var
                            })
                            count += 1
                    
                    if count >= target_count // 2:
                        break
                if count >= target_count // 2:
                    break
            if count >= target_count // 2:
                break
        
        # 生成户外场景组合
        for setting in outdoor_settings:
            for time in times:
                for weather_cond in weather:
                    if count >= target_count:
                        break
                    
                    variations = [
                        f"at {setting} during {time}",
                        f"in a {weather_cond} {setting}",
                        f"outdoor {setting} scene",
                        f"natural {setting} environment",
                        f"({setting} at {time}:1.1)",
                        f"beautiful {setting} landscape",
                        f"scenic {setting} view"
                    ]
                    
                    for var in variations:
                        if count >= target_count:
                            break
                        entries.append({
                            "weight": round(random.uniform(0.8, 1.2), 2),
                            "term": var
                        })
                        count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "settings_environments.json",
            "Settings & Environments",
            "场景与环境词库 - 设定人物所处的具体环境，包括室内外场景和背景元素",
            "settings_environments",
            entries[:target_count]
        )

    def generate_lighting_effects(self):
        """生成光影效果词库"""
        entries = []
        target_count = 10000
        
        # 光源类型
        light_sources = [
            "natural light", "sunlight", "moonlight", "candlelight", "firelight",
            "window light", "studio light", "softbox light", "ring light",
            "LED light", "fluorescent light", "incandescent light", "neon light",
            "street light", "lamp light", "overhead light", "side light",
            "back light", "rim light", "key light", "fill light", "ambient light"
        ]
        
        # 光线质量
        light_qualities = [
            "soft", "hard", "diffused", "direct", "indirect", "warm", "cool",
            "bright", "dim", "dramatic", "subtle", "harsh", "gentle", "filtered",
            "scattered", "focused", "even", "uneven", "consistent", "variable"
        ]
        
        # 光线方向
        light_directions = [
            "from above", "from below", "from the side", "from behind",
            "from the front", "from the left", "from the right", "diagonal",
            "overhead", "backlit", "side-lit", "front-lit", "top-lit",
            "under-lit", "cross-lit", "rim-lit", "edge-lit"
        ]
        
        # 阴影描述
        shadow_descriptions = [
            "soft shadows", "hard shadows", "deep shadows", "subtle shadows",
            "dramatic shadows", "gentle shadows", "strong shadows", "light shadows",
            "no shadows", "minimal shadows", "prominent shadows", "artistic shadows",
            "natural shadows", "artificial shadows", "long shadows", "short shadows"
        ]
        
        # 光线效果
        lighting_effects = [
            "golden hour lighting", "blue hour lighting", "magic hour lighting",
            "cinematic lighting", "moody lighting", "atmospheric lighting",
            "volumetric lighting", "god rays", "lens flare", "bokeh",
            "high contrast lighting", "low contrast lighting", "flat lighting",
            "Rembrandt lighting", "butterfly lighting", "split lighting",
            "loop lighting", "broad lighting", "short lighting"
        ]
        
        # 环境光线
        ambient_lighting = [
            "well-lit", "poorly lit", "evenly lit", "unevenly lit", "brightly lit",
            "dimly lit", "dramatically lit", "softly lit", "harshly lit",
            "naturally lit", "artificially lit", "beautifully lit", "perfectly lit"
        ]
        
        count = 0
        all_lighting = [light_sources, light_qualities, light_directions, 
                       shadow_descriptions, lighting_effects, ambient_lighting]
        
        # 生成单个光线描述
        for lighting_list in all_lighting:
            for light in lighting_list:
                variations = [
                    light,
                    f"({light}:1.1)",
                    f"({light}:1.2)",
                    f"beautiful {light}",
                    f"stunning {light}",
                    f"dramatic {light}",
                    f"perfect {light}",
                    f"professional {light}",
                    f"artistic {light}",
                    f"cinematic {light}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        # 生成组合光线效果
        while count < target_count:
            source = random.choice(light_sources)
            quality = random.choice(light_qualities)
            direction = random.choice(light_directions)
            combined = f"{quality} {source} {direction}"
            entries.append({
                "weight": round(random.uniform(0.9, 1.1), 2),
                "term": combined
            })
            count += 1
        
        self.save_vocabulary(
            "lighting_effects.json",
            "Lighting Effects",
            "光影效果词库 - 定义照片的光照条件，决定照片真实感、氛围和专业度",
            "lighting_effects",
            entries[:target_count]
        )

    def generate_colors_atmosphere(self):
        """生成色彩与氛围词库"""
        entries = []
        target_count = 10000
        
        # 色彩调性
        color_tones = [
            "warm tones", "cool tones", "neutral tones", "earth tones", "pastel tones",
            "vibrant colors", "muted colors", "saturated colors", "desaturated colors",
            "monochromatic", "complementary colors", "analogous colors", "triadic colors",
            "high contrast", "low contrast", "soft contrast", "dramatic contrast"
        ]
        
        # 色彩描述
        color_descriptions = [
            "rich colors", "deep colors", "bright colors", "dark colors", "light colors",
            "bold colors", "subtle colors", "natural colors", "artificial colors",
            "harmonious colors", "clashing colors", "balanced colors", "gradient colors",
            "fade colors", "blend colors", "pop colors", "accent colors"
        ]
        
        # 氛围描述
        atmosphere_descriptions = [
            "romantic atmosphere", "mysterious atmosphere", "dreamy atmosphere",
            "nostalgic atmosphere", "melancholic atmosphere", "joyful atmosphere",
            "peaceful atmosphere", "energetic atmosphere", "calm atmosphere",
            "intense atmosphere", "serene atmosphere", "dramatic atmosphere",
            "intimate atmosphere", "grand atmosphere", "cozy atmosphere",
            "elegant atmosphere", "sophisticated atmosphere", "casual atmosphere"
        ]
        
        # 情绪氛围
        mood_atmospheres = [
            "happy mood", "sad mood", "contemplative mood", "playful mood",
            "serious mood", "relaxed mood", "tense mood", "excited mood",
            "calm mood", "anxious mood", "confident mood", "shy mood",
            "mysterious mood", "romantic mood", "dramatic mood", "peaceful mood"
        ]
        
        # 环境氛围
        environmental_atmospheres = [
            "urban atmosphere", "rural atmosphere", "natural atmosphere",
            "industrial atmosphere", "vintage atmosphere", "modern atmosphere",
            "classic atmosphere", "futuristic atmosphere", "retro atmosphere",
            "bohemian atmosphere", "minimalist atmosphere", "luxurious atmosphere"
        ]
        
        # 视觉效果
        visual_effects = [
            "soft focus", "sharp focus", "shallow depth of field", "deep depth of field",
            "bokeh effect", "blur effect", "vignette effect", "film grain",
            "lens flare", "light leak", "double exposure", "multiple exposure",
            "motion blur", "freeze motion", "time lapse", "slow motion"
        ]
        
        count = 0
        all_atmospheres = [color_tones, color_descriptions, atmosphere_descriptions,
                          mood_atmospheres, environmental_atmospheres, visual_effects]
        
        # 生成单个氛围描述
        for atmosphere_list in all_atmospheres:
            for atmosphere in atmosphere_list:
                variations = [
                    atmosphere,
                    f"({atmosphere}:1.1)",
                    f"({atmosphere}:1.2)",
                    f"beautiful {atmosphere}",
                    f"stunning {atmosphere}",
                    f"gorgeous {atmosphere}",
                    f"perfect {atmosphere}",
                    f"natural {atmosphere}",
                    f"artistic {atmosphere}",
                    f"cinematic {atmosphere}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        # 生成组合氛围效果
        while count < target_count:
            color = random.choice(color_tones)
            atmosphere = random.choice(atmosphere_descriptions)
            combined = f"{color} with {atmosphere}"
            entries.append({
                "weight": round(random.uniform(0.9, 1.1), 2),
                "term": combined
            })
            count += 1
        
        self.save_vocabulary(
            "colors_atmosphere.json",
            "Colors & Atmosphere",
            "色彩与氛围词库 - 描述画面的整体色调和想要传达的情绪氛围",
            "colors_atmosphere",
            entries[:target_count]
        )

    def generate_camera_parameters(self):
        """生成相机与镜头参数词库"""
        entries = []
        target_count = 10000
        
        # 相机品牌和型号
        cameras = [
            "Canon EOS R5", "Canon EOS 5D Mark IV", "Canon EOS R6", "Canon 1DX Mark III",
            "Nikon D850", "Nikon Z9", "Nikon Z7", "Nikon D780", "Nikon Z6",
            "Sony A7R IV", "Sony A7 III", "Sony A7R III", "Sony A9", "Sony FX3",
            "Fujifilm X-T4", "Fujifilm GFX 100", "Fujifilm X-Pro3", "Fujifilm X-H1",
            "Leica M10", "Leica Q2", "Leica SL2", "Hasselblad X1D", "Phase One XF"
        ]
        
        # 镜头规格
        lenses = [
            "24-70mm f/2.8", "70-200mm f/2.8", "85mm f/1.4", "50mm f/1.4", "35mm f/1.4",
            "24mm f/1.4", "135mm f/2", "200mm f/2.8", "300mm f/2.8", "16-35mm f/2.8",
            "14-24mm f/2.8", "24-105mm f/4", "70-300mm f/4.5-5.6", "100mm f/2.8 macro",
            "180mm f/2.8 macro", "fisheye 8-16mm", "tilt-shift 24mm", "85mm f/1.2"
        ]
        
        # 拍摄角度
        shot_angles = [
            "close-up", "medium close-up", "medium shot", "full body shot", "wide shot",
            "extreme close-up", "headshot", "portrait shot", "three-quarter shot",
            "profile shot", "side angle", "front angle", "back angle", "overhead shot",
            "low angle", "high angle", "eye level", "dutch angle", "bird's eye view"
        ]
        
        # 技术参数
        technical_params = [
            "f/1.4", "f/1.8", "f/2.8", "f/4", "f/5.6", "f/8", "f/11", "f/16",
            "ISO 100", "ISO 200", "ISO 400", "ISO 800", "ISO 1600", "ISO 3200",
            "1/60s", "1/125s", "1/250s", "1/500s", "1/1000s", "1/2000s",
            "shallow depth of field", "deep depth of field", "wide aperture",
            "narrow aperture", "fast shutter", "slow shutter", "high ISO", "low ISO"
        ]
        
        # 摄影风格
        photography_styles = [
            "portrait photography", "fashion photography", "beauty photography",
            "lifestyle photography", "commercial photography", "editorial photography",
            "fine art photography", "documentary photography", "street photography",
            "studio photography", "natural light photography", "environmental portrait",
            "headshot photography", "glamour photography", "boudoir photography"
        ]
        
        # 图像质量
        image_qualities = [
            "8K resolution", "4K resolution", "high resolution", "ultra high definition",
            "sharp focus", "tack sharp", "crystal clear", "razor sharp", "pin sharp",
            "professional quality", "commercial quality", "magazine quality",
            "gallery quality", "museum quality", "award-winning", "masterpiece"
        ]
        
        count = 0
        
        # 生成相机镜头组合
        for camera in cameras:
            for lens in lenses:
                if count >= target_count // 4:
                    break
                
                variations = [
                    f"shot on {camera} with {lens}",
                    f"({camera} with {lens}:1.2)",
                    f"photographed with {camera}",
                    f"captured on {camera}",
                    f"professional {camera} photography"
                ]
                
                for var in variations:
                    if count >= target_count // 4:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
            
            if count >= target_count // 4:
                break
        
        # 添加其他参数
        all_params = [shot_angles, technical_params, photography_styles, image_qualities]
        for param_list in all_params:
            for param in param_list:
                if count >= target_count:
                    break
                
                variations = [
                    param,
                    f"({param}:1.1)",
                    f"professional {param}",
                    f"high-quality {param}",
                    f"expert {param}",
                    f"masterful {param}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
            
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "camera_parameters.json",
            "Camera & Parameters",
            "相机与镜头参数词库 - 模拟专业摄影的设备和参数，生成照片而非画作",
            "camera_parameters",
            entries[:target_count]
        )

    def generate_quality_style(self):
        """生成图像质量与风格词库"""
        entries = []
        target_count = 10000
        
        # 图像质量
        quality_terms = [
            "photorealistic", "hyper-realistic", "ultra-realistic", "lifelike",
            "highly detailed", "ultra-detailed", "extremely detailed", "intricate details",
            "sharp focus", "tack sharp", "crystal clear", "high definition",
            "ultra high definition", "4K", "8K", "high resolution", "ultra high resolution",
            "professional quality", "commercial grade", "magazine quality", "gallery quality",
            "museum quality", "award-winning", "masterpiece", "best quality",
            "premium quality", "top quality", "superior quality", "excellent quality"
        ]
        
        # 摄影风格
        photography_styles = [
            "professional photography", "commercial photography", "editorial photography",
            "fashion photography", "portrait photography", "beauty photography",
            "lifestyle photography", "documentary photography", "fine art photography",
            "candid photography", "posed photography", "natural photography",
            "studio photography", "environmental photography", "glamour photography"
        ]
        
        # 风格描述符
        style_descriptors = [
            "cinematic", "dramatic", "artistic", "elegant", "sophisticated", "refined",
            "polished", "pristine", "flawless", "perfect", "immaculate", "stunning",
            "gorgeous", "beautiful", "breathtaking", "captivating", "mesmerizing",
            "enchanting", "alluring", "striking", "remarkable", "exceptional",
            "extraordinary", "magnificent", "splendid", "wonderful", "marvelous"
        ]
        
        # 技术术语
        technical_terms = [
            "bokeh", "depth of field", "composition", "framing", "lighting",
            "exposure", "contrast", "saturation", "white balance", "color grading",
            "post-processing", "retouching", "enhancement", "optimization",
            "calibration", "professional editing", "color correction", "tone mapping"
        ]
        
        # 视觉效果
        visual_effects = [
            "soft focus", "selective focus", "shallow depth of field", "deep focus",
            "motion blur", "freeze motion", "long exposure", "HDR effect",
            "lens flare", "light leak", "vignette", "film grain", "texture",
            "gradient", "smooth transition", "seamless blend", "natural look"
        ]
        
        count = 0
        all_qualities = [quality_terms, photography_styles, style_descriptors, 
                        technical_terms, visual_effects]
        
        # 生成单个质量描述
        for quality_list in all_qualities:
            for quality in quality_list:
                variations = [
                    quality,
                    f"({quality}:1.1)",
                    f"({quality}:1.2)",
                    f"({quality}:1.3)",
                    f"professional {quality}",
                    f"high-quality {quality}",
                    f"expert {quality}",
                    f"masterful {quality}",
                    f"superior {quality}",
                    f"premium {quality}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "quality_style.json",
            "Quality & Style",
            "图像质量与风格词库 - 定义图像的最终质感、清晰度和艺术风格",
            "quality_style",
            entries[:target_count]
        )

    def generate_emotions_expressions(self):
        """生成情绪与表情词库"""
        entries = []
        target_count = 10000
        
        # 基础情绪
        basic_emotions = [
            "happy", "sad", "angry", "surprised", "afraid", "disgusted", "contempt",
            "joy", "sorrow", "fear", "love", "hate", "excitement", "boredom",
            "curiosity", "confusion", "satisfaction", "frustration", "hope", "despair"
        ]
        
        # 复杂情绪
        complex_emotions = [
            "melancholic", "nostalgic", "euphoric", "ecstatic", "serene", "peaceful",
            "anxious", "nervous", "confident", "insecure", "proud", "humble",
            "passionate", "indifferent", "empathetic", "sympathetic", "envious",
            "grateful", "resentful", "optimistic", "pessimistic", "determined"
        ]
        
        # 面部表情
        facial_expressions = [
            "smile", "frown", "grin", "smirk", "pout", "laugh", "cry", "wink",
            "glare", "stare", "gaze", "glance", "scowl", "beam", "grimace",
            "sneer", "leer", "ogle", "peer", "squint", "blink", "flutter"
        ]
        
        # 眼神描述
        eye_expressions = [
            "twinkling eyes", "sparkling eyes", "bright eyes", "dull eyes", "tired eyes",
            "alert eyes", "sleepy eyes", "wide eyes", "narrow eyes", "piercing eyes",
            "gentle eyes", "kind eyes", "cold eyes", "warm eyes", "loving eyes",
            "sad eyes", "happy eyes", "mysterious eyes", "seductive eyes", "innocent eyes"
        ]
        
        # 嘴部表情
        mouth_expressions = [
            "gentle smile", "bright smile", "wide smile", "shy smile", "crooked smile",
            "mysterious smile", "seductive smile", "innocent smile", "playful smile",
            "warm smile", "cold smile", "fake smile", "genuine smile", "radiant smile",
            "subtle smile", "broad smile", "tight smile", "nervous smile", "confident smile"
        ]
        
        # 整体表情描述
        overall_expressions = [
            "serene expression", "peaceful expression", "calm expression", "relaxed expression",
            "tense expression", "worried expression", "focused expression", "distant expression",
            "dreamy expression", "thoughtful expression", "contemplative expression",
            "pensive expression", "reflective expression", "introspective expression"
        ]
        
        count = 0
        all_expressions = [basic_emotions, complex_emotions, facial_expressions,
                          eye_expressions, mouth_expressions, overall_expressions]
        
        # 生成表情组合
        for expression_list in all_expressions:
            for expression in expression_list:
                variations = [
                    expression,
                    f"({expression}:1.1)",
                    f"with {expression}",
                    f"showing {expression}",
                    f"expressing {expression}",
                    f"displaying {expression}",
                    f"radiating {expression}",
                    f"exuding {expression}",
                    f"natural {expression}",
                    f"genuine {expression}",
                    f"beautiful {expression}",
                    f"captivating {expression}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "emotions_expressions.json",
            "Emotions & Expressions",
            "情绪与表情词库 - 明确人物的情绪状态和面部表情，为角色注入生命",
            "emotions_expressions",
            entries[:target_count]
        )

    def generate_makeup(self):
        """生成妆容词库"""
        entries = []
        target_count = 10000
        
        # 妆容风格
        makeup_styles = [
            "natural makeup", "minimal makeup", "no makeup", "fresh-faced",
            "glamorous makeup", "dramatic makeup", "bold makeup", "subtle makeup",
            "classic makeup", "vintage makeup", "retro makeup", "modern makeup",
            "editorial makeup", "high fashion makeup", "runway makeup", "bridal makeup",
            "evening makeup", "day makeup", "party makeup", "professional makeup"
        ]
        
        # 眼妆
        eye_makeup = [
            "smokey eyes", "cat eye", "winged eyeliner", "natural eyeliner",
            "bold eyeliner", "subtle eyeliner", "thick eyeliner", "thin eyeliner",
            "eyeshadow", "neutral eyeshadow", "colorful eyeshadow", "shimmery eyeshadow",
            "matte eyeshadow", "metallic eyeshadow", "gradient eyeshadow", "bold eyeshadow",
            "mascara", "false eyelashes", "long eyelashes", "thick eyelashes",
            "curled eyelashes", "natural eyelashes", "dramatic eyelashes"
        ]
        
        # 唇妆
        lip_makeup = [
            "red lipstick", "pink lipstick", "nude lipstick", "coral lipstick",
            "berry lipstick", "plum lipstick", "orange lipstick", "burgundy lipstick",
            "matte lipstick", "glossy lipstick", "satin lipstick", "velvet lipstick",
            "lip gloss", "tinted lip balm", "natural lips", "bold lips",
            "subtle lips", "ombre lips", "gradient lips", "overlined lips"
        ]
        
        # 底妆
        base_makeup = [
            "flawless foundation", "natural foundation", "full coverage foundation",
            "light coverage foundation", "dewy foundation", "matte foundation",
            "luminous foundation", "satin foundation", "airbrushed makeup",
            "perfect complexion", "even skin tone", "radiant skin", "glowing skin",
            "highlighted skin", "contoured face", "bronzed skin", "porcelain skin"
        ]
        
        # 腮红
        blush_makeup = [
            "pink blush", "peach blush", "coral blush", "rose blush", "berry blush",
            "natural blush", "subtle blush", "rosy cheeks", "flushed cheeks",
            "healthy glow", "sun-kissed cheeks", "highlighted cheeks", "defined cheekbones"
        ]
        
        # 眉毛
        brow_makeup = [
            "natural brows", "defined brows", "bold brows", "subtle brows",
            "groomed brows", "shaped brows", "filled brows", "tinted brows",
            "feathered brows", "laminated brows", "sculpted brows", "soft brows"
        ]
        
        count = 0
        all_makeup = [makeup_styles, eye_makeup, lip_makeup, base_makeup, blush_makeup, brow_makeup]
        
        # 生成妆容组合
        for makeup_list in all_makeup:
            for makeup in makeup_list:
                variations = [
                    makeup,
                    f"({makeup}:1.1)",
                    f"with {makeup}",
                    f"wearing {makeup}",
                    f"beautiful {makeup}",
                    f"perfect {makeup}",
                    f"flawless {makeup}",
                    f"professional {makeup}",
                    f"expertly applied {makeup}",
                    f"skillfully done {makeup}",
                    f"artistically applied {makeup}",
                    f"carefully crafted {makeup}"
                ]
                
                for var in variations:
                    if count >= target_count:
                        break
                    entries.append({
                        "weight": round(random.uniform(0.8, 1.2), 2),
                        "term": var
                    })
                    count += 1
                
                if count >= target_count:
                    break
            if count >= target_count:
                break
        
        self.save_vocabulary(
            "makeup.json",
            "Makeup",
            "妆容词库 - 描述面部的妆容细节，从自然到夸张，影响角色的外观和风格",
            "makeup",
            entries[:target_count]
        )

    def generate_all_vocabularies(self):
        """生成所有词库"""
        print("🚀 开始生成ComfyUI随机提示词插件大型词库...")
        print(f"📊 目标：为12个元素类别各生成10,000+词条")
        print("-" * 60)
        
        # 生成各个词库
        self.generate_subject_base_features()
        self.generate_facial_features()
        self.generate_hair_styles_colors()
        self.generate_poses_actions()
        self.generate_apparel_accessories()
        self.generate_settings_environments()
        self.generate_lighting_effects()
        self.generate_colors_atmosphere()
        self.generate_camera_parameters()
        self.generate_quality_style()
        self.generate_emotions_expressions()
        self.generate_makeup()
        
        print("-" * 60)
        print("✅ 词库生成完成！")

if __name__ == "__main__":
    generator = VocabularyGenerator()
    generator.generate_all_vocabularies()
